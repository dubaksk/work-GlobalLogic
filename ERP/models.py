from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



db = SQLAlchemy()

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))



class Student(db.Model):
    __tablename__ = 'student'

    admno = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(80))
    Name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    authenticated = db.Column(db.Boolean, default=False)
    id = db.Column(db.Integer, ForeignKey('teacher.id'))

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.admno

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Marks(db.Model):
    __tablename__ = 'marks'
    no = db.Column(db.Integer, primary_key=True,autoincrement=True)
    admno = db.Column(db.Integer, ForeignKey('student.admno'))
    marks = db.Column(db.Integer)
    id = db.Column(db.Integer, ForeignKey('teacher.id'))

    def __init__(self, admno,marks,id):
        self.admno = admno
        self.marks = marks
        self.id = id