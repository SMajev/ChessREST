from figures import *
from board import Board


if __name__ == "__main__":
    board = Board()
    board.show_board()


# # litera , cyfra
#     pawn1 = Pawn(board.board, 7, 1)
#     pawn2 = Pawn(board.board, 1, 6, "black")
#     pawn3 = Pawn(board.board, 1, 2)
#     pawn4 = Pawn(board.board, 0, 5, "black")
#     print("Pawn1(White):")
#     print(pawn1.position)
#     print(pawn1.list_available_moves())
#     print("\n")
#     print("Pawn2(Black):")
#     print(pawn2.position)
#     print(pawn2.list_available_moves())
#     print("\n")
#     print("Pawn3(White):")
#     print(pawn3.position)
#     print(pawn3.list_available_moves())
#     print("\n")
#     print("Pawn4(Black):")
#     print(pawn4.position)
#     print(pawn4.list_available_moves())

# rook1 = Rook(board.board, 5, 5)
# print(f"Rook{rook1.position}:")
# print(rook1.list_available_moves())
# print("\n")

# bishop1 = Bishop(board.board, 5, 5)
# print(f"Bishop{bishop1.position}:")
# print(bishop1.list_available_moves())
# print("\n")

# knight = Knight(board.board, 2, 4)
# print(f"knight{knight.position}:")
# print(knight.list_available_moves())
# print("\n")
