# lib/helpers.py
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from models.Book import Book
from models.Library import Library

console = Console()
##helpers
def create_columns(table, columns):
  for column_name in columns:
   table.add_column(column_name)

####
   
#create library
def add_library():
  while True:
    name = Prompt.ask("Library Name")
    library_name = Library.find_by_name(name)
   
    if not library_name:
      Library.create(name)
      console.print(f"{name} library has been created!", style="green")
      break
    else:
      console.print(f"Oops! {name} library already exist", style="red")
      console.print(f"Please try again", style="red")
#delete library
def delete_library():
  while True:
    view_libraries()
    name = Prompt.ask("Which library would you like to delete?")
    library_name = Library.find_by_name(name)
    print(library_name)
    if library_name:
      library_books = library_name.books()
      for book in library_books:
        book.delete()
      library_name.delete()
      console.print(f"{library_name.name} library has been deleted!", style='red')
    else:
      console.print(f"{name} does not exist", style="red")
      pass


  pass
#find library by name(attribute)
def find_library_by_name():
  pass
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

##create book
def add_book():
  pass
#delete book
def delete_book():
  pass
#find book by name(attribute)
def find_book_by_name():
  pass
#display all the objects(books) 
def view_all_books():
  pass
#view related objects(the library that book is in)
def view_book_library():
  pass


def exit_program():
    console.print("GOODBYE!", style="green")
    exit()