from . import colors as cl

def show_help():
    """Display help menu with available commands"""
    print(f"{cl.green}\n╔══════════════════════════════════════════════════════╗{cl.reset}")
    print(f"{cl.green}║           Terminal Password Manager - Help            ║{cl.reset}")
    print(f"{cl.green}╚══════════════════════════════════════════════════════╝{cl.reset}")
    
    print(f"{cl.cyan}\n📋 BASIC COMMANDS:{cl.reset}")
    print(f"{cl.green}  add / a{cl.reset}                    Add a new password entry")
    print(f"{cl.green}  get / g{cl.reset}                    Get password for a specific site")
    print(f"{cl.green}  list / l{cl.reset}                   List all stored password entries")
    print(f"{cl.green}  search / s{cl.reset}                 Search entries by site name")
    print(f"{cl.green}  delete / del / d{cl.reset}           Delete a password entry")
    print(f"{cl.green}  edit / e{cl.reset}                   Edit an existing entry")
    
    print(f"{cl.cyan}\n🔧 UTILITY COMMANDS:{cl.reset}")
    print(f"{cl.green}  copy / c{cl.reset}                   Copy password to clipboard (hidden)")
    print(f"{cl.green}  stats / st{cl.reset}                 Show vault statistics")
    print(f"{cl.green}  clear / logout{cl.reset}             clear cached master password")
    #print(f"{cl.green}  export / exp{cl.reset}               Export vault to JSON/CSV")
    #print(f"{cl.green}  import / imp{cl.reset}               Import from JSON/CSV backup")
    #print(f"{cl.green}  categories / cat{cl.reset}           Manage password categories")
    #print(f"{cl.green}  strength / str{cl.reset}             Check password strength")
    #print(f"{cl.green}  favorites / fav{cl.reset}            Show favorite entries")
    
    print(f"{cl.cyan}\nℹ️  GENERAL:{cl.reset}")
    print(f"{cl.green}  help / h{cl.reset}                   Show this help menu")
   #print(f"{cl.green}  version / v{cl.reset}                Show version info")
   #print(f"{cl.green}  backup / b{cl.reset}                 Create encrypted backup")
    print(f"{cl.green}  passwd / mp{cl.reset}                Change master password")
    
    print(f"{cl.green}\n┌──────────────────────────────────────────────────────┐{cl.reset}")
    print(f"{cl.green}│{cl.reset}  {cl.yellow}Usage examples:{cl.reset}                                          {cl.green}│{cl.reset}")
    print(f"{cl.green}│{cl.reset}                                                    {cl.green}│{cl.reset}")
    print(f"{cl.green}│{cl.reset}    python3 main.py add                            {cl.green}│{cl.reset}")
    print(f"{cl.green}│{cl.reset}    python3 main.py get gmail                      {cl.green}│{cl.reset}")
    print(f"{cl.green}│{cl.reset}    python3 main.py list                           {cl.green}│{cl.reset}")
    print(f"{cl.green}│{cl.reset}    python3 main.py edit                           {cl.green}│{cl.reset}")
    print(f"{cl.green}│{cl.reset}    python3 main.py copy github                    {cl.green}│{cl.reset}")
    print(f"{cl.green}│{cl.reset}    python3 main.py stats                          {cl.green}│{cl.reset}")
    print(f"{cl.green}└──────────────────────────────────────────────────────┘{cl.reset}")
    
    print(f"{cl.cyan}\n💡 TIPS:{cl.reset}")
    print(f"  • Use {cl.green}copy{cl.reset} instead of {cl.green}get{cl.reset} to avoid showing password on screen")
    print(f"  • Run {cl.green}backup{cl.reset} weekly to keep your vault safe")
    print(f"  • Use {cl.green}categories{cl.reset} to organize work/personal passwords")
    print(f"  • Check {cl.green}strength{cl.reset} periodically for weak passwords\n")
