from flask import Flask
from views import views
from secrets import secret
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.config['SECRET_KEY'] = secret
Bootstrap4(app)

app.register_blueprint(views, url_prefix='/views')
if __name__ == '__main__':
    app.run(debug=True, port=8000)
