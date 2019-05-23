from flask_sqlalchemy import SQLAlchemy

# import datetime

db = SQLAlchemy()


# class BaseModel(db.Model):
#     """Base data model for all objects"""
#     __abstract__ = True
#
#     def __init__(self, *args):
#         super().__init__(*args)
#
#     def __repr__(self):
#         """Define a base way to print models"""
#         return '%s(%s)' % (self.__class__.__name__, {
#             column: value
#             for column, value in self._to_dict().items()
#         })

    # def json(self):
    #     """
    #             Define a base way to jsonify models, dealing with datetime objects
    #     """
    #     return {
    #         column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
    #         for column, value in self._to_dict().items()
    #     }


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    ecode = db.Column(db.String(80))
    Name = db.Column(db.String(80))

    # def __init__(self, id, ecode, Name):
    #     self.id = id
    #     self.ecode = ecode
    #     self.Name = Name

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Student(db.Model):
    """Model for the stations table"""
    __tablename__ = 'student'

    admno = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(80))
    Name = db.Column(db.String(80))
