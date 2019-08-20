from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String, Column
from sqlalchemy.orm import backref, relationship

db = SQLAlchemy()

class ModelStudent(db.Model):
    __tablename__ = 'student'

    admno = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(80))
    Name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    teacher_id = db.Column(db.Integer, ForeignKey('teacher.id'))

    # def __init__(self, admno, section, Name, password, id):
    #     self.admno = admno
    #     self.section = section
    #     self.Name = Name
    #     self.password = password
    #     self.id = id


class ModelTeacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    studentlist = relationship(ModelStudent, backref='teacher')

    # def __init__(self, id,name,password):
    #     self.id = id
    #     self.name = name
    #     self.password = password
