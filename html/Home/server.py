
from random import randint
from time import strftime
from flask import Flask, render_template, flash, request, send_from_directory, $
from wtforms import Form, TextField, TextAreaField, validators, StringField, Su$
from jinja2 import FileSystemLoader, Environment
from flask_talisman import Talisman, ALLOW_FROM
from OpenSSL import SSL
import hashlib
from passlib.hash import sha256_crypt
import psycopg2
import psycopg2.extras

DEBUG = True
app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def user_verify(user:str,password:str):

           password_query = "select password from users.account where email = "$
           try:
               cursor.execute(password_query)
           except:  # lost cursor
               cursor = connect()

               cursor.execute(password_query)
def write_to_disk(email,pwd):
    data = open('file.log', 'a')
    timestamp = get_time()
    data.write('Time={}, Email={}, Password={}\n'.format(timestamp,email,pwd))
    data.close()
@app.route('/')
def default():
    loader = FileSystemLoader('static')
    env = Environment(loader=loader)
    template = env.get_template('front_page.html')
    login = env.get_template('log_in.html')
    register = env.get_template('register.html')
    js_url = url_for('static', filename='log_in.html')
    return (template.render(root_url='',login=login.render(),register=register.$
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = ReusableForm(request.form)

    #print(form.errors)
    if request.method == 'POST':
        user_id=request.form['email']
        password=request.form['pwd']
        if form.validate() and user_verify(user_id,password):
            write_to_disk(name, surname, email)
        elif form.validate():
            flash('Email or password is not correct')
        else:
            flash('All Fields are Required')
        loader = FileSystemLoader('SignedIn')
        env = Environment(loader=loader)
        template = env.get_template('main.html')
        return (template.render())

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = ReusableForm(request.form)

    # print(form.errors)
    if rpequest.method == 'POST':
        user_id = request.form['email']
        password = request.form['pwd']

def connect():
    # get credentials to log into database
    cred_file_name = 'server_info.csv'
    user, secret, host, dbname = get_credentials(cred_file_name)
    conn_string = "host=" + host + " dbname=" + dbname + " user=" + user + " password=" + sec$
    # connect
    try:
        conn = psycopg2.connect(conn_string)
        conn.set_session(readonly=True, autocommit=True)
        cursor = conn.cursor()
        return cursor
    except:
        print("I am unable to connect to the database.")


def get_credentials(filename):
    keys = loadfile(filename)
    db_userName = keys[0]
    db_passWord = keys[1]
    db_host = keys[2]
    db_name = keys[3]
    return db_userName, db_passWord, db_host, db_name


def loadfile(filename):
    with open(filename) as f:
        items = f.readline().strip().split(',')
        return items


if __name__ == "__main__":
    cursor = connect()
    app.run(ssl_context=('cert.pem', 'key.pem'))