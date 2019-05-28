from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from models import *
import os
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

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
        if obj is not None:
            return render_template('options.html')
        else:
            return render_template("login_teacher.html")
    else:
        return render_template('login_teacher.html')


@app.route('/loginstudent', methods=['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        u_name = request.form.get('admno')
        u_pwd = request.form.get('password')
        log = Student.query.filter(Student.admno == u_name, Student.password == u_pwd).first()
        if log is not None:
            return 'login'
        else:
            return render_template("login_student.html")


    else:
        return render_template('login_student.html')


@app.route("/add",methods=['GET', 'POST'])
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

    # else:
    #     return render_template('login_teacher.html')

# @app.route("/viewmarks",methods=['GET','POST'])
# def viewmarks():
#     if request.method == 'POST':
#         admno = Marks.admno
#         abc = db.session.query(Marks).filter_by(Marks.admno == admno).all()
#         if abc is not None:
#             render_template('marksview.html', abc=abc)
#         else:
#             return 'wrong details.'





@app.route("/delete", methods=['GET', 'POST'])
def delete():
    # import pdb
    # pdb.set_trace()
    admno = request.form.get('admno')
    marks = request.form.get('marks')
    id = request.form.get('id')
    #queryrm = Marks(admno,marks,id)
    queryrm = Marks.query.filter_by(admno=admno, marks=marks, id=id).first()
    db.session.delete(queryrm)
    db.session.commit()
    return 'record removed'

@app.route("/addoption")
def addoption():

    return render_template('markscrud.html')

@app.route("/deleteoption")
def deleteoption():
    return render_template('marksdelete.html')


if __name__ == '__main__':
    app.run(debug=True)
