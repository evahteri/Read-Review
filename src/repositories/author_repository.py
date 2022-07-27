from db import (db as default_db)

class AuthorRepository:
    def __init__(self, db=default_db):
        self._db=db

    def create_author(self, first_name, last_name):
        values = {"first_name":first_name, "last_name":last_name}
        sql = """INSERT INTO authors (first_name, last_name) 
        VALUES (:first_name, :last_name)"""
        self._db.session.execute(sql, values)
        self._db.session.commit()

author_repository = AuthorRepository()