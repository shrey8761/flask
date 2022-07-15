from flask import Flask, render_template
from blueprints import aboutme
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_url_path='/static',static_folder='static',template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite3'
db = SQLAlchemy(app)
@app.route('/')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(256), nullable=False) 

def index():
    context = {'title':'Something great','user':'shrey'}
    return render_template('index.html',context=context)

app.register_blueprint(aboutme.app)


app.run()