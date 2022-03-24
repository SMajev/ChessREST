class AvaiableMovesSerializer:
    def serilize(self, figure, error, current_field):
        if figure and error != "This field doesn't exist!":
            self.figure_json = {
                'figure': figure.name,
                'moves': figure.moves,
                'error': error,
                'current_field': current_field,
            }

        elif figure and error == "This field doesn't exist!":
            self.figure_json = {
                'figure': figure.name,
                'error': error,
                'current_field': current_field
            }

        elif not figure and error != "This field doesn't exist!":
            self.figure_json = {
                'figure': figure,
                'error': 'No such figure!',
                'current_field': current_field,
            }
        else:
            self.figure_json = {
                'figure': figure,
                'error': 'No such figure!, ' + error,
                'current_field': current_field,
            }

        return self.figure_json


class ValidateMoveSerializer:
    def serialize(self, figure, error, error_destination, current_field, destination_field, response):
        if figure:
            self.figure_json = {
                'figure': figure.name,
                'error': error,
                'current_field': current_field,
                'destination_field': destination_field,
                'response': response
            }

        else:
            self.figure_json = {
                'error': f"{error}, {error_destination}",
                'current_field': current_field,
                'destination_field': destination_field
            }

        return self.figure_json


