from repositories.review_repository import (
    review_repository as default_review_repository)
from repositories.user_repository import (
    user_repository as default_user_repository)


class ReviewService:
    def __init__(self, review_repository=default_review_repository,
                 user_repository=default_user_repository):
        self._review_repository = review_repository
        self._user_repository = user_repository

    def check_review_length(self, review):
        if len(review) < 2:
            return False
        if len(review) > 10000:
            return False
        return True

    def check_title_length(self, title):
        if len(title) < 2:
            return False
        if len(title) > 100:
            return False
        return True

    def check_rating(self, rating):
        if not rating:
            return False
        if rating < 0:
            return False
        if rating > 5:
            return False
        return True

    def create_review(self, title, review, rating, book_id):
        user_id = self._user_repository.get_user_id()
        self._review_repository.create_review(
            title, review, rating, book_id, user_id)
        return True

    def get_recent_reviews(self):
        return self._review_repository.get_recent_reviews()

    def get_review_by_id(self, review_id):
        return self._review_repository.get_review_by_id(review_id)

    def get_reviews(self, book_id):
        return self._review_repository.get_reviews(book_id)


review_service = ReviewService()
