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
        Returns False if path is in excluded paths, else, True.
        Ensures slash tolerant paths.
        :param path: path for something I guess
        :param excluded_paths: paths to exclude I guess
        :return: False if path is in excluded_paths, else, True
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        for excl_pth in excluded_paths:
            excl_pth_norm = excl_pth if excl_pth.endswith(
                '/') else excl_pth + '/'
            if normalized_path == excl_pth_norm:
                return False
        return True

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
