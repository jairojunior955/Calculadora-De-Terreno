from flask import Flask, redirect, render_template, request, url_for, flash
# from views import views
from flask_bootstrap import Bootstrap4
from flask_session import Session
from packages.Database.database import Query as query
from packages.calculate_area.calculo_de_terreno import Rectangle,Elipse
app = Flask(__name__)
app.config['SECRET_KEY'] = '123321'
Session(app)
Bootstrap4(app)


@app.route('/')
@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('Login.html')


@app.route('/validate', methods=["POST"])
def validate():
    if request.method == 'POST':
        login_user = request.form['login']
        password = request.form['password']
        if query().auth_user(f'{login_user}', f'{password}'):
            return render_template('Index.html', login_user=login_user)


@app.route('/register', methods=['POST', 'GET'])
def register():
    login = request.form['login']
    password = request.form['password']
    check = query().check_exists('login')
    if not check:
        query().register_user(f'{login}', f'{password}')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('cadastro'))


@app.route('/erro')
def erro():
    return render_template('CadastroErro.html')


@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('Index.html')

@app.route('/gerar', methods=['POST', 'GET'])
def gerar():
    if request.method == 'POST':
        formato = request.form['option']
        arealote = float(request.form['area-lote'])
        xE = float(request.form['x-extra'])
        yE = float(request.form['y-extra'])
        custo = float(request.form['custo'])
        if formato == 'RECTANGLE':
            area = Rectangle().calculate_area_rectangle(xE,yE,arealote)
            custoTotal = round(Rectangle().calculate_cost(area[2],custo))
            print(area)
            print(custoTotal)
            return render_template('Resultado.html', resposta=area, custo=custoTotal)
        if formato == 'ELIPSE':
            area = Elipse().calculate_area_elipse(xE,yE,arealote)
            custoTotal = round(Elipse().calculate_cost(area[2],custo))
            return render_template('Resultado.html', resposta=area, custo=custoTotal)
    return render_template('Index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
