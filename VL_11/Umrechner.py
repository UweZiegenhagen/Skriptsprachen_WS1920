import xml.etree.ElementTree as et 

xtree = et.parse("eurofxref-daily.xml")
xroot = xtree.getroot()

rates = {}

for child in xroot:
    for subchild in child:
        for subsubchild in subchild:
            rates[subsubchild.attrib['currency']]  = float(subsubchild.attrib['rate'])

eingabe = input('Was soll ich umrechnen: ')

splits = eingabe.split(' ')

betrag = float(splits[0])
zielwaehrung = splits[3]

print(str(betrag), 'EUR entsprechen', betrag * rates[zielwaehrung], zielwaehrung)