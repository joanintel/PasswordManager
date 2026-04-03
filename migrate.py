#!/usr/bin/env python3
import json
from pathlib import Path
from getpass import getpass
from functions.encr import derive_key, encrypt_data

# Paths
BACKUP_FILE = Path(input("Enter path to your plaintext vault backup: ")).expanduser()
PM_DIR = Path.home() / ".pm"
SALT_FILE = PM_DIR / "salt.bin"
VAULT_FILE = PM_DIR / "vault.json"

# Load plaintext
with open(BACKUP_FILE, 'r') as f:
    data = json.load(f)

# Get password
password = getpass("Enter your master password: ")

# Load salt
with open(SALT_FILE, 'rb') as f:
    salt = f.read()

# Derive key and encrypt
key = derive_key(password, salt)
encrypted = encrypt_data(data, key)

# Save
with open(VAULT_FILE, 'wb') as f:
    f.write(encrypted)

print(f"✅ Migrated {len(data)} entries to encrypted vault")
