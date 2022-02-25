from flask import Flask, request
from flask import jsonify
from API import API
from field_function import field_convert, field_check

app = Flask(__name__)
API = API()


@app.route("/api/avail_moves", methods=["GET"])
def show_available_moves_for():
    destination = request.args.get("destination")
    current_field = request.args.get("current_field")
    figure = request.args.get("figure")
    x, y, error = field_convert(current_field)
    if x != None and y != None:
        available_moves = API.show_avail_moves_request(figure, x, y)
    else:
        available_moves = None

    return jsonify(
        availableMoves=available_moves,
        figure=figure,
        error=error,
        currentField=current_field,
    )


@app.route("/api/is_validate", methods=["GET"])
def validate_move():
    pass


if __name__ == "__main__":
    app.run(debug=True, port=8000)
