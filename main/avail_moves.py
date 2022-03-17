# from figures import *
# from flask import jsonify



# class AvailableMovesSerializer:
#     serializer = Serializer()
#     def serialize(self, figure, x, y):
#         if figure == "pawn":
#             pawn = Pawn(x, y)          
#             return serializer(pawn)

#         if figure == "rook":
#             rook = Rook(x, y)
#             return rook.list_available_moves()

#         if figure == "bishop":
#             bishop = Bishop(x, y)
#             return bishop.list_available_moves()

#         if figure == "knight":
#             knight = Knight(x, y)
#             return knight.list_available_moves()

#         if figure == "queen":
#             queen = Queen(x, y)
#             return queen.list_available_moves()

#         if figure == "king":
#             king = King(x, y)
#             return king.list_available_moves()

#         else:
#             return False

# if __name__ == "__main__":
#     serializer = AvailableMovesSerializer()
#     print(serializer.serialize('pawn', 2, 2))