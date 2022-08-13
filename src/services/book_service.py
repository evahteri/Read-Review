from repositories.book_repository import (
    book_repository as default_book_repository)
from repositories.author_repository import (
    author_repository as default_author_repository)


class BookService:
    def __init__(self, book_repository=default_book_repository,
                 author_repository=default_author_repository):
        self._book_repository = book_repository
        self._author_repository = author_repository

    def create_new_book(self, author_first_name, author_last_name, title):
        if self._author_repository.check_if_author_exists(author_first_name, author_last_name):
            id = self._author_repository.get_author_id(
                author_first_name, author_last_name)
            self._book_repository.create_book(id, title)
        else:
            self._author_repository.create_author(
                author_first_name, author_last_name)
            id = self._author_repository.get_author_id(
                author_first_name, author_last_name)
            self._book_repository.create_book(id, title)

    def search_books(self, query):
        return self._book_repository.search_books(query)

    def get_book_by_id(self, book_id):
        return self._book_repository.get_book_by_id(book_id)
    
    def delete_book(self, book_id):
        return self._book_repository.delete_book(book_id)


book_service = BookService()
