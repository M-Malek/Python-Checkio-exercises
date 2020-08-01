text = str(input("Podaj tekst do sprawdzenia:"))

if text == "":
    print(True)
elif text.isspace() == True:
    print(True)
elif text.isdigit() == True:
    print(True)
elif text.isupper() == True:
    print(True)
else:
    print(False)
