# Find how many times digit "0" figure in given string
def beginning_zeros(number: str) -> int:
    # In loop: if an element of string is "0", increase counter by 1
    counter = 0
    for i in range(0, len(number)):
        if number[i] == "0":
            counter += 1
        else:
            break

    return counter

text = "000111001"
print(begining_zeros(text))
