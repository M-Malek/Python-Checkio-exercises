val = str(input("Give a text to reverse: "))

new_val = ""

while val != "":
    new_val += val[len(val)-1]
    val = val[:len(val)-1]

print("Reversed text: ")
print(new_val)