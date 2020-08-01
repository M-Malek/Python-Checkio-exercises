data = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ] #słownik zawierający nazwy i ceny produktów posiadający dwa klucze: "name" - nazwa przedmiotu i "price" - cena przedmiotu
limit = 2 #int podający ile towarów z TOP najdroższych ma się wyświetlić

new_table = sorted(data, key = lambda x:x['price'], reverse=True) #posortuj listę według funkcji lambda, która ustawia wartości w słowniku według ceny (price) od najniższej do najwyższej, reverse = True odwraca tą zależność
new_table = new_table[:limit] #przypisuje do new_table analizowany słownik data raz jeszcze, tym razem uwzględniając tylko "limit" pierwsze wpisy - u nas są to tylko 2 pierwsze wpisy

print(new_table)