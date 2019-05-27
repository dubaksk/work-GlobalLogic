from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



db = SQLAlchemy()

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    # subcode = db.Column(db.String(80))
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))



class Student(db.Model):
    __tablename__ = 'student'

    admno = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(80))
    Name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    id = db.Column(db.Integer, ForeignKey('teacher.id'))


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