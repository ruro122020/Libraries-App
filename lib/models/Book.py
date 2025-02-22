from models.__init__ import CONN, CURSOR

class Book:

    all = {}

    def __init__(self, title, author, published_year, library_id):
        self.id = None
        self.title = title
        self.author = author
        self.published_year = published_year
        self.library_id = library_id

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) >= 3:
            self._title = title.title()
        else:
            raise ValueError('title must be of type string and more than 2 characters')
        
    @property
    def author(self):
        return self._author 
    @author.setter
    def author(self, author):
        if type(author) == str and len(author) >= 3:
            self._author = author.title()
        else:
            raise ValueError('author must be of type string and more than 2 characters')
    
    @property
    def published_year(self):
        return self._published_year 
    @published_year.setter
    def published_year(self, published_year):
        if type(published_year) == int and published_year >= 1000:
            self._published_year = published_year
        else: 
            raise ValueError("published_year must be of type int and greater than the year 1000")
        
    @property
    def library_id(self):
        return self._library_id
    @library_id.setter
    def library_id(self, library_id):
        if type(library_id) == int:
            self._library_id = library_id
        else:
            raise ValueError("library_id must be of type integer")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            published_year INTEGER,
            library_id INTEGER,
            FOREIGN KEY (library_id) REFERENCES libraries(id))
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """

            DROP TABLE IF EXISTS books
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, title, author, published_year, library_id):
        book = cls(title, author, published_year, library_id)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        
        if book:
            book.title = row[1]
            book.author = row[2]
            book.published_year = row[3]
            book.library_id = row[4]
        else:
            book = cls(row[1], row[2], row[3], row[4])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM books
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM books
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_title(cls, title):
        new_title = title.title()
        sql = """
            SELECT * FROM books
            WHERE title = ? 
        """
        row = CURSOR.execute(sql, (new_title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def save(self):
        sql ="""
            INSERT INTO books (title, author, published_year, library_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.author, self.published_year, self.library_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        sql = """
            DELETE FROM books 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    def library(self):
     from models.Library import Library
     
     sql = """
         SELECT * 
         FROM libraries
         WHERE id = ?
    """
    
     row = CURSOR.execute(sql, (self.library_id,)).fetchone()
     return Library.instance_from_db(row)

    