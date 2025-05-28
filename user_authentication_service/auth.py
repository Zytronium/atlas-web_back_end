#!/usr/bin/env python3

import bcrypt
from sqlalchemy.exc import NoResultFound

from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user with the database with a hashed password.
        """
        try:  # If this raises a NoResultFound error, user doesn't exist yet
            self._db.find_user_by(email=email)
            #  If above line doesn't raise NoResultFound, user already exists
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            #  User doesn't already exist, proceed with creating user
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if the user login is valid
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"),
                                   user.hashed_password)
        except Exception:
            return False


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the hashed password in bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """
    Generates a random UUID
    """
    pass
