def digit_multip(number: int):
    result = 1
    for i in str(number):
        if i == "0":
            pass
        else:
            result *= int(i)
    return result


number = 15253450
print(digit_multip(number))