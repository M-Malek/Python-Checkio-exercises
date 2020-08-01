from datetime import date #biblioteka operująca na datach

a = (1982, 4, 19)
b = (1982, 4, 22)

c = date(*a) # *a - zapis *a jest równoznaczny z zapisem (a[0], a[1], a[2]) itd
d = date(*b)
delta = abs(c - d)

print(delta)
print("A jak nie chcesz minut, to tak:")

e = date(*a)
f = date(*b)
delta = abs((e-f).days) # .days zwraca nam samą ilość dni pomiędzy datami a i b, normalnie ich odjęcie zwróci nam zapis 3 days, 0:00:00 co może nie być akceptowalne

print(delta)