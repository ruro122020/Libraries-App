from models.Book import Book
from models.Library import Library

def seed_database():
  Library.drop_table()
  Library.create_table()

  Book.drop_table()
  Book.create_table()

  nooks = Library.create("Nooks")
  castle = Library.create("Castle")
  arch = Library.create("Arch")
  campbell = Library.create("Campbell")

  #Nooks Books
  Book.create("Dracula", "Spike Castle", 1930, nooks.id)
  Book.create("Space", "Harper Lee", 1980, nooks.id)
  Book.create("Lord of the Earth", "Jeff Martin", 1980, nooks.id)
  Book.create("Mass Hern", "William Locks", 1980, nooks.id)
  Book.create("Take and Take", "William Golding", 1980, nooks.id)

  #Castle Books
  Book.create("The Fall", "J. D. Salinger", 1980, castle.id)
  Book.create("The Rise", "William Green", 1980, castle.id)
  Book.create("The Spirits Of Christmas", "William Houseward", 1980, castle.id)
  Book.create("Flies Frisk", "Harper Chang", 1980, castle.id)
  Book.create("Give and Take", "Stephanie Lee", 1980, castle.id)
  Book.create("Remember Me", "Christopher Spike", 1980, castle.id)


  #Arch Books
  Book.create("Stalian", "Christian Pike", 1980, arch.id)
  Book.create("Original Stories", "Charles Kelly", 1980, arch.id)
  Book.create("Vampire School", "Austin Castle", 1930, arch.id),
  Book.create("Lord of the Flies", "Sarah Lee", 1980, arch.id)
  Book.create("Attack on Titans", "Sam Castle", 1930, arch.id)

  #Campbell Books
  Book.create("Taken", "Will Rogers", 1980, campbell.id)
  Book.create("Spiderman and Venom", "Ross William", 1930, campbell.id)
  Book.create("Spiderman", "Steven Spillburger", 1930, campbell.id)
  Book.create("Captain America", "Jason Sanchez", 1930, campbell.id)
  Book.create("Attack on Titans Part 2", "Helan Garcia", 1930, campbell.id)

seed_database()
print("data seeded")
