def cipher_map(code: list, decoder: list):
    #Find all x positions in currently analyzed decoder table
    def x_positions(dec):
        x_pos = {}
        counter = 0
        for row in dec:
            x_p = [i for i, x in enumerate(row) if x == "X"]
            x_pos[counter] = x_p
            counter += 1
        return x_pos

    #Rotate decoder table by 90 degrees clockwise
    def decoder_rotate(dec):
        return list(zip(*dec[::-1]))

    #Decode the message as one posible position of decoder table used on our message in "code"
    def piece_decode(code, decoder):
        piece_result = ""
        decoder_x_p = x_positions(decoder)
        for i in range(0, 4):
            x_pos = decoder_x_p[i]
            for x in x_pos:
                for j in code[i]:
                    if code[i].index(j) == x:
                        piece_result += j
        return piece_result

    #In for loop: decode message by decode a piece of message one by one - add each piece to reslut, then: return the result
    result = ""
    for i in range(0, 4):
        result += piece_decode(code, decoder)
        decoder = decoder_rotate(decoder)
    return result


cipher_algorithm1 = ['X...', '..X.', 'X..X', '....']
message1 = ['itdf', 'gdce', 'aton', 'qrdi']
print(cipher_map(message1, cipher_algorithm1))
#result: message = 'icantforgetiddqd'

cipher_algorithm2 = ['....', 'X..X', '.X..', '...X']
message2 = ['xhwc', 'rsqx', 'xqzz', 'fyzr']
print(cipher_map(message2, cipher_algorithm2))
#result: message = 'rxqrwsfzxqzhczy'
