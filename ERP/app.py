from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from models import *
import os
from sqlalchemy.orm import sessionmaker
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
POSTGRES = {
    'user': 'postgres',
    'pw': 'sid',
    'db': 'book',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def teacherlogin():
    if request.method == 'POST':
        u_name = request.form.get('username')
        u_pwd = request.form.get('password')
        obj = Teacher.query.filter(Teacher.name == u_name, Teacher.password == u_pwd).first()
        all = Student.query.all()
        if obj is not None:
            return render_template('options.html',all=all)
        else:
            return render_template("login_teacher.html")
    else:
        return render_template('login_teacher.html')


@app.route("/viewteacher", methods=['POST','GET'])
def viewMarks():
    # import pdb
    # pdb.set_trace()
    # admno1 = Student.admno
    # admno2 = Marks.admno
    sadmno = db.session.query(Student.admno).all()
    student = db.session.query(Student.Name).all()
    admno = db.session.query(Marks.admno).all()
    marks = db.session.query(Marks.marks).all()
    if sadmno == admno:
        view = {'Name':student, 'Admission Number':admno, 'Marks':marks}
    # view = db.session.query(Student, Marks).filter_by(admno=admno2).all()
    # view = db.session.query(
    # return render_template('marksview.html',view=view)
    # for student, marks in db.session.query(Student, Marks).filter(Student.admno == Marks.admno).all():
    #     view = "Name: {} Admission Number: {} Marks: {}".format(student.Name, marks.admno, marks.marks)
        return render_template('marksview.html', view=view)


@app.route('/loginstudent', methods=['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        u_name = request.form.get('admno')
        u_pwd = request.form.get('password')
        log = Student.query.filter(Student.admno == u_name, Student.password == u_pwd).first()
        result = Marks.query.filter_by(admno=u_name).all()
        if log is not None:
            return render_template('MarksViewStudent.html',u_name=u_name,result=result)
        else:
            return render_template("login_student.html")
    else:
        return render_template('login_student.html')


@app.route("/add", methods=['GET', 'POST'])
def add():
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        admno = request.form.get('admno')
        marks = request.form.get('marks')
        id = request.form.get('id')
        query = Marks(admno, marks, id)
        db.session.add(query)
        db.session.commit()
    return 'record added'


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    # import pdb
    # pdb.set_trace()
    admno = Marks.admno
    marks = Marks.marks
        # admno = request.form['admno']
        # marks = request.form['marks']
    # id = request.form.get('id')
    queryrm = Marks.query.filter_by(admno=admno, marks=marks).first()
    db.session.delete(queryrm)
    db.session.commit()
    return 'record removed'


@app.route("/addoption")
def addoption():
    return render_template('markscrud.html')


# @app.route("/deleteoption")
# def deleteoption():
#     return render_template('marksdelete.html')


if __name__ == '__main__':
    app.run(debug=True)
