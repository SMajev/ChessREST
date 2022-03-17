class Serializer:
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
                'figure': None,
                'moves': None,
                'error': 'No such figure!',
                'current_field': current_field,
            }

        return self.figure_json


