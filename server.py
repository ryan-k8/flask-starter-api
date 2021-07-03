from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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


@app.route('/getdetails/<animeid>')
def get_details(animeid):
    from api.example import anime
    result = {'message': 'i don"t know shit'}
    while True:
        try:
            result = anime.anime_details(animeid)
            break
        except:
            pass
    return result


@app.route('/stream/<animeid>/ep/<ep_no>')
def stream(animeid, ep_no):
    from api.example import anime
    test_result = ''
    while True:
        try:
            test_result = anime.stream_anime(animeid, ep_no)
            break
        except:
            pass
    return test_result


if __name__ == "__main__":
    app.run()
