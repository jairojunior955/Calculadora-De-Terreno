from flask import Flask, redirect, render_template, request, url_for, session
# from views import views
from packages.Database.database import Query
from packages.calculate_area.calculo_de_terreno import Rectangle, Elipse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pppppp'


@app.route('/')
def home():
    return render_template('TelaInicial.html')


@app.route('/cadastro', methods=['post'])
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
        if Query().auth_user(f'{login_user}', f'{password}'):
            if login_user is not None:
                session['login'] = login_user
                return render_template('Index.html', login_user=login_user)
            else:
                redirect(url_for("login"))
        else:
            return redirect(url_for("login"))


@app.route('/register', methods=['POST', 'GET'])
def register():
    login = request.form['login']
    password = request.form['password']
    check = Query().check_exists('login')
    if not check:
        Query().register_user(f'{login}', f'{password}')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('cadastro'))


@app.route('/erro')
def erro():
    return render_template('CadastroErro.html')


@app.route('/index', methods=['POST', 'GET'])
def index():
    if 'login' in session:
        login_user = session['login']
        return render_template('Index.html', login_user=login_user)
    else:
        return redirect(url_for('login'))


@app.route('/gerar', methods=['POST', 'GET'])
def gerar():
    if request.method == 'POST':
        formato = request.form['option']
        arealote = float(request.form['area-lote'])
        x_e = float(request.form['x-extra'])
        y_e = float(request.form['y-extra'])
        custo = float(request.form['custo'])
        user = session['login']
        if formato == 'RECTANGLE':
            area = Rectangle().calculate_area_rectangle(x_e, y_e, arealote)
            custo_total = round(Rectangle().calculate_cost(area[2], custo), 2)
            area = [round(i, 2) for i in area]
            Query().log_generator(
                user,
                x_e,
                y_e,
                arealote,
                area[2],
                area[1],
                area[0],
                custo)
            return render_template(
                'Resultado.html',
                resposta=area,
                custo=custo_total)
        if formato == 'ELIPSE':
            area = Elipse().calculate_area_elipse(x_e, y_e, arealote)
            custo_total = round(Elipse().calculate_cost(area[2], custo), 2)
            area = [round(i, 2) for i in area]
            Query().log_generator(
                user,
                x_e,
                y_e,
                arealote,
                area[2],
                area[1],
                area[0],
                custo)
            return render_template(
                'Resultado.html',
                resposta=area,
                custo=custo_total)
    return render_template('Index.html')


@app.route('/historico', methods=['POST'])
def historico():
    print(session)
    if 'login' in session:
        user = session['login']
        historico = Query().get_log(user)
        print(historico)
        return render_template('Historico.html', historico=historico)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
