from flask import Flask, render_template
import signal_generator

app = Flask(__name__)

@app.route('/')
def home():
    signal = signal_generator.get_signal()
    return render_template('index.html', signal=signal)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
