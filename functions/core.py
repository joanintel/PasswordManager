import sys
import json
from pathlib import Path
from getpass import getpass
from functions.encr import derive_key, generate_salt, decrypt_data, encrypt_data
from functions import colors as cl

# Storage paths
PM_DIR = Path.home() / ".pm"
VAULT_FILE = PM_DIR / "vault.json"
SALT_FILE = PM_DIR / "salt.bin"
CONFIG_FILE = PM_DIR / "config.json"


def ensure_storage():
    """Create ~/.pm directory, vault, salt, config, and verify master password"""

    # Create directory if it doesn't exist
    if not PM_DIR.exists():
        PM_DIR.mkdir(mode=0o700)
        print(f"[+] Created directory: {PM_DIR}")

    # --- Salt ---
    if not SALT_FILE.exists():
        salt = generate_salt()
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
        print(f"[+] Created new salt.")
    else:
        with open(SALT_FILE, "rb") as f:
            salt = f.read()

    # --- Config (first time setup) ---
    if not CONFIG_FILE.exists():
        username = input("Enter your name: ").strip()
        default_password_length = 12
        config = {
            "username": username,
            "vault_version": 1,
            "default_password_length": default_password_length
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
        print(f"[+] Created config file.")

    # --- Vault (first time setup) ---
    if not VAULT_FILE.exists():
        with open(VAULT_FILE, "w") as f:
            json.dump([], f, indent=4)
        print(f"[+] Created vault file: {VAULT_FILE}")

    # --- Master password ---
    # Check if this is first time (vault is empty/initial state OR we just created it)
    is_first_time = False
    
    # Read vault to check if it's the initial empty JSON or encrypted
    try:
        with open(VAULT_FILE, "rb") as f:
            raw_data = f.read()
            # If file starts with '{' or '[', it's plaintext JSON (first time, not encrypted yet)
            if raw_data and (raw_data[0] == ord('{') or raw_data[0] == ord('[')):
                is_first_time = True
    except:
        pass

    if is_first_time or not VAULT_FILE.exists():
        # First time setup - create new master password
        print(f"{cl.cyan}First time setup - Create your master password{cl.reset}")
        master_password = getpass("Enter master password: ").strip()
        confirm_password = getpass("Confirm master password: ").strip()
        
        if master_password != confirm_password:
            print(f"{cl.red}[!] Passwords do not match. Exiting.{cl.reset}")
            sys.exit(1)
        
        if not master_password:
            print(f"{cl.red}[!] Password cannot be empty.{cl.reset}")
            sys.exit(1)
        
        key = derive_key(master_password, salt)
        
        # Encrypt the empty vault immediately
        from functions.encr import encrypt_data
        empty_vault = []
        encrypted_vault = encrypt_data(empty_vault, key)
        with open(VAULT_FILE, "wb") as f:
            f.write(encrypted_vault)
        print(f"{cl.green}[+] Vault encrypted and saved.{cl.reset}")
        
        return key
    
    else:
        # Existing vault - verify master password
        max_attempts = 3
        for attempt in range(max_attempts):
            master_password = getpass(f"Enter master password (attempt {attempt + 1}/{max_attempts}): ").strip()
            key = derive_key(master_password, salt)
            
            # Test the key by trying to decrypt
            try:
                with open(VAULT_FILE, "rb") as f:
                    encrypted_data = f.read()
                test_decrypt = decrypt_data(encrypted_data, key)
                print(f"{cl.green}[+] Authentication successful{cl.reset}")
                return key
            except ValueError as e:
                if "MAC check failed" in str(e):
                    print(f"{cl.red}[!] Wrong master password{cl.reset}")
                else:
                    print(f"{cl.red}[!] Error: {e}{cl.reset}")
                
                if attempt == max_attempts - 1:
                    print(f"{cl.red}[!] Too many failed attempts. Exiting.{cl.reset}")
                    sys.exit(1)
        
        return key  # Should never reach here


def load_vault(key):
    """Load and decrypt vault"""
    try:
        with open(VAULT_FILE, "rb") as f:
            encrypted_data = f.read()

        if not encrypted_data:
            return []

        return decrypt_data(encrypted_data, key)
    
    except ValueError as e:
        if "MAC check failed" in str(e):
            print(f"{cl.red}[!] Wrong master password{cl.reset}")
        else:
            print(f"{cl.red}[!] Corrupted vault: {e}{cl.reset}")
        sys.exit(1)
    except Exception as e:
        print(f"{cl.red}[!] Failed to load vault: {e}{cl.reset}")
        sys.exit(1)


def save_vault(data, key):
    """Encrypt and save vault"""
    from functions.encr import encrypt_data

    encrypted_data = encrypt_data(data, key)
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted_data)
