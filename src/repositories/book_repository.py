from db import (db as default_db)

class BookRepository:
    def __init__(self, db=default_db):
        self._db=db

    def create_book(self, author_id, title):
        values = {"author_id":author_id, "title":title}
        sql = """INSERT INTO books (author_id, title) 
        VALUES (:author_id, :title)"""
        self._db.session.execute(sql, values)
        self._db.session.commit()
    
    def get_all_books(self):
        sql = """SELECT * FROM books"""
        return self._db.session.execute(sql).fetchall()
    
book_repository = BookRepository()