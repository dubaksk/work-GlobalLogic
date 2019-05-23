from flask import Flask
from models import db
from models import Teacher

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


@app.route("/")
def main():
    return 'Hello World !'

@app.route("/add",methods=['GET','POST'])
def add_teacher():
    #if request.args.get():
    # id = request.args.get('id')
    # ecode = request.args.get('ecode')
    # Name = request.args.get('Name')
    id = 11
    ecode = '1011'
    Name ="ABD!"
    new = Teacher(id=1002, ecode='EN', Name='Aditya')

    db.session.add(new)
    db.session.commit()

    return "New entry added"
    # if request.form:
    #     book = Book(title=request.form.get("title"))
    #     db.session.add(book)
    #     db.session.commit()


if __name__ == '__main__':

    app.run(debug=True)
