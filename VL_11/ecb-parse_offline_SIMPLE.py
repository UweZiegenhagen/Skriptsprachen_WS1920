import pandas as pd
import xml.etree.ElementTree as et 

# Datei wurde heruntergeladen
xtree = et.parse("eurofxref-daily.xml")
xroot = xtree.getroot()

namespaces = {'ex': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}

for child in xroot:
    #print("Child: ", child)
    for subchild in child:
        #print("Subchild: ", subchild, subchild.tag)
        if subchild.tag.endswith('Cube'):
            print(subchild.attrib['time'], end='\n\n')
        for subsubchild in subchild:
            print(subsubchild.attrib['currency'], subsubchild.attrib['rate'])    

