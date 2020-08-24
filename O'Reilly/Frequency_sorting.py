def frequency_sorting(numbers):
    # Check if list is descending: if it is descending, sort list ascending
    # if not, sort the list by elements, frequency
    elements_amount = {}
    first_element_frequency_sort = {}
    result = []
    if sorted(numbers) == numbers[::-1]:
        return sorted(numbers)
    else:
        numbers.sort()
        for i in numbers:
            elements_amount[i] = numbers.count(i)
        sorted_by_amount = sorted(elements_amount.items(), key=lambda x: x[1], reverse=True)
        for i in sorted_by_amount:
            if i[1] == 1:
                pass
            else:
                for j in range(0, i[1]):
                    result.append(i[0])

        numbers = [x for x in numbers if x not in result]
        numbers.sort()

        return result + numbers


number_list = [5, 6, 13, 99, 45, 34, 99, 6, 6, 45]
number_list2 = [3, 4, 11, 13, 11, 4, 4, 7, 3]
print(frequency_sorting(number_list))
