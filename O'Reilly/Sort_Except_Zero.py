from typing import Iterable


def except_zeros(items: list):
    zeros_position = [i for i, x in enumerate(items) if x == 0]
    items[:] = (i for i in items if i != 0)
    items.sort()
    for i in zeros_position:
        items.insert(i, 0)
    return items


listed = [2, 0, 4, 5, 1, 6, 0, 0, 3, 9]

print(except_zeros(listed))
