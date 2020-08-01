items = [6, 6, 2, 2, 6, 4, 4, 4,4]

result_list = []
if items == [] or len(items) == 1:
    print(items)
else:
    a = items.count(items[0])
    for j in items:
        b = items.count(j)
        if b > a:
            break

    elementsDic = dict((i, 0) for i in items)

    for i in elementsDic:
        elementsDic[i] = items.count(i)

    print(elementsDic)

    mostPopularItem = max(elementsDic, key=elementsDic.get)
    amountOfMostPopularItem = elementsDic.get(mostPopularItem)
    for k in range(0, amountOfMostPopularItem):
        result_list.append(mostPopularItem)
        items.remove(mostPopularItem)

    result_list = result_list + items
    print(result_list)
    print("Most populat item: " + str(mostPopularItem))

