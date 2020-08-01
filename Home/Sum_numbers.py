text = ('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year')

sumOfDigit = 0
if not text: #sprawdź czy tekst jest pusty - w sensie czy nie ma tekstu
    print(0)
else:
    l = []
    for i in text.split(): #rozdzielamy text czyli string na poszczególne znaki a następnie przypisujemy im wartość i, to leci przez cały string. Jak już to zrobi, to dodajemy to do listy l, konwertując to na int, jeżeli jest błąd (czyli znak nie jest cyfrą) to pomijamy
        try:
            l.append(int(i))
        except ValueError:
            pass
    for i in l:
        sumOfDigit += i

    print(sumOfDigit)


