# -*- coding: utf-8 -*-
"""
https://stackoverflow.com/questions/17250660/how-to-parse-xml-file-from-european-central-bank-with-python 
https://medium.com/@moreless/how-to-fix-python-ssl-certificate-verify-failed-97772d9dd14c    

Alternative Lösung mit XPATH
"""


from urllib.request import urlopen    
import xml.etree.ElementTree as et 
from xml.etree import cElementTree as ET

import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context



rates = urlopen('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')    # has to be full path#
tree = ET.ElementTree(file=rates)
xroot = tree.getroot()
namespaces = {'ex': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}

date_cube = xroot.find('.//ex:Cube[@time]', namespaces=namespaces)
print(date_cube.attrib['time'], end='\n\n')


for cube in xroot.findall('.//ex:Cube[@currency]', namespaces=namespaces):
    print(cube.attrib['currency'], cube.attrib['rate'])


