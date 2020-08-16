from typing import List


def checkio(data: List[int]):
    data.sort()
    return (data[len(data)//2] + data[len(data) // 2-1]) / 2 if len(data) % 2 == 0 else data[len(data)//2]


data_list = [3, 6, 20, 99, 10, 15]
print(checkio(data_list))
