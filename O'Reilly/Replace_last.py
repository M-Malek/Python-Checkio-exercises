from typing import Iterable


def replace_last(items: list) -> Iterable:
    if not items:
        return items
    items.insert(0, items[-1])
    items.pop()
    return items


things = []
print(replace_last(things))
