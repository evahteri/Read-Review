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
    
    def search_books(self, query):
        sql = """SELECT A.first_name, A.last_name, B.title FROM books B, authors A WHERE B.author_id = A.id AND B.title LIKE :query"""
        result = self._db.session.execute(sql, {"query":"%"+query+"%"})
        books = result.fetchall()
        return books
    
book_repository = BookRepository()