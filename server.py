from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search/<name>')
def search(name):
    from api.example import anime
    result = None
    while True:
        try:
            result = anime.search_animes(name)
            break
        except:
            pass
    return result


@ app.route('/getdetails/<animeid>')
def get_details(animeid):
    from api.example import anime
    result = None
    while True:
        try:
            result = anime.anime_details(animeid)
            break
        except:
            pass
    return result


if __name__ == "__main__":
    app.run()
