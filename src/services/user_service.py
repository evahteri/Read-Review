from flask import session

from repositories.user_repository import (user_repository as default_user_repository)

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
    
    def _check_password_validity(self, password):
        special_characters = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
                              ":", ";", "<", "=", ">", "?", "@", "[", "]",
                              "^", "_", "`", "{", "|", "}", "~", "."]
        valid = True
        if len(password) < 8:
            valid = False
        if not any(i.isupper() for i in password):
            valid = False
        if not any(i.isdigit() for i in password):
            valid = False
        if not any(i.islower() for i in password):
            valid = False
        if not any(i in special_characters for i in password):
            valid = False
        return valid
    
    def _check_user_does_not_exist(self, username):
        if self._user_repository.search_user(username):
            return False
        return True

    
    def create_user(self, username, password, role):
        if self._check_user_does_not_exist(username):
            if self._check_password_validity(password):
                self._user_repository.create_user(username, password, role)
                print("User created")
        else:
            print("problem")
            return False

user_service = UserService()