from flask import Flask
from models import *
from flask_graphql import GraphQLView
from schema import schema
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


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


if __name__ == '__main__':
    app.run(debug=True)
