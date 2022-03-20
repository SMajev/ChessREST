from figures import *
from field_function import field_convert
from serializers import AvaiableMovesSerializer, ValidateMoveSerializer


class API:
    def __init__(self) -> None:
        self.serializer = AvaiableMovesSerializer()

    def show_avail_moves_request(self, figure, current_field):

        try:
            x, y, error = field_convert(current_field)
            if error != "This field doesn't exist!":
                
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
                    result_json = self.serializer.serilize(None, error, current_field), 404
                    

            else:
                result_json = self.serializer.serilize(figure_class, error, current_field), 404
                

            result_json = self.serializer.serilize(figure_class, error, current_field), 200
            return result_json
            
        except:
            return 404



    def validate_move(self, figure, current_field, destination_field):
        try:
            x , y, error = field_convert(current_field)
            x_dest, y_dest, error_destination = field_convert(destination_field)

            if (
                error != "This field doesn't exist!" and error_destination != "This field doesn't exist!"
            ):
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
                    result_json = (
                        ValidateMoveSerializer(
                            None, error, error_destination, current_field, destination_field
                        ), 404
                    )
                    return result_json
            else:
                if destination_field in figure_class.moves:
                    response = True
                    result_json = (
                        ValidateMoveSerializer(
                            figure_class, error, error_destination, current_field, destination_field,
                            response
                        ), 404
                    )
                    return result_json
                    

        except:
            print('Here!!!!!')
            return "", 404