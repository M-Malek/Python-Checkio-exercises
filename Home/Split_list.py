entry_list = [1, 2, 3, 4, 5, 6]
new_list_1 = []
new_list_2 = []
result_list = []
j = 0

if len(entry_list) == 0:
    result_list.append(new_list_1)
    result_list.append(new_list_2)
    print(result_list)

elif len(entry_list) % 2 == 0:
    for i in entry_list:
        if j < len(entry_list)/2:
            new_list_1.append(i)
            j += 1
        else:
            new_list_2.append(i)
            j += 1


elif len(entry_list) % 2 != 0:
    border = int(len(entry_list) / 2)+1
    for i in entry_list:
        if j < border:
            new_list_1.append(i)
            j += 1
        else:
            new_list_2.append(i)
            j += 1


result_list.append(new_list_1)
result_list.append(new_list_2)
print(result_list)


def test(entry_list):
    new_list_1 = [1]
    new_list_2 = [3]
    return new_list_1, new_list_2


