from turtle import position
from figures import *
from field_function import field_convert
from serializer import Serializer


class API:
    def __init__(self) -> None:
        self.serializer = Serializer()

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
                    return result_json

            else:
                result_json = self.serializer.serilize(figure_class, error, current_field), 404
                return result_json

            result_json = self.serializer.serilize(figure_class, error, current_field), 200
            return result_json
            



        except:
            return 404



    def validate_move(self, figure, current_field, x_dest, y_dest):
        x , y, error = field_convert(current_field)
        if figure == "pawn":
            pawn = Pawn(x, y)

        elif figure == "rook":
            rook = Rook(x, y)

        elif figure == "bishop":
            bishop = Bishop(x, y)

        elif figure == "knight":
            knight = Knight(x, y)

        elif figure == "queen":
            queen = Queen(x, y)

        elif figure == "king":
            king = King(x, y)

        else:
            return False
