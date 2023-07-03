import uuid
import datetime
import jwt

from flask.globals import request
from flask.wrappers import Response
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash

import config
from models.user_model import User
from utils import authentication
from utils import response_formatter as responses


class Users(Resource):
    def post(self):
        data = request.get_json()
        hashed_password = generate_password_hash(data["password"], method="sha256")

        new_user = User(_id = str(uuid.uuid4()), username = data["username"], email = data.pop("email", None), password = hashed_password)
        new_user.save_to_db()
        created_user = User.find_user_by_id(new_user.id)

        return responses.created(msg="User created successfully.", data=created_user)        


    def get(self):
        return  {"statusCode": 200, "message": "Operation Successful"}



class Login(Resource):
    def post(self):
        data = request.get_json()
        
        user = User.find_by_username(data["username"])
        if not user:
            return responses.not_found("Unsuccessful Login. Invalid credentials."),  404

        if check_password_hash(user["password"], data["password"]):
            token = jwt.encode({"user_id": user["id"], 'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=60)}, config.SECRET_KEY, algorithm="HS256")
            session_data =  {"TokenType": "Access-Token", "AccessToken": token}

            return responses.accepted(msg="Login Successful" ,data=session_data), 202

        return responses.failure(msg="Unsuccessful Login. Check Credentials"), 400

    
class ResetPassword(Resource):
    def post(self):
        data = request.get_json()

        new_hashed_password = generate_password_hash(data["password"], method="sha256")
        _ = User.update_password(data["email"], new_hashed_password)

        return responses.success(msg="Password reset successful"), 200



class AllUsers(Resource):
    @authentication.auth_required
    def get(self):
        if all_users := User.get_all_users():
            return responses.success(data=all_users), 200
        else:
            return responses.no_content("No Users Available"), 204

