from flask import Flask, jsonify
from API import API


APP = Flask(__name__)
API = API()


@APP.route("/api/opt1/<string:figure>/<string:current_field>", methods=["GET"])
def show_available_moves_for(figure, current_field):

    available_moves, code = API.show_avail_moves_request(figure, current_field)
    # else:
    #     available_moves = None
    #     code = 409

    return jsonify(available_moves), code


@APP.route("/api/opt2/<string:figure>/<string:current_field>/<string:destination_field>",
    methods=["GET"],
)
def validate_move(figure, current_field, destination_field):
    move, code = API.validate_move(figure, current_field, destination_field)
        #     if move:
        #         code = 200
        #     else:
        #         code = 409
        # else:
    return jsonify(move), code


if __name__ == "__main__":
    # print(API.show_avail_moves_request('pawn', 'A2'))
    APP.run(debug=True, port=8000)
