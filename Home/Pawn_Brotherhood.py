def sorting(n):
    return n[0]


safe_pawns = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
x_all_positions = "abcdefgh"
pawns = 0

for pawn in safe_pawns:
    if (str(chr(ord(pawn[0])))) in x_all_positions:
        x_backward = str(chr(ord(pawn[0]) - 1))
        x_forward = str(chr(ord(pawn[0]) + 1))
        y_required_position = str(int(pawn[1]) - 1)
        xy_back = x_backward + y_required_position
        xy_next = x_forward + y_required_position
        if xy_next in safe_pawns or xy_back in safe_pawns:
            pawns += 1
    else:
        pass


print("Safe pawns: " + str(pawns))



