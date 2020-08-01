text = "hi mr Mayor"
symbol = " "

if text.count(symbol) < 2:
    print(None)
else:
    firstSymbol = text.find(symbol)
    if firstSymbol == 0:
        text = text[1:len(text)]
        print(text.find(symbol)+1)
    else:
        text = text[firstSymbol+1:len(text)]
        print(text)
        secondSymbol = text.find(symbol) + len(text[0:firstSymbol])
        print(secondSymbol)

#Funkcja find() może przyjąć 2 argumenty, pierwszy: jakiego znaku szukamy, drugi: od którego miejsca szukamy. Jak znajdziemy 1 znak i wpiszemy że ma szukać od jego indeksu + 1 (żeby go nie znalazło) to znajdzie nam kolejny index
#Wygląda to tak
if text.count(symbol) < 2:
    print(None)

firstSymbol = text.find(symbol)
print(text.find(symbol, firstSymbol+1))