from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
@app.route('/Index')
def hello_world():  # put application's code here
    return render_template('Index.html')


if __name__ == '__main__':
    app.run()
