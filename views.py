from flask import Blueprint, render_template

views = Blueprint('views',__name__)


@views.route('/Index')
def index():
    return render_template('Index.html')
@views.route('/Cadastro')
def cadastro():
    return render_template('Cadastro.html')
@views.route('/Login')
def login():
    return render_template('Login.html')
