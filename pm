#!/usr/bin/env python3

import readline
import sys
from functions.core import ensure_storage
from functions.core import clear_session
from functions.pm_funcs import (
    add_entry,
    list_entries,
    delete_entry,
    search_entries,
    get_entry,
    edit_entry,      
    copy_password,   
    show_stats,
    update_master_password 

)
from functions import colors as cl
from functions.help import show_help 

def main():
    # Derive key and ensure storage
    key = ensure_storage()

    # Check command-line arguments
    if len(sys.argv) < 2:
        print(f"{cl.red}No command provided.{cl.reset}")
        show_help()
        return

    command = sys.argv[1].lower()

    if command in ("add", "a"):
        add_entry(key)

    elif command in ("list", "l"):
        list_entries(key)

    elif command in ("delete", "del", "d"):
        delete_entry(key)

    elif command in ("search", "s"):
        search_entries(key)

    elif command in ("get", "g"):
        get_entry(key)

    elif command in ("edit", "e"):
        edit_entry(key)

    elif command in ("copy", "c"):
        copy_password(key)

    elif command in ("stats", "st"):
        show_stats(key)


    elif command in ("help", "h"):
        show_help()

    elif command in ("passwd", "mp", "master"):
        update_master_password(key)

    elif command in ("logout", "clear"):
        clear_session()
        print(f"{cl.green}[+] Session cleared. You will be prompted for password next time.{cl.reset}")


    else:
        print(f"{cl.red}Unknown command: {command}{cl.reset}")
        show_help()


if __name__ == "__main__":
    main()
