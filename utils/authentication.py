from functools import wraps
from flask.globals import request
import jwt

import config
from models.user_model import User
from utils import response_formatter as responses


def auth_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]

        if not token:
            return responses.unauthorised(msg="Authentication token required."), 401

        try:
            decoded_info = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
            user_data = User.find_user_by_id(decoded_info["user_id"])
            print(user_data) 
        except jwt.ExpiredSignatureError as err:
            return responses.unauthorised(msg="Authentication Token Expired.."), 401
        except Exception as err:
            print(err)
            return responses.unauthorised(msg="Invalid token.."), 401

        return func(*args, **kwargs)
    return decorated