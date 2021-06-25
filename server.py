from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search/<name>')
def search(name):
    from api.example import search_animes
    result = str(search_animes(name))
    return result


if __name__ == "__main__":
    app.run()
