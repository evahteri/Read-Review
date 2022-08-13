from db import (db as default_db)

class ReviewRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_review(self, title, review, rating, book_id, user_id):
        values = {"book_id":book_id, "review": review, 
        "rating":rating, "title":title, "user_id":user_id}
        sql = """INSERT INTO reviews (
            book_id, review, title, rating, created_by_id)
        VALUES(:book_id, :review, :title, :rating, :user_id)"""
        self._db.session.execute(sql, values)
        self._db.session.commit()
    
    def get_recent_reviews(self):
        sql = """SELECT R.id, B.title AS book_title, R.review , R.title AS review_title, R.rating, U.username 
        FROM reviews R, users U, books B 
        WHERE R.created_by_id = U.id 
        AND R.book_id = B.id 
        ORDER BY R.created_at 
        DESC LIMIT 5
        """
        return self._db.session.execute(sql).fetchall()
    
    def get_review_by_id(self, review_id):
        values = {"review_id":review_id}
        sql = """SELECT R.id, B.title AS book_title, R.review , R.title AS review_title, R.rating, U.username 
        FROM reviews R, users U, books B 
        WHERE R.created_by_id = U.id 
        AND R.book_id = B.id
        AND R.id =:review_id
        """
        return self._db.session.execute(sql,values).fetchone()
    
    def get_reviews(self, book_id):
        values = {"book_id":book_id}
        sql= """SELECT  R.id, B.title AS book_title, R.review, R.title AS review_title, R.rating, 
        U.username, R.created_at
        FROM reviews R, users U, books B
        WHERE R.book_id = B.id
        AND R.created_by_id = U.id
        AND book_id =:book_id"""

        return self._db.session.execute(sql, values).fetchall()

review_repository = ReviewRepository()