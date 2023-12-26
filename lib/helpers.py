# lib/helpers.py
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from models.Book import Book
from models.Library import Library

console = Console()
##helper
def get_books(book_title):
    all_books = Book.get_all()
    books = []
    for book in all_books:
        if book.title == book_title.title():
            books.append(book)
    return books
####
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
      view_libraries()
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
          break
      else:
          console.print("Invalid Name", style='red')

def search_book_by_location():
    book_title = Prompt.ask("Enter Book Title")
    books = get_books(book_title)
    if books:
      table = Table()
      table.add_column("")
      table.add_column("title")
      table.add_column("Author")
      table.add_column("Published Year")
      table.add_column("Library")

      for i,book in enumerate(books):
        library = Library.find_by_id(book.library_id)
        table.add_row(f"{i+1}", str(book.title), str(book.author), str(book.published_year), str(library.name))
      console.print(table)
    else:
      console.print("Book Title Not Found", style="red")

    

def exit_program():
    print("Goodbye!")
    exit()