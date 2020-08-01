array = []
sumNumbers = 0
if not array:    #check, if array is empty
    print("0")
else:
    for i in range(len(array)):
        if i % 2 == 0:
            sumNumbers += array[i]

    print(sumNumbers*array[-1])