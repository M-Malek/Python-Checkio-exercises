def index_power(array: list, n: int):
    try:
        return array[n] ** n
    except IndexError:
        return -1


number_list = [1, 2]
power = 3

print(index_power(number_list, power))
