from typing import Iterable


def remove_all_after(items: list, border: int):
    try:
        return items[0:items.index(border)+1]
    except ValueError:
        return items


numbers_list = [1, 2, 4, 5, 6, 7, 8, 9]
numbers_border = 3
print(remove_all_after(numbers_list, numbers_border))
