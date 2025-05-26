#!/usr/bin/env python3
"""
Encrypt Password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a random salt using bcrypt
    :param password: password to hash
    :return: a hashed, encrypted password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if the hashed password is matches the password
    :param hashed_password: the hashed password
    :param password: the password
    :return: true if the hashed password is valid, false otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
