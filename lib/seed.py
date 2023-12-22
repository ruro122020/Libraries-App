from models.Book import Book
from models.Library import Library

def seed_database():
  Library.create_table()
  Library.drop_table()

  Book.create_table()
  Book.create_table()

  nooks = Library.create("Nooks")
  castle = Library.create("Castle")
  arch = Library.create("Arch")
  campbell = Library.create("Campbell")

  #Nooks Books
  Book.create("Remember Me", "Christopher Spike", 1980, nooks.id)
  Book.create("Dracula", "Spike Castle", 1930, nooks.id)
  Book.create("Lord of the Flies", "Harper Lee", 1980, nooks.id)
  #Castle Books
  Book.create("The Fall", "J. D. Salinger", 1980, castle.id)
  Book.create("The Rise", "William Golding", 1980, castle.id)
  #Arch Books
  Book.create("The Fall", "J. D. Salinger", 1980, arch.id)
  Book.create("Remember Me", "Christopher Spike", 1980, arch.id)
  #Campbell Books
  Book.create("Remember Me", "Christopher Spike", 1980, campbell.id)
  Book.create("Dracula", "Spike Castle", 1930, campbell.id)
 
seed_database()
print("data seeded")
