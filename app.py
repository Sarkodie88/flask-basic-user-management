from flask import Flask, jsonify
from flask_restful import Api
from database.db import db
from resources.user import AllUsers, Users, Login, ResetPassword


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    from database.db import db
    db.init_app(app)

    return app

app = create_app()
api = Api(app)

# user endpoints
api.add_resource(AllUsers, "/allusers")

api.add_resource(Users, "/users")

api.add_resource(Login, "/login")

api.add_resource(ResetPassword, "/resetpassword")



@app.before_first_request
def create_tables():
    db.create_all()
    db.session.commit()
    print("first request")


if __name__ == "__main__":
    app.run(debug= True, port= 6000)







# from flask import Flask
# from flask_restful import Api

# from resources.user import AllUsers, Users, Login, ResetPassword

# app = Flask(__name__)
# api = Api(app)
# app.config.from_object('config')

# api.add_resource(AllUsers, "/allusers")

# api.add_resource(Users, "/users")

# api.add_resource(Login, "/login")

# api.add_resource(ResetPassword, "/resetpassword")



# if __name__ == "__main__":
#     from database.db import db
#     db.init_app(app)
#     app.run(debug= False, port= 5000)