def field_convert(field):
    x_letter = field[:1].lower()
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    try:
        x = int(letters.index(x_letter))
        y = int(field[1:]) - 1
        error = None
        return x, y, error
        
    except:
        x = None
        y = None
        error = "This field doesn't exist!"
        return x, y, error


def tuple_to_string(tup):
    list_of_moves = []
    for item1, item2 in tup:
        list_of_moves.append(item1 + str(item2))

    return list_of_moves
