from repositories.author_repository import (
    author_repository as default_author_repository)


class AuthorService:
    def __init__(self, author_repository=default_author_repository):
        self._author_repository = author_repository

    def create_author(self, first_name, last_name):
        self._author_repository.create_author(first_name, last_name)


author_service = AuthorService()
