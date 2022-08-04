from db import (db as default_db)

class AuthorRepository:
    def __init__(self, db=default_db):
        self._db=db

    def check_if_author_exists(self, first_name, last_name):
        values = {"first_name":first_name, "last_name":last_name}
        sql = """SELECT first_name, last_name FROM authors
        WHERE first_name=:first_name AND last_name=:last_name"""
        return bool(self._db.session.execute(sql,values).fetchall())

    def get_author_id(self, first_name, last_name):
        values = {"first_name":first_name, "last_name":last_name}
        sql = """SELECT id FROM authors
        WHERE first_name=:first_name AND last_name=:last_name"""
        return self._db.session.execute(sql,values).fetchone()[0]

    def get_author_by_id(self, id):
        values = {"id":id}
        sql = """SELECT first_name, last_name FROM authors WHERE id=:id"""
        return self._db.session.execute(sql, values).fetchall()

    def create_author(self, first_name, last_name):
        if not self.check_if_author_exists(first_name, last_name):

            values = {"first_name":first_name, "last_name":last_name}
            sql = """INSERT INTO authors (first_name, last_name)
            VALUES (:first_name, :last_name)"""
            self._db.session.execute(sql, values)
            self._db.session.commit()
        else:
            print("Author already exists!")

author_repository = AuthorRepository()
