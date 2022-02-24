from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return jsonify(result='To jest test')

@app.route('/test2', methods=['POST'])
def test2():
    request_data = request.get_json()
    return jsonify(result='To jest test')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
