from figures import *
import pytest
from field_function import *


def test_pawn1():
    x, y, _ = field_convert("H2")
    pawn = Pawn(x, y)
    result = ["H3", "H4"]
    assert pawn.list_available_moves() == result


def test_pawn2():
    x, y, _ = field_convert("H3")
    pawn = Pawn(x, y)
    result = ["H4"]
    assert pawn.list_available_moves() == result


def test_pawn3():
    x, y, _ = field_convert("H2")
    pawn = Pawn(x, y, color="black")
    result = ["H1"]
    assert pawn.list_available_moves() == result


def test_pawn4():
    x, y, _ = field_convert("E7")
    pawn = Pawn(x, y, color="black")
    result = ["E6", "E5"]
    assert pawn.list_available_moves() == result


def test_rook():
    x, y, _ = field_convert("F4")
    rook = Rook(x, y)
    result = [
        "F1",
        "A4",
        "F2",
        "B4",
        "F3",
        "C4",
        "F5",
        "E4",
        "F6",
        "F4",
        "F7",
        "G4",
        "F8",
        "H4"
       
    ]
    assert rook.list_available_moves() == result


def test_bishop():
    x, y, _ = field_convert("F4")
    bishop = Bishop(x, y)
    result = ["E3", "D2", "C1", "E5", "D6", "C7", "B8", "G3", "H2", "G5", "H6"]
    assert bishop.list_available_moves() == result


def test_knight():
    x, y, _ = field_convert("F4")
    knight = Knight(x, y)
    result = ["E2", "G2", "E6", "G6", "D3", "H3", "D5", "H5"]
    assert knight.list_available_moves() == result


def test_queen():
    x, y, _ = field_convert("F4")
    queen = Queen(x, y)
    result = [
        "F1",
        "A4",
        "F2",
        "B4",
        "F3",
        "C4",
        "F5",
        "E4",
        "F6",
        "F4",
        "F7",
        "G4",
        "F8",
        "H4",
        "E3",
        "D2",
        "C1",
        "E5",
        "D6",
        "C7",
        "B8",
        "G3",
        "H2",
        "G5",
        "H6",
    ]
    assert queen.list_available_moves() == result


def test_king():
    x, y, _ = field_convert("F4")
    king = King(x, y)
    result = ["G4", "F5", "G5", "E4", "F3", "E3", "G3", "E5"]
    assert king.list_available_moves() == result


def test_pawn_validate1():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("A4")
    pawn = Pawn(x, y)
    result = "is validate"
    assert pawn.validate_move(x_dest, y_dest) == result


def test_pawn_validate2():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("A8")
    pawn = Pawn(x, y)
    result = "isn't validate"
    assert pawn.validate_move(x_dest, y_dest) == result


def test_rook_validate1():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("D3")
    rook = Rook(x, y)
    result = "is validate"
    assert rook.validate_move(x_dest, y_dest) == result


def test_rook_validate2():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("F4")
    rook = Rook(x, y)
    result = "isn't validate"
    assert rook.validate_move(x_dest, y_dest) == result


def test_bishop_validate():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("B4")
    bishop = Bishop(x, y)
    result = "is validate"
    assert bishop.validate_move(x_dest, y_dest) == result


def test_bishop_validate2():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("A4")
    bishop = Bishop(x, y)
    result = "isn't validate"
    assert bishop.validate_move(x_dest, y_dest) == result


def test_knight_validate():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("C2")
    knight = Knight(x, y)
    result = "is validate"
    assert knight.validate_move(x_dest, y_dest) == result


def test_knight_validate2():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("A4")
    knight = Knight(x, y)
    result = "isn't validate"
    assert knight.validate_move(x_dest, y_dest) == result


def test_queen_validate():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("A4")
    queen = Pawn(x, y)
    result = "is validate"
    assert queen.validate_move(x_dest, y_dest) == result


def test_queen_validate2():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("G8")
    queen = Pawn(x, y)
    result = "isn't validate"
    assert queen.validate_move(x_dest, y_dest) == result


def test_king_validate():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("A4")
    king = King(x, y)
    result = "is validate"
    assert king.validate_move(x_dest, y_dest) == result


def test_king_validate2():
    x, y, _ = field_convert("A3")
    x_dest, y_dest, _ = field_convert("G8")
    king = King(x, y)
    result = "isn't validate"
    assert king.validate_move(x_dest, y_dest) == result
