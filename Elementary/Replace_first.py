items = []

if items == []:
    print(items)
elif len(items) == 1:
    print(items)
else:
    a = items[0]
    items.append(a)
    items.pop(0)
    print(items)