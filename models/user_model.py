from database.db import db

class User(db.Model):
    __tablename__ = 'users'


    id = db.Column('id', db.String(36), primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, _id, username, email, password):
        self.id = _id
        self.username = username
        self.email = email
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_user_by_id(cls, _id):
        if user_obj := cls.query.filter_by(id=_id).first():
            return cls.row_to_dict(user_obj)
        else:
            return []

    @classmethod
    def find_by_username(cls, username):
        if user_obj := cls.query.filter_by(username=username).first():
            return cls.row_to_dict(user_obj)
        else:
            return []

    @classmethod
    def get_all_users(cls):
        if users_obj := cls.query.all():
            return list(map(cls.row_to_dict, users_obj))
        else:
            return []

    @classmethod
    def update_password(cls):
        pass

    @staticmethod
    def row_to_dict(row):
        return {column.name: str(getattr(row, column.name)) for column in row.__table__.columns}