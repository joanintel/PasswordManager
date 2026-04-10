import subprocess as sp
from functions.core import load_vault, save_vault
from .psd_gen import generate_password  # your password generator function
from functions import colors as cl  
from getpass import getpass




def add_entry(key):
    """Add a new password entry"""
    print(f"\n{cl.cyan}Add New Password{cl.reset}")
    print("-----------------")

    site = input("Site: ").strip()
    email = input("Email: ").strip()
    username = input("Username: ").strip()

    # Ask user if they want to generate a password
    use_gen = input("Generate password? (Y/N): ").strip().lower()
    if use_gen == "y":
        psd = generate_password()
        print(f"Generated password: {psd}")
    else:
        psd = input("Password: ").strip()

    option = input("Option: ").strip()

    # Load, append, save
    vault = load_vault(key)

    entry = {
        "site": site,
        "email": email,
        "username": username,
        "psd": psd,
        "option": option
    }

    vault.append(entry)
    save_vault(vault, key)
    print(f"{cl.green}[+] Entry added for site: {site}{cl.reset}")


def list_entries(key):
    #sp.run("clear")
    """List all stored entries"""
    print(f"{cl.cyan}\nStored Password Entries{cl.reset}")
    vault = load_vault(key)

    if not vault:
        print(f"{cl.red}No entries found.{cl.reset}")
        return

    for i, entry in enumerate(vault, start=1):
        print(
            f"{cl.green}{i}) Site:{cl.yellow} {entry.get('site','N/A')} "
            f"{cl.green}- Email:{cl.yellow} {entry.get('email','N/A')} "
            f"{cl.green}- Username:{cl.yellow} {entry.get('username','N/A')} "
            #f"{cl.green}- Option:{cl.yellow} {entry.get('option','N/A')}{cl.reset}"
        )

    print(f"{cl.green}\nTotal entries: {cl.cyan}{len(vault)}{cl.reset}")


def delete_entry(key):
    """Delete an entry from the vault by index number"""
    print(f"{cl.red}\nDelete Password Entry{cl.reset}")
    vault = load_vault(key)

    if not vault:
        print(f"{cl.red}No entries to delete.{cl.reset}")
        return

    for i, entry in enumerate(vault, start=1):
        print(
            f"{cl.green}{i}) Site:{cl.yellow} {entry.get('site','N/A')} "
            f"{cl.green}- Email:{cl.yellow} {entry.get('email','N/A')} "
            f"{cl.green}- Username:{cl.yellow} {entry.get('username','N/A')} "
            f"{cl.green}- Option:{cl.yellow} {entry.get('option','N/A')}{cl.reset}"
        )

    try:
        choice = int(input(f"{cl.red}Enter entry number to delete:{cl.reset} ").strip())
        if choice < 1 or choice > len(vault):
            print(f"{cl.red}Invalid selection.{cl.reset}")
            return
        confirm = input(f"{cl.red}Are you sure you want to delete entry {choice}? (Y/N):{cl.reset} ").strip().lower()
        if confirm != "y":
            print(f"{cl.cyan}Entry not deleted.{cl.reset}")
            return

        removed = vault.pop(choice - 1)
        save_vault(vault, key)
        print(f"{cl.cyan}[+] Deleted entry for site: {removed.get('site','N/A')}{cl.reset}")
    except ValueError:
        print(f"{cl.red}Please enter a valid number.{cl.reset}")


def search_entries(key):
    """Search for entries by site name"""
    print(f"{cl.cyan}\nSearch Password Entries{cl.reset}")
    query = input("Enter site to search: ").strip().lower()
    if not query:
        print(f"{cl.red}Search term cannot be empty.{cl.reset}")
        return

    vault = load_vault(key)
    if not vault:
        print(f"{cl.red}No entries found.{cl.reset}")
        return

    results = [(i, e) for i, e in enumerate(vault, start=1) if query in e.get("site","").lower()]

    if not results:
        print(f"{cl.red}No matching entries found.{cl.reset}")
        return

    print(f"{cl.green}Matches:{cl.reset}")
    for index, entry in results:
        print(
            f"{index}) Site:{entry.get('site','N/A')} | "
            f"Email:{entry.get('email','N/A')} | "
            f"Username:{entry.get('username','N/A')}"
        )

    print(f"{cl.green}Total matches: {len(results)}{cl.reset}")


def get_entry(key):
    """Get a single entry's password by site name"""
    print(f"{cl.cyan}\nGet Password Entry{cl.reset}")
    query = input("Enter site name: ").strip().lower()
    if not query:
        print(f"{cl.red}Site cannot be empty.{cl.reset}")
        return

    vault = load_vault(key)
    for entry in vault:
        if query == entry.get("site","").lower():
            print(f"{cl.green}Site:{cl.yellow} {entry.get('site','N/A')}")
            print(f"{cl.green}Email:{cl.yellow} {entry.get('email','N/A')}")
            print(f"{cl.green}Username:{cl.yellow} {entry.get('username','N/A')}")
            print(f"{cl.green}Password:{cl.yellow} {entry.get('psd','N/A')}{cl.reset}")
            return

    print(f"{cl.red}No entry found for site '{query}'.{cl.reset}")




def copy_password(key):
    """Copy password to clipboard"""
    try:
        import pyperclip
    except ImportError:
        print(f"{cl.red}[!] Install pyperclip: pip install pyperclip{cl.reset}")
        return
    
    site = input("Enter site name: ").strip().lower()
    vault = load_vault(key)
    
    for entry in vault:
        if site == entry.get("site", "").lower():
            pyperclip.copy(entry.get("psd", ""))
            print(f"{cl.green}[+] Password for '{site}' copied to clipboard{cl.reset}")
            return
    
    print(f"{cl.red}[!] No entry found for '{site}'{cl.reset}")



def edit_entry(key):
    """Edit an existing entry"""
    vault = load_vault(key)
    
    if not vault:
        print(f"{cl.red}No entries found.{cl.reset}")
        return
    
    # List entries with numbers
    for i, entry in enumerate(vault, 1):
        print(f"{i}) {entry.get('site', 'N/A')} - {entry.get('username', 'N/A')}")
    
    try:
        choice = int(input(f"{cl.cyan}Enter number to edit: {cl.reset}"))
        if choice < 1 or choice > len(vault):
            print(f"{cl.red}Invalid selection.{cl.reset}")
            return
        
        entry = vault[choice - 1]
        print(f"{cl.green}Leave blank to keep current value{cl.reset}")
        
        site = input(f"Site [{entry.get('site', '')}]: ").strip()
        email = input(f"Email [{entry.get('email', '')}]: ").strip()
        username = input(f"Username [{entry.get('username', '')}]: ").strip()
        option = input(f"Option [{entry.get('option', '')}]: ").strip()
        
        # Password handling - simple: Enter new password or press Enter to keep
        print(f"{cl.cyan}Password [{cl.yellow}press Enter to keep current{cl.cyan}]{cl.reset}")
        new_password = input("New password: ").strip()
        if new_password:
            entry['psd'] = new_password
        
        # Update only fields that were entered
        if site: entry['site'] = site
        if email: entry['email'] = email
        if username: entry['username'] = username
        if option: entry['option'] = option
        
        save_vault(vault, key)
        print(f"{cl.green}[+] Entry updated{cl.reset}")
        
    except ValueError:
        print(f"{cl.red}Invalid input.{cl.reset}")


def show_stats(key):
    """Show vault statistics"""
    vault = load_vault(key)
    
    if not vault:
        print(f"{cl.red}No entries found.{cl.reset}")
        return
    
    print(f"{cl.green}\n╔════════════════════════════════════════╗{cl.reset}")
    print(f"{cl.green}║         VAULT STATISTICS               ║{cl.reset}")
    print(f"{cl.green}╚════════════════════════════════════════╝{cl.reset}")
    
    # Basic counts
    total = len(vault)
    print(f"{cl.cyan}\n📊 Overview:{cl.reset}")
    print(f"  Total entries:     {cl.yellow}{total}{cl.reset}")
    
    # Unique sites (in case of duplicates)
    unique_sites = len(set(entry.get('site', '').lower() for entry in vault))
    if unique_sites < total:
        print(f"  Unique sites:      {cl.yellow}{unique_sites}{cl.reset}")
        print(f"  Duplicates:        {cl.yellow}{total - unique_sites}{cl.reset}")
    
    # Password strength analysis
    weak = 0
    medium = 0
    strong = 0
    no_password = 0
    
    for entry in vault:
        psd = entry.get('psd', '')
        if not psd:
            no_password += 1
        elif len(psd) < 8:
            weak += 1
        elif len(psd) < 12:
            medium += 1
        else:
            # Check for complexity
            has_upper = any(c.isupper() for c in psd)
            has_lower = any(c.islower() for c in psd)
            has_digit = any(c.isdigit() for c in psd)
            has_symbol = any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in psd)
            complexity = sum([has_upper, has_lower, has_digit, has_symbol])
            
            if len(psd) >= 16 and complexity >= 3:
                strong += 1
            elif len(psd) >= 12 and complexity >= 2:
                medium += 1
            else:
                weak += 1
    
    print(f"{cl.cyan}\n🔐 Password Strength:{cl.reset}")
    print(f"  Strong (12+ chars, complex):  {cl.green}{strong}{cl.reset}")
    print(f"  Medium (8-11 chars):          {cl.yellow}{medium}{cl.reset}")
    print(f"  Weak (<8 chars):              {cl.red}{weak}{cl.reset}")
    if no_password > 0:
        print(f"  Missing password:             {cl.red}{no_password}{cl.reset}")
    
    # Categories/Tags (if you have option field as category)
    categories = {}
    for entry in vault:
        cat = entry.get('option', 'Uncategorized')
        if cat:
            categories[cat] = categories.get(cat, 0) + 1
    
    if categories:
        print(f"{cl.cyan}\n📁 By Category:{cl.reset}")
        for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat}: {cl.yellow}{count}{cl.reset}")
    
    # Recently added (last 5)
    print(f"{cl.cyan}\n🕐 Recently Added (last 5):{cl.reset}")
    # Note: This requires a 'created_at' field in entries
    # If you don't have timestamps, just show first/last 5
    recent = vault[-5:] if len(vault) >= 5 else vault
    for entry in reversed(recent):
        print(f"  • {entry.get('site', 'N/A')} ({entry.get('username', 'N/A')})")
    
    # Summary line
    print(f"{cl.green}\n┌────────────────────────────────────────┐{cl.reset}")
    print(f"{cl.green}│{cl.reset}  {cl.yellow}Total passwords stored: {total}{cl.reset}                      {cl.green}│{cl.reset}")
    print(f"{cl.green}└────────────────────────────────────────┘{cl.reset}\n")



def update_master_password(key):
    """Change the master password and re-encrypt the vault"""
    import sys
    from functions.core import SALT_FILE, PM_DIR
    from functions.encr import generate_salt, derive_key, encrypt_data
    
    print(f"{cl.cyan}\n🔐 Change Master Password{cl.reset}")
    print("----------------------------")
    
    # Verify current password
    current = getpass("Enter current master password: ").strip()
    
    # Load current salt
    with open(SALT_FILE, "rb") as f:
        salt = f.read()
    
    # Verify current password works
    try:
        test_key = derive_key(current, salt)
        # Test decrypt
        vault = load_vault(test_key)
        if vault is None:
            print(f"{cl.red}[!] Wrong master password{cl.reset}")
            return
    except Exception as e:
        print(f"{cl.red}[!] Wrong master password{cl.reset}")
        return
    
    # Get new password
    print(f"\n{cl.cyan}Enter new master password:{cl.reset}")
    new_password = getpass("New password: ").strip()
    confirm_password = getpass("Confirm new password: ").strip()
    
    if new_password != confirm_password:
        print(f"{cl.red}[!] Passwords do not match{cl.reset}")
        return
    
    if len(new_password) < 6:
        print(f"{cl.red}[!] Password must be at least 6 characters{cl.reset}")
        return
    
    if new_password == current:
        print(f"{cl.red}[!] New password must be different from current{cl.reset}")
        return
    
    # Generate new salt
    new_salt = generate_salt()
    
    # Derive new key
    new_key = derive_key(new_password, new_salt)
    
    # Re-encrypt vault with new key
    vault = load_vault(key)  # Load with current key
    encrypted_vault = encrypt_data(vault, new_key)
    
    # Save new salt
    with open(SALT_FILE, "wb") as f:
        f.write(new_salt)
    
    # Save re-encrypted vault
    from functions.core import VAULT_FILE
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted_vault)
    
    print(f"{cl.green}\n[+] Master password changed successfully{cl.reset}")
    print(f"{cl.yellow}[!] Remember your new password. Old password no longer works.{cl.reset}")
