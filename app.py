from flask import Flask, render_template
from waitress import serve
import random

app = Flask(__name__)


@app.route('/')
def index():
    facts = open('facts.txt').read().splitlines()
    quote = random.choice(facts);
    return render_template('index.html', quote=quote)


if __name__ == '__main__':
    print('BatFacts server starting...')
    serve(app, listen='0.0.0.0:8081')
