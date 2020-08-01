#Reverse given text
text = "hello       world"

text = text[::-1]
textReverse = text.split(' ')
result = ' '.join(reversed(textReverse))

print(result)