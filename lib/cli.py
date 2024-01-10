# lib/cli.py
from rich.console import Console
from rich.table import Table

from helpers import (
  add_library,
  delete_library,
  find_library_by_name,
  view_libraries,
  view_library_books,
  add_book,
  delete_book,
  find_book_by_name,
  view_all_books,
  view_book_library,
  exit_program,
)

console = Console()

def create_rows(table, row_names):
    for i, name in enumerate(row_names):
        table.add_row(f"{i+1}", f"{name}")
    

def main():
    while True:
        menu()
        choice = input("What would you like to do? ")
        if choice == "1": 
          add_library()
        elif choice == "2":
          delete_library()
        elif choice == "3":
          find_library_by_name()
        elif choice == "4":
          view_libraries()
        elif choice == '5':
          view_library_books()
        elif choice == "6":
          add_book()
        elif choice == "7":
          delete_book()
        elif choice == "8":
          find_book_by_name()
        elif choice == "9":
          view_all_books()
        elif choice == "10":
          view_book_library()
        elif choice == "11":
          exit_program()
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
