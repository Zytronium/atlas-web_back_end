#!/usr/bin/env python3
"""
Basic Auth class
"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
    Basic Auth class
    """
    def __init__(self):
        pass

    #  Or, if this were C, extrbauthead(), or even xb64ah()
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header for a Basic
        Authentication request
        :param authorization_header: The Authorization header
        :return: The Base64 part of the Authorization header
        """
        return (None if (authorization_header is None
                         or type(authorization_header) is not str
                         or not authorization_header.startswith('Basic '))
                else authorization_header.replace('Basic ', ''))

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decodes a Base64-encoded Authorization header
        :param base64_authorization_header: Te Base64 encoded header string
        :return: THe decoded UTF-8 string, or None if invalid
        """
        b64authead_is_valid = True
        decoded_bytes = None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header,
                                             validate=True)
        except (base64.binascii.Error, UnicodeDecodeError, TypeError):
            b64authead_is_valid = False
        return (None if (base64_authorization_header is None
                         or type(base64_authorization_header) is not str
                         or not b64authead_is_valid)
                else decoded_bytes.decode('utf-8'))

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str) -> (
            str, str):
        """
        Extracts user email and password from the Base64 decoded string
        :param decoded_base64_authorization_header: Decoded Bas64 string
        :return: A tuple of user_email, user_password or None, None
        """
        return (
            (None, None) if (decoded_base64_authorization_header is None or
                             type(decoded_base64_authorization_header) is not
                             str  # I hate the 80-char hard limit we're given
                             or ':' not in decoded_base64_authorization_header)
            else decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on the user's email and password
        :param user_email: The user's email
        :param user_pwd: The user's password
        :return: User instance if creds are valid, else None
        """
        try:
            users = User.search({'email': user_email})
        except Exception:
            users = None

        return (None if (user_email is None
                         or type(user_email) is not str
                         or user_pwd is None
                         or type(user_pwd) is not str
                         or not users
                         or not any(user.is_valid_password(user_pwd)
                                    for user in users))
                else next(user for user in users
                          if user.is_valid_password(user_pwd)))
