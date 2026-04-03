from functions.core import load_vault, save_vault
from .psd_gen import generate_password  # your password generator function
from functions import colors as cl  

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
    """List all stored entries"""
    print(f"{cl.green}\nStored Password Entries{cl.reset}")
    vault = load_vault(key)

    if not vault:
        print(f"{cl.red}No entries found.{cl.reset}")
        return

    for i, entry in enumerate(vault, start=1):
        print(
            f"{cl.green}{i}) Site:{cl.yellow} {entry.get('site','N/A')} "
            f"{cl.green}- Email:{cl.yellow} {entry.get('email','N/A')} "
            f"{cl.green}- Username:{cl.yellow} {entry.get('username','N/A')} "
            f"{cl.green}- Option:{cl.yellow} {entry.get('option','N/A')}{cl.reset}"
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
