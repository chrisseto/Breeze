import datetime

import peewee as p

from breeze import App, Resource, Serializable


db = p.SqliteDatabase('users.db')


class UserModel(p.Model):
    username = p.CharField(unique=True)
    password = p.CharField()
    email = p.CharField()
    join_date = p.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class User(Serializable, Resource):
    email = Serializable.String()
    username = Serializable.String()
    join_date = Serializable.DateTime()

    @classmethod
    def from_model(cls, model):
        return cls.__init__(
            email=model.email,
            username=model.username,
            join_date=model.join_date
        )

    @classmethod
    def list(cls, filter_options):
        return [
            cls.from_model(u) for u in
            UserModel.select().paginate(
                filter_options.page + 1,
                filter_options.size
            )
        ]

db.connect()
app = App(User, prefix='/api/v1/', debug=True)

if __name__ == '__main__':
    app.serve()
