from flask import Blueprint, render_template, request, redirect, url_for, flash
from packages.Database.database import Query as query

views = Blueprint('views', __name__)
'''@views.route('/index', methods=['POST'])
def index():
    return render_template('Index.html')'''


@views.route('/')
@views.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html')


@views.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('Login.html')


@views.route('/validate', methods=["POST"])
def validate():
    if request.method == 'POST':
        login_user = request.form['login']
        password = request.form['password']
        if query().auth_user(f'{login_user}', f'{password}'):
            return render_template('Index.html', login_user=login_user)


@views.route('/register', methods=['POST', 'GET'])
def register():
    login = request.form['login']
    password = request.form['password']

    if login and password is not None:
        try:
            query().register_user(f'{login}', f'{password}')
            return render_template('Login.html')
        except:
            redirect(url_for('views.cadastro'))
