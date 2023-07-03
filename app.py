from flask import Flask
from flask_restful import Api

from resources.user import AllUsers, Users, Login, ResetPassword

app = Flask(__name__)
api = Api(app)
app.config.from_object('config')

api.add_resource(AllUsers, "/allusers")

api.add_resource(Users, "/users")

api.add_resource(Login, "/login")

api.add_resource(ResetPassword, "/resetpassword")



if __name__ == "__main__":
    from database.db import db
    db.init_app(app)
    app.run(debug= False, port= 5000)