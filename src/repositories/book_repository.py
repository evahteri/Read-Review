from db import (db as default_db)


class BookRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_book(self, author_id, title):
        values = {"author_id": author_id, "title": title}
        sql = """INSERT INTO books (author_id, title)
        VALUES (:author_id, :title)"""
        self._db.session.execute(sql, values)
        self._db.session.commit()

    def search_books(self, query):
        sql = """SELECT A.first_name, A.last_name, B.id, B.title
        FROM books B LEFT JOIN authors A 
        ON B.author_id = A.id 
        WHERE LOWER(B.title) LIKE :query
        OR LOWER(A.first_name) LIKE :query
        OR LOWER(A.last_name) LIKE :query
        LIMIT 30"""
        result = self._db.session.execute(
            sql, {"query": "%"+query.lower()+"%"})
        books = result.fetchall()
        return books

    def get_book_by_id(self, book_id):
        values = {"book_id": book_id}
        sql = """SELECT B.author_id, B.title, A.first_name, A.last_name
        FROM books B, authors A
        WHERE B.author_id = A.id
        AND B.id = :book_id"""
        return self._db.session.execute(sql, values).fetchone()

    def delete_book(self, book_id):
        values = {"book_id": book_id}
        sql = """DELETE FROM books
        WHERE id =:book_id"""
        if self._db.session.execute(sql, values):
            self._db.session.commit()
            return True
        return False

    def book_exists(self, author_first_name, author_last_name, title):
        values = {"author_first_name": author_first_name, "author_last_name": author_last_name,
                  "title": title}
        sql = """SELECT A.first_name, A.last_name, A.id, B.title, B.author_id
        FROM authors A, books B
        WHERE A.id = B.author_id
        AND A.first_name=:author_first_name AND A.last_name=:author_last_name
        AND B.title=:title"""
        return self._db.session.execute(sql, values).fetchone()


book_repository = BookRepository()
