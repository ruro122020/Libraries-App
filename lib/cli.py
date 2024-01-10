# lib/cli.py
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from helpers import (
  add_library,
  delete_library,
  find_library_by_name,
  view_libraries,
  view_library_books,
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
          add_library()
          pass
        elif choice == "2":
          delete_library()
          pass
        elif choice == "3":
          find_library_by_name()
          pass
        elif choice == "4":
          view_libraries()
          pass
        elif choice == '5':
          view_library_books()
          pass
        elif choice == "6":
          pass
        elif choice == "7":
          pass
        elif choice == "8":
          pass
        elif choice == "9":
          pass
        elif choice == "10":
          pass
        elif choice == "11":
          pass
        else:
            console.print("Invalid Choice", style='red')



def menu():
    table = Table()
    table.add_column("",style="purple")
    table.add_column("Main Menu", style="purple", header_style='purple')
    create_rows(table, [
         "Add A Library",
         "Delete A Library",
         "Find A Library",
         "View All Libraries",
         "View All Book in Library",
         "Add A Book",
         "Delete A Book",
         "Find a Book",
         "View All Books",
         "View Book's Library Location",
         "Exit"
         ])
    console.print(table)

if __name__ == "__main__":
    main()
