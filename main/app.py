from flask import Flask, request
from flask import jsonify
from API import API
from field_function import field_convert

APP = Flask(__name__)
API = API()


@APP.route("/api/opt1/<string:figure>/<string:current_field>", methods=["GET"])
def show_available_moves_for(figure, current_field):
    try:
        x, y, error = field_convert(current_field)
        if error != "This field doesn't exist!":
            available_moves = API.show_avail_moves_request(figure, x, y)
            if available_moves:
                code = 200
            else:
                code = 404
        else:
            available_moves = None
            code = 409

        return (
            jsonify(
                availableMoves=available_moves,
                figure=figure,
                error=error,
                currentField=current_field,
            ),
            code,
        )
    except:
        return 500


@APP.route(
    "/api/opt2/<string:figure>/<string:current_field>/<string:destination_field>",
    methods=["GET"],
)
def validate_move(figure, current_field, destination_field):
    try:
        x, y, error = field_convert(current_field)
        if error != "This field doesn't exist!":
            x_dest, y_dest, error = field_convert(destination_field)
            move = API.validate_move(figure, x, y, x_dest, y_dest)
            if move:
                code = 200
            else:
                code = 409
        else:
            move = None

        return (
            jsonify(
                move=move,
                figure=figure,
                error=error,
                current_field=current_field,
                destination_field=destination_field,
            ),
            code,
        )
    except:
        return 500


if __name__ == "__main__":
    APP.run(debug=True, port=8000)
