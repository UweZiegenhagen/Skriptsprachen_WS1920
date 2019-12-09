
zahlenliste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wortliste = ['abc', 'def', 'ghi']

f = filter(lambda x: x % 2 == 0, zahlenliste)
print(list(f))

c = lambda x: x.capitalize()
print(list(map(c, wortliste)))

from functools import reduce
s = lambda x, y : x + y
print(reduce(s, zahlenliste))