def flat_list(array):
    result = []
    for i in array:
        if type(i) == list:
            result.extend(flat_list(i))
        else:
            result.append(i)
    return result


list_1 = [1, 2, 3]
list_2 = [1, [2, 2, 2], 4]
list_3 = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
list_4 = [-1, [1, [-2], 1], -1]

x = list(flat_list(list_3))
print(x)
