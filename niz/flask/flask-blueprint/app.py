from flask import Flask
from my_site.routes import site
from api.routes import api
from admin.routes import admin


app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(admin)


if __name__ == '__main__':
    app.run(debug=True)