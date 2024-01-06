# lib/cli.py
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from helpers import (
    view_libraries,
    view_library_books,
    search_book_by_location,
    author_books,
    view_all,
    exit_program,
)

console = Console()

def create_rows(table, row_names):
    for i, name in enumerate(row_names):
        table.add_row(f"{i+1}", f"{name}")
    

def main():
    while True:
        menu()
        choice = Prompt.ask("What would you like to do?")
        if choice == "1":
            view_libraries()
        elif choice == "2":
            view_library_books()
        elif choice == "3":
            search_book_by_location()
        elif choice == "4":
            author_books()
        elif choice == '5':
            view_all()
            pass
        elif choice == "6":
            exit_program()
        else:
            console.print("Invalid Choice", style='red')



def menu():
    table = Table()
    table.add_column("",style="purple")
    table.add_column("Main Menu", style="purple", header_style='purple')
    create_rows(table, ["View All Libraries", "View Books in Library", "Search Book Locations", "Get Books By Author", "View All", "Exit"])
    console.print(table)

if __name__ == "__main__":
    main()
