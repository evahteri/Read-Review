import secrets
from flask import session
from repositories.user_repository import (
    user_repository as default_user_repository)


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

    def _check_username_validity(self, username):
        if len(username) < 3:
            return False
        if len(username) > 50:
            return False
        return True

    def create_user(self, username, password, role):
        if not self._check_username_validity(username):
            if not self._user_repository.search_user(username):
                if self._check_password_validity(password):
                    self._user_repository.create_user(username, password, role)
                    return True
                return "invalid password"
            return "username exists"
        return "invalid username"

    def sign_in(self, username, password):
        user = self._user_repository.sign_in(username, password)
        if user:
            session["username"] = user.username
            session["role"] = user.role
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

    def get_role(self, username):
        return self._user_repository.get_role(username)
    
    def get_user_id(self):
        return self._user_repository.get_user_id()

user_service = UserService()
