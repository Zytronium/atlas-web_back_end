#!/usr/bin/env python3
"""
Basic Auth class
"""
import base64

from api.v1.auth.auth import Auth


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
        pass
