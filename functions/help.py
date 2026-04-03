from . import colors as cl

def show_help():
    """Display help menu with available commands"""
    print(f"{cl.green}\nTerminal Password Manager - Help{cl.reset}")
    print(f"{cl.green}---------------------------------{cl.reset}")
    print(f"{cl.cyan}Commands:{cl.reset}")
    print(f"{cl.green}add / a{cl.reset}       - Add a new password entry")
    print(f"{cl.green}list / l{cl.reset}      - List all stored password entries")
    print(f"{cl.green}get / g{cl.reset}       - Get password for a specific site")
    print(f"{cl.green}delete / del / d{cl.reset} - Delete a password entry")
    print(f"{cl.green}search / s{cl.reset}    - Search entries by site name")
    print(f"{cl.green}help / h{cl.reset}      - Show this help menu")
    print(f"{cl.green}---------------------------------{cl.reset}")
    print(f"{cl.cyan}Usage example:{cl.reset} python main.py add")
