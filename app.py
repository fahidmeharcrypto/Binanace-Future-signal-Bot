from flask import Flask, render_template
from signal_generator import generate_signals
import time

app = Flask(__name__)

@app.route('/')
def home():
    signals = generate_signals()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', signals=signals, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True)
