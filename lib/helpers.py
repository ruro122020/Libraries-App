# lib/helpers.py
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from models.Book import Book
from models.Library import Library

console = Console()

def view_libraries():
    libraries_list = Library.get_all()
    table = Table(title="Libraries")
    table.add_column("", style="cyan")
    table.add_column("Name", justify="right", style="cyan", header_style="cyan")
    for i, library in enumerate(libraries_list):
        table.add_row(f"{i+1}", library.name)
    console.print(table)

def view_library_books():
    while True:
      library_name = Prompt.ask("Enter Library Name")
      library = Library.find_by_name(library_name)
      if library:
          table=Table(title="Books")
          table.add_column("")
          table.add_column("Title")
          table.add_column("Author")
          table.add_column("Published Year")
          books = library.books()
          for i, book in enumerate(books):
              table.add_row(f"{i+1}",str(book.title), str(book.author), str(book.published_year))
          console.print(table)
      else:
          console.print("invalid choice", style='red')

def search_book_by_location():
    table = Table()
    table.add_column("", style='bold magenta')
    table.add_column("Title")
    table.add_column("Author")
    table.add_column("Published Year")
    table.add_column("Library Locations")

    print('list of libraries that holds book')

def exit_program():
    print("Goodbye!")
    exit()