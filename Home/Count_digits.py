text = "test123"

counter = 0
for i in text:
    if i.isdigit() == True:
        counter += 1

print(counter)