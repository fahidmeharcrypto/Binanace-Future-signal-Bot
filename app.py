from flask import Flask, render_template
from signal_generator import signal_generator

app = Flask(__name__)

@app.route('/')
def index():
    signal = signal_generator()
    return render_template('index.html', signal=signal)
