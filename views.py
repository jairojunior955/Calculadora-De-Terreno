from flask import Blueprint, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from packages.Database.database import Query as query
views = Blueprint('views', __name__)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('username', validators=[InputRequired(), Length(min=8, max=80)])


@views.route('/Index',methods=['POST'])
def index():
    return render_template('Index.html')


@views.route('/Cadastro')
def cadastro():
    return render_template('Cadastro.html')


@views.route('/Login', methods=['POST', 'GET'])
def login():
    return render_template('Login.html')


@views.route('/validate', methods=["POST"])
def validate():
    login = request.form['login']
    password = request.form['password']

    if query().auth_user(f'{login}',f'{password}'):
        return render_template('Index.html')
    else:
        return '<h1>Não logamos</h1>'
