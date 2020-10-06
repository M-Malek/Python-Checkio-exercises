def checkio(numbers_array: tuple):
    return sorted(numbers_array, key=lambda x: abs(x))


array = [-20, -5, 10, 15, ]
print(checkio(array))
