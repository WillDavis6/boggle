from boggle import Boggle
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.config['SECRET_KEY'] ='secret'

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def homepage():

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)
   
    "Builds empty board and starts the game"
    return render_template("index.html",
    board=board,
    highscore= session.get("highscore", 0)
    nplays = session.get("nplays", 0))

@app.route("/check=word")
def check_word():
    "Check if word is in dictionary"
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/post-score", methods=['POST'])
def post_score():
    """Reviece score, update nplays, update high score if appropriate"""

    score = request.json["highscore", 0]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)
