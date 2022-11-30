from flask import Blueprint, render_template

views = Blueprint('views', __name__)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('username', validators=[InputRequired(), Length(min=8, max=80)])


@views.route('/Index')
def index():
    return render_template('Index.html')


@views.route('/Cadastro')
def cadastro():
    return render_template('Cadastro.html')


@views.route('/Login', methods=["POST", "GET"])
def login():
    username = request.form['form-login']
    password = request.form['password-form']
    print(username, password)
    return render_template('Login.html')
