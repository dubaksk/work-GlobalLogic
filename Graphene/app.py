from flask import Flask, render_template, request, session, abort
from models import *

app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': 'sid',
    'db': 'erp',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
engine = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def main():
    return 'Hello World !'

if __name__ == '__main__':
    app.run()