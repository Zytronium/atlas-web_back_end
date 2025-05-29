#!/usr/bin/env python3
"""
Flask App
"""

import flask
from flask import Flask, jsonify, request, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH._db.find_user_by(email=email)
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response, 200
    except Exception:
        pass

    flask.abort(401)
    return None


@app.route("/sessions", methods=["DELETE"])
def logout():
    session_id = request.cookies.get("session_id")
    try:
        user = AUTH._db.find_user_by(session_id=session_id)
        AUTH.destroy_session(user.id)
        return redirect("/")
    except Exception:
        flask.abort(403)
        return None


@app.route("/profile", methods=["GET"])
def profile():
    session_id = request.cookies.get("session_id")

    try:
        AUTH._db.find_user_by(session_id=session_id)
        return {"email": "<user email>"}, 200
    except Exception:
        flask.abort(403)
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
