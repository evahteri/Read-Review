from repositories.review_repository import (
    review_repository as default_review_repository)
from repositories.user_repository import (
    user_repository as default_user_repository)

class ReviewService:
    def __init__(self, review_repository=default_review_repository,
            user_repository=default_user_repository):
        self._review_repository = review_repository
        self._user_repository = user_repository
        
    def create_review(self, title, review, rating, book_id):
        user_id = self._user_repository.get_user_id()
        self._review_repository.create_review(title, review, rating, book_id, user_id)
        return True
    
    def get_recent_reviews(self):
        return self._review_repository.get_recent_reviews()
    
    def get_review_by_id(self, review_id):
        return self._review_repository.get_review_by_id(review_id)

review_service = ReviewService()
