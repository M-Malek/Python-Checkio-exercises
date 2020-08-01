#Find in set a number nearest number to the given one, e.g. set: values = {4,7,10,11,12,17}; int: one = 9 result: 10
values = {4, 7, 10, 11, 12, 17}
one = 9

def nearest_value(values: set, one: int):
    values = sorted(values)
    difference = abs(one - values[0])
    num = values[0]

    for i in values:
        if i == one:
            return one
        else:
            calc = abs(one - i)
            if calc < difference:
                difference = calc
                num = i

    return num


print(nearest_value(values, one))
