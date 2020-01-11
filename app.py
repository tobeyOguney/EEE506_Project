import flask
from flask import request
from main import main as predictor

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>EEE 506 Project: REST API</h1><p>This site is a prototype API for a machine learning powered power diagnostic tool.</p>"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    return predictor(data)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)