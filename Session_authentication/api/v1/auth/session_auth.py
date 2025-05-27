#!/usr/bin/env python3
"""
Session Auth class
"""

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Session Auth class
    """
    user_id_by_session_id = {}

    def __init__(self):
        pass

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for the given user_id
        :param user_id: The User ID to create the session for
        :return: The session ID string if successful, else None
        """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id
