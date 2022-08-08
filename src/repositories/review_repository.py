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

review_repository = ReviewRepository()