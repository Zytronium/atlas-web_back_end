#!/usr/bin/env python3
"""
Auth class
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        I honestly don't know what this will be used for at the
        time of writing this
        :param path: path for something I guess
        :param excluded_paths: paths to exclude I guess
        :return:
        """
        return False  # Todo, I guess

    def authorization_header(self, request=None) -> str:
        """
        I honestly don't know what this will be used for
        :param request: the Flask request object
        :return:
        """
        return None  # Todo, I guess

    def current_user(self, request=None) -> TypeVar('User'):
        """
        I honestly don't know what this will be used for
        :param request: the Flask request object
        :return:
        """
        return None  # Todo, I guess
