#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv

from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
try:
    import api.v1.views.app_views as app_views  # Sometimes only this works
except ModuleNotFoundError:
    from api.v1.views import app_views  # Other times only this works
try:
    import api.v1.auth.auth.Auth as Auth  # Sometimes only this works
except ModuleNotFoundError:
    from api.v1.auth.auth import Auth  # Other times only this works

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv('AUTH_TYPE')

if auth_type == "auth":
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(401)
def unauth(error) -> str:
    """ Unauthorized error handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ The Forbidden Error Handler that handles the "403: Forbidden" error
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.before_request
def before_request_auth():
    """
    Filter each request before it's handled
    """
    excl = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/',
            '/api/v1/auth_session/login/']
    if auth is None or not auth.require_auth(request.path, excl):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)

    if (auth.authorization_header(request) is None
        and auth.session_cookie(request) is None):
        abort(401)

    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
