from repositories.read_list_repository import (
    read_list_repository as default_read_list_repository)

class ReadListService:
    def __init__(self, read_list_repository=default_read_list_repository):
        self._read_list_repository = read_list_repository
    
    def get_read_list(self, user_id):
        return self._read_list_repository.get_read_list(user_id)
    
    def add_to_read_list(self, user_id, book_id):
        return self._read_list_repository.add_to_read_list(user_id, book_id)

    def delete_from_read_list(self, user_id, book_id):
        return self._read_list_repository.delete_from_read_list(user_id, book_id)

read_list_service = ReadListService()