from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/greeting', methods=['GET'])
def display_greeting():
    return jsonify(message="Hi Client!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
