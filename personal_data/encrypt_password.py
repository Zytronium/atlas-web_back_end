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
