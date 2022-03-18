class AvaiableMovesSerializer:
    def serilize(self, figure, error, current_field):
        if figure:
            self.figure_json = {
                'figure': figure.name,
                'moves': figure.moves,
                'error': error,
                'current_field': current_field,
            }
        else:
            self.figure_json = {
                'error': 'No such figure!',
                'current_field': current_field,
            }

        return self.figure_json


class ValidateMoveSerializer:
    def serialize(self, figure, error, error_destination, current_field, destination_field):
        if figure:
            self.figure_json = {
                'figure': figure.name,
                'error': error,
                'current_field': current_field,
                'destination_field': destination_field
            }
        else:
            self.figure_json = {
                'error': f"{error}, {error_destination}",
                'current_field': current_field,
                'destination_field': destination_field
            }
            
        return self.figure_json


