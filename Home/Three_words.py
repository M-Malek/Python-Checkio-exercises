words = "He is 123 man"

counter = 0

for w in words.split():
    if counter == 3:
        break
    if w.isalpha():
        counter += 1
    else:
        counter = 0
    if counter == 3:
        print("True")
        break
try:
    print("False")
except ValueError:
    counter != 3
