def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    try:
        if items == []:
            return items
        else:
            a = items.index(border)
            return items[a:]
    except:
        return items


items = [1,3,4,5,6]
border = 3
print(remove_all_before(items, border))