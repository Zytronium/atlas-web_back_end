#!/usr/bin/env python3
"""
Auth class file
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        I honestly don't know what this is for; I just followed instructions
        to make it
        :param path: path for something I guess
        :param excluded_paths: paths to exclude I guess
        :return: False if path is in excluded_paths, else, True
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0 or path not in excluded_paths: return True
        else: return False

    def authorization_header(self, request=None) -> str:
        """
        I honestly don't know what this will be used for
        :param request: the Flask request object
        """
        return None  # Todo, I guess

    def current_user(self, request=None) -> TypeVar('User'):
        """
        I honestly don't know what this will be used for
        :param request: the Flask request object
        """
        return None  # Todo, I guess
