from flask import Flask
from werkzeug.security import check_password_hash, generate_password_hash
from db import (db as default_db)

class UserRepository:
    def __init__(self, db=default_db):
        self._db=db

    def search_user(self, username):
        values = {"username":username}
        sql = """SELECT username FROM users
        WHERE username=:username"""
        return bool(self._db.session.execute(sql,values).fetchall())

    def create_user(self, username, password, role):
        hash_value = generate_password_hash(password)
        values = {"username":username, "password":hash_value, "role":role}
        sql = """INSERT INTO users (username, password, role)
        VALUES (:username, :password, :role)"""
        self._db.session.execute(sql, values)
        self._db.session.commit()

    def _check_username_and_password(self,username, password):
        values = {"username":username}
        sql = """SELECT id, username, password, role FROM users WHERE username=:username"""
        user = self._db.session.execute(sql, values).fetchone()
        if not user:
            return False
        hash_password = user.password
        if check_password_hash(hash_password, password):
            return user
        return False

    def sign_in(self, username, password):
        return self._check_username_and_password(username, password)


user_repository = UserRepository()
