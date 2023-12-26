from models.__init__ import CONN, CURSOR

class Library:
    all = {}

    def __init__(self, name):
        self.id = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name.title()
        else:
            raise ValueError('name must be of type string and more than 1 character')
    
    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS libraries(
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(self):
        sql = """
            DROP TABLE IF EXISTS libraries
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name):
        library = cls(name)
        library.save()
        return library
    
    @classmethod
    def instance_from_db(cls, row):
        library = cls.all.get(row[0])

        if library:
          library.name = row[1]
        else: 
            library = cls(row[1])
            library.id = row[0]
            cls.all[library.id] = library
        return library
            
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM libraries
        """
        rows = CURSOR.execute(sql).fetchall()
        CONN.commit()
        
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM libraries 
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        new_name = name.capitalize()
        sql ="""
            SELECT * FROM libraries
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (new_name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def save(self):
        sql = """
            INSERT INTO libraries (name) VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE libraries
            SET name = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM libraries 
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id] 
        self.id = None

    def books(self):
        from models.Book import Book
        sql = """
            SELECT * FROM books
            WHERE library_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        
        return [Book.instance_from_db(row) for row in rows]