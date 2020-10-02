from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world</h1>'

# Endpoints
@app.route('/home/<test>', methods=['GET', 'POST'])
def home(test):
    return '<h1>Home Page</h1>'+ test

# Render page
@app.route('/render')
def render():
    return render_template('render.html', testvar = 'testvar')


# Form proecess
@app.route('/process', methods=["POST"])
def process():
    name = request.form['name']
    return f'{name}'

if __name__ == '__main__':
    app.run(debug=True)