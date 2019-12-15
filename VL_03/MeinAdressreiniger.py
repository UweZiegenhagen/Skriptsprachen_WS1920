# Lade die Datei schreibgeschützt als Textdatei
with open('Datensatz.txt', 'rt', encoding='utf-8') as eingabedatei:
    for zeile in eingabedatei:
        
        if zeile[-1] == '\n':
            zeile = zeile[:-1] # Entferne Zeilenumbruch, falls vorhanden
        gesplittet = zeile.split(' ') # Splitte anhand des Leerzeichens
        print(gesplittet) # gibt die Liste aus

        if gesplittet[-1].isdigit() and gesplittet[0].isdigit():
            namensteil = ''
            for i in gesplittet[1:]:
                namensteil = namensteil + " " + i 
            print('Name ist "', namensteil.strip() ,  '", Hausnummer ist ',  gesplittet[0], sep = '')

        elif gesplittet[-1][0].isdigit() and gesplittet[-1][-1].isalpha():
            namensteil = ''
            for i in gesplittet[:-1]:
                namensteil = namensteil + " " + i 
            print('Name ist "', namensteil.strip() ,  '", Hausnummer ist ',  gesplittet[-1], sep = '')
        
        elif gesplittet[-1].isdigit():
            namensteil = ''
            for i in gesplittet[:-1]:
                namensteil = namensteil + " " + i 
            print('Name ist "', namensteil.strip() ,  '", Hausnummer ist ',  gesplittet[-1], sep = '')
            
        elif gesplittet[0].isdigit():
            namensteil = ''
            for i in gesplittet[1:]:
                namensteil = namensteil + " " + i 
            print('Name ist "', namensteil.strip() ,  '", Hausnummer ist ',  gesplittet[0], sep = '')            
            
        elif gesplittet[0][0].isdigit() and gesplittet[0][-1] == ',':
            namensteil = ''
            for i in gesplittet[1:]:
                namensteil = namensteil + " " + i 
            print('Name ist "', namensteil.strip() ,  '", Hausnummer ist ',  gesplittet[0][:-1], sep = '')   





                     