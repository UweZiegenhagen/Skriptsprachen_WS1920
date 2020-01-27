# -*- coding: utf-8 -*-
"""

https://stackoverflow.com/questions/17250660/how-to-parse-xml-file-from-european-central-bank-with-python 
https://medium.com/@moreless/how-to-fix-python-ssl-certificate-verify-failed-97772d9dd14c    
"""

## Certifcate-related stuff
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


from urllib.request import urlopen    
from xml.etree import cElementTree as ET
rates = urlopen('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')
tree = ET.ElementTree(file=rates)
root = tree.getroot()

for child in root:
    for subchild in child:
        if subchild.tag.endswith('Cube'):
            print(subchild.attrib['time'], end='\n\n')
        for subsubchild in subchild:
            print(subsubchild.attrib['currency'], subsubchild.attrib['rate'])
