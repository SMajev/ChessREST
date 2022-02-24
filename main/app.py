from flask import Flask, request
from flask import jsonify
from API import API


app = Flask(__name__)
API = API()

def field_convert(field):
    x_letter = field[0:1]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    x = int(letters.index(x_letter))
    y = int(field[1:])
    print(x, y)
    return x, y 

@app.route("/api", methods=["GET"])
def test():
    destination = request.args.get("destination")
    current_field = request.args.get("current_field")
    x, y = field_convert(current_field)
    figure = request.args.get("figure")
    available_moves = API.show_avail_moves_request(figure, x, y)

    return jsonify(
        availableMoves=available_moves,
        figure=figure,
        error=None,
        currentField=current_field,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
