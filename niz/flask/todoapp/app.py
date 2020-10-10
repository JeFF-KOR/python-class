import os
from flask import Flask
from extensions import mongo
from dotenv import load_dotenv
from main.routes import main

load_dotenv()
user_id = os.getenv('USER_ID')
user_password = os.getenv('USER_PASSWORD')

app = Flask(__name__)
# Need dnspython
app.config['MONGO_URI'] = f'mongodb+srv://{user_id}:{user_password}@cluster0.hbauo.mongodb.net/testdb?retryWrites=true&w=majority'
# mongodb+srv://<username>:<password>@cluster0.hbauo.mongodb.net/<dbname>?retryWrites=true&w=majority
mongo.init_app(app)
todos = mongo.db.todos

app.register_blueprint(main)



if __name__ == '__main__':
    app.run(debug=True)