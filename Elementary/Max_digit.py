a = int(input("Give me a number: "))

a = str(a)
table = []

for i in range(0, len(a)):
    table.append(a[i])

table.sort()
print(table[len(a)-1])

b = int(input("Give me new number: "))
print(max(str(b)))