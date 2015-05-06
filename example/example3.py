import peewee as p

from breeze import App, Model, Resource


db = p.SqliteDatabase('users.db')


class User(Model, Resource):
    email = Model.String()
    username = Model.String()
    join_date = Model.DateTime()

    class Meta:
        database = db

    # @classmethod
    # def list(cls, filter_options):
    #     return list(
    #         cls.select().paginate(
    #             filter_options.page + 1,
    #             filter_options.size
    #         )
    #     )

db.connect()
app = App(User, prefix='/api/v1/', debug=True)

if __name__ == '__main__':
    app.serve()
