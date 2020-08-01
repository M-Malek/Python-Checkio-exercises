#Divide given string into pairs, e.g "abc"  -> ['ab','c_']
a = input("Give ma a text to split: ")
result = []

for i in range(0,len(a),2):
    result.append(a[i:i+2])

if len(a) % 2 !=0:
    b = result[int(len(result) - 1)]
    b = b + "_"
    result.pop(-1)
    result.append(b)

print(result)

