from typing import Iterable


def compress(items: list):
    result = []
    try:
        for i in range(0, len(items)):
            if items[i] == items[i + 1]:
                pass
            else:
                result.append(items[i])
    except IndexError:
        result.append(items[-1])
    return result


numbers = [
    5, 5, 5,
    4, 5, 6,
    6, 5, 5,
    7, 8, 0,
    0]  # result: [5, 4, 5, 6, 5, 7, 8, 0]
numbers2 = [1, 2, 3, 4]  # result: [1, 2, 3, 4]
numbers3 = [1, 1, 1, 1, 2, 2, 2, 1, 1, 1]  # result: [1, 2, 1]
print(compress(numbers))
