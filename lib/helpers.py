# lib/helpers.py
from rich.console import Console
from rich.table import Table
from rich import box
from models.Book import Book
from models.Library import Library

console = Console()
##helpers
def create_columns(table, columns):
  for column_name in columns:
   table.add_column(column_name)

# def check_library_exist(library_name):

#     library_name = input("Enter library that book will belong to: ")
#   else:
#     return library
  
####
   
#create library
def add_library():
  while True:
    name = input("Library Name: ")
    library_name = Library.find_by_name(name)
    if not library_name:
      try:
        Library.create(name)
        console.print(f"{name} library has been added!", style="green")
        break
      except Exception as exc:
       console.print("Error creating library:", exc, style='red')
    else:
      console.print(f"Oops! {name} library already exist", style="red")
      console.print(f"Please try again", style="red")

#delete library
def delete_library():
    view_libraries()
    name = input("Which library would you like to delete? ")
    library_name = Library.find_by_name(name)
    print(library_name)
    if library_name:
      library_books = library_name.books()
      for book in library_books:
        book.delete()
      library_name.delete()
      console.print(f"{library_name.name} library and its books have been deleted!", style='green')
    else:
      console.print(f"{name} does not exist", style="red")

#find library by name(attribute)
def find_library_by_name():
  name = input('Library Name: ')
  library = Library.find_by_name(name)
  if library:
    table = Table(box=box.SIMPLE_HEAVY)
    create_columns(table,["", "Library Name"])
    table.add_row(library.name)
    console.print(table)
  else:
    console.print(f"Oops! {name} does not exist", style='red')
  
#display all the objects(library) 
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
#view related objects(all the books in the library)
def view_library_books():
    view_libraries()
    library_name = input("Enter Library Name: ")
    library = Library.find_by_name(library_name)
    if library:
        table=Table(box=box.SIMPLE_HEAVY)
        create_columns(table, ["", "Title", "Author", "Published Year"])
        books = library.books()
        for i, book in enumerate(books):
            table.add_row(f"{i+1}",str(book.title), str(book.author), str(book.published_year))
        console.print(table)
    else:
        console.print("Library does not exist", style='red')

##create book
def add_book():
  title = input("Enter Title: ")
  book_title = Book.find_by_title(title)
  if not book_title:
    while True:
      library_name = input("Enter library that book will belong to: ")
      library = Library.find_by_name(library_name)
      if not library:
        console.print("Oops! libarary does not exist", style = 'red')
        console.print("Please try again", style = 'red')
      else:
        try:
          author = input("Enter Author: ")
          published_year = input("Enter Published Year: ")
          Book.create(title, author, int(published_year), library.id)
          console.print(f"{title} has been added!", style="green")
        except Exception as exc:
          console.print("Error creating book: ", exc, style = 'red')
        break
  else:
    console.print(f"Oops! {title} already exist", style = 'red')

#delete book
def delete_book():
  title = input("What book would you like to delete? ")
  book_title = Book.find_by_title(title)
  if book_title:
    book_title.delete()
    console.print(f"{title} has been deleted!", style="green")
  else:
    console.print(f"{title} does not exist", style="red")

#find book by name(attribute)
def find_book_by_name():
  title = input('Book Title: ')
  book = Book.find_by_title(title)
  if book:
    table = Table(box=box.SIMPLE_HEAVY)
    create_columns(table,["", "Title", "Author", "Published Year" ])
    table.add_row("", str(book.title), str(book.author), str(book.published_year))
    console.print(table)
  else:
    console.print(f"Oops! {title} does not exist", style='red')

#display all the objects(books) 
def view_all_books(): 
  book_list = Book.get_all()
  if book_list:
    table = Table(box=box.SIMPLE_HEAVY)
    create_columns(table, ["", "Title", "Author", "Published Year"])
    for i, book in enumerate(book_list):
      table.add_row(f"{i+1}", str(book.title), str(book.author), str(book.published_year))
    console.print(table)
  else:
    console.print("There are no libraries in the database", style='red')

#view related objects(the library that book is in)
def view_book_library():
  title = input("Enter Book Title: ")
  book = Book.find_by_title(title)
  if book:
    library = book.library()
    table = Table(box=box.SIMPLE_HEAVY)
    create_columns(table, ["", "Book Title", "Library"])
    table.add_row("", str(book.title), str(library.name))
    console.print(table)
  else:
    console.print("Book does not exist", style='red')
  
def exit_program():
    console.print("GOODBYE!", style="green")
    exit()