from flask import Flask, render_template, request, session, redirect, url_for
from hangman import Hangman

app = Flask(__name__)
app.secret_key = 'secret'  # Secret to use sessions

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'game' not in session:
        session['game'] = Hangman().to_dict()

    game = Hangman.from_dict(session['game'])

    if request.method == 'POST':
        guess = request.form['guess'].lower()
        if len(guess) == 1 and guess.isalpha():
            game.guess(guess)

    session['game'] = game.to_dict()

    return render_template('index.html', 
                           word_display=game.display_word(),
                           guessed_letters=', '.join(sorted(game.guessed_letters)),
                           attempts_left=game.attempts,
                           message=game.message,
                           game_over=game.is_game_over())

@app.route('/new_game')
def new_game():
    session.pop('game', None)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)