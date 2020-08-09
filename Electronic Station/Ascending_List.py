from typing import Iterable


def is_ascending(items: Iterable[int]):
    if len(items) == 1 or items == []:
        return True
    elif items.count(items[0]) == len(items):
        return False
    else:
        m = items[0]
        for i in items:
            if i < m:
                return False
            m = i

    return True


items = [99]
print(is_ascending(items))
