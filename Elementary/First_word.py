text = "don't touch it"

text = text.replace(".", " ").replace(",", " ")
text = text.lstrip()
text = text.split()

print(text[0])
