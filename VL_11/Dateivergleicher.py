import pandas as pd

quelle = pd.read_table('D:/Quelle.txt',skiprows=[1])
ziel = pd.read_table('D:/Ziel.txt',skiprows=[1])

print(len(quelle))
print(len(ziel))

vergleich = pd.merge(left=quelle,right=ziel, how='outer',
                     on='Dateiname',indicator=True)

print(vergleich)

vergleich = vergleich[vergleich['_merge'] != 'both']

vergleich['_merge'].replace('left_only', 'fehlt in Ziel', 
         inplace=True)
vergleich['_merge'].replace('right_only', 'fehlt in Quelle', 
         inplace=True)

vergleich.rename(columns={"_merge": "Fehlt wo"}, inplace=True)

print(vergleich)
