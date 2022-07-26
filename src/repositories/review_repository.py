from db import db

class ReviewRepository:
    def __init__(self, db):
        self._db = db

def create_review(self, book_id, review, rating, created_by_id, created_at):
    sql = f"""INSERT INTO reviews (
        book_id, 
        review, 
        rating, 
        created_by_id, 
        created_at)
    VALUES(
        {book_id},
        {review}, 
        {rating}, 
        {created_by_id}, 
        {created_at})"""
    