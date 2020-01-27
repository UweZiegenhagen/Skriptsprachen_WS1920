import xml.etree.ElementTree as et 

xtree = et.parse("eurofxref-daily.xml")
xroot = xtree.getroot()

for child in xroot:
    for subchild in child:
        if subchild.tag.endswith('Cube'):
            print(subchild.attrib['time'], end='\n\n')
        for subsubchild in subchild:
            print(subsubchild.attrib['currency'], subsubchild.attrib['rate'])    

