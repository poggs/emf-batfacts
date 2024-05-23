from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    facts = open('facts.txt').read().splitlines()
    quote = random.choice(facts);

    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
