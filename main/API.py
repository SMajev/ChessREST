from figures import *
from field_function import field_convert
from serializers import AvaiableMovesSerializer, ValidateMoveSerializer


class API:
    def show_avail_moves_request(self, figure, current_field):
        self.serializer = AvaiableMovesSerializer()
        try:
            x, y, error = field_convert(current_field)
            if error == "This field doesn't exist!":
                x = 0
                y = 0

            if figure == "pawn":
                figure_class = Pawn(x, y)

            elif figure == "rook":
                figure_class = Rook(x, y)
            
            elif figure == "bishop":
                figure_class = Bishop(x, y)
                
            elif figure == "knight":
                figure_class = Knight(x, y)
                
            elif figure == "queen":
                figure_class = Queen(x, y)
                
            elif figure == "king":
                figure_class = King(x, y)

            else:
                result = self.serializer.serilize(None, error, current_field), 404
                return result

            result = self.serializer.serilize(figure_class, error, current_field), 200
            return result
            
        except:
            return {'error': 404}, 404



    def validate_move(self, figure, current_field, destination_field):
        self.serializer = ValidateMoveSerializer()
        
        try:
            x , y, error = field_convert(current_field)
            x_dest, y_dest, error_destination = field_convert(destination_field)
            if error != "This field doesn't exist!" and error_destination != "This field doesn't exist!":
                
                if figure == "pawn":
                    figure_class = Pawn(x, y)

                elif figure == "rook":
                    figure_class = Rook(x, y)

                elif figure == "bishop":
                    figure_class = Bishop(x, y)

                elif figure == "knight":
                    figure_class = Knight(x, y)

                elif figure == "queen":
                    figure_class = Queen(x, y)

                elif figure == "king":
                    figure_class = King(x, y)

                else:
                    result = (
                        ValidateMoveSerializer(
                            None, error, error_destination, current_field, destination_field
                        ), 404
                    )
                    

                result = (
                    ValidateMoveSerializer(
                        figure_class, error, error_destination, current_field, destination_field
                    ), 200
                )
                return result
                
            else:
                result = (
                    ValidateMoveSerializer(
                        figure_class, error, error_destination, current_field, destination_field
                    ), 404
                )
                return result

        except:
            return {'error': 404}, 404