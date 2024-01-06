# lib/helpers.py
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from models.Book import Book
from models.Library import Library

console = Console()
##helper
def create_rows(table, rows):
  pass

def create_columns(table, columns):
  for column_name in columns:
   table.add_column(column_name)

def get_books_location(book_title):
    all_books = Book.get_all()
    books = []
    for book in all_books:
        if book.title == book_title.title():
            books.append(book)
    return books

def get_authors_books(author):
  authors_books = []
  for book in Book.get_all():
    if book.author == author.title():
      authors_books.append(book)
  return authors_books


def get_all_data():
  books = Book.get_all()
  data = []
  for book in books:
     library = Library.find_by_id(book.library_id)
     data.append({
        'library': library.name,
        'book_title': book.title,
        'book_author': book.author
     })
  return data
####
def view_libraries():
    libraries_list = Library.get_all()
    if libraries_list:
      table = Table(box=box.SIMPLE_HEAVY)
      create_columns(table, ["", "Library Name"])
      for i, library in enumerate(libraries_list):
        table.add_row(f"{i+1}", library.name)
      console.print(table)
    else:
      console.print("There are no libraries in the database", style='red')

def view_library_books():
    view_libraries()
    library_name = Prompt.ask("Enter Library Name")
    library = Library.find_by_name(library_name)
    if library:
        table=Table(box=box.SIMPLE_HEAVY)
        create_columns(table, ["", "Title", "Author", "Published Year"])
        books = library.books()
        for i, book in enumerate(books):
            table.add_row(f"{i+1}",str(book.title), str(book.author), str(book.published_year))
        console.print(table)
    else:
        console.print("Invalid Name", style='red')

def search_book_by_location():
    book_title = Prompt.ask("Enter Book Title")
    books = get_books_location(book_title)
    if books:
      table = Table(box=box.SIMPLE_HEAVY)
      create_columns(table, ["", "Title", "Author", "Published Year", "Library"])
      for i,book in enumerate(books):
        library = Library.find_by_id(book.library_id)
        table.add_row(f"{i+1}", str(book.title), str(book.author), str(book.published_year), str(library.name))
      console.print(table)
    else:
      console.print("Book Title Not Found", style="red")

    
def author_books():
  author = Prompt.ask("Enter Author's name")
  books = get_authors_books(author)
  if books:
    table = Table(title="Author's Book", box=box.SIMPLE_HEAVY)
    create_columns(table, ["", "Title", "Author", "Published Year", "Library"])
    for i, book in enumerate(books):
      library = Library.find_by_id(book.library_id)
      table.add_row(f"{i+1}", str(book.title), str(book.author), str(book.published_year), str(library.name))
    console.print(table)
  else:
    console.print("No Books By Author Found", style='red')


def view_all():
  data = get_all_data()
  if data:
    table = Table(box=box.SIMPLE_HEAVY)
    create_columns(table, ["", "Library Name", "Title", "Author"])
    for i, obj in enumerate(data):
      table.add_row(f"{i+1}", obj['library'], obj['book_title'], obj['book_author'])
    console.print(table)
  else: 
    console.print("Data Does Not Exists", style = 'red')

def exit_program():
    console.print("GOODBYE!", style="green")
    exit()