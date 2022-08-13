from db import (db as default_db)

class ReadListRepository:
    def __init__(self, db=default_db):
        self._db = db
    
    def get_read_list(self, user_id):
        values = {"user_id": user_id}
        sql = """SELECT B.id, A.first_name, A.last_name, B.title FROM authors A, books B 
        LEFT JOIN read_lists R ON B.id = R.book_id 
        WHERE B.author_id = A.id
        AND R.user_id =:user_id"""
        return self._db.session.execute(sql, values).fetchall()
    
    def add_to_read_list(self, user_id, book_id):
        values = {"user_id":user_id, "book_id":book_id}
        sql = """INSERT INTO read_lists (user_id, book_id)
        VALUES (:user_id, :book_id)"""
        self._db.session.execute(sql, values)
        self._db.session.commit()
        return True

read_list_repository = ReadListRepository()