# Prüfe String auf Palindrom
def pruefe_palindrom(text):
    if text[:].upper() == text[::-1].upper():
        return True
    return False
        

print(pruefe_palindrom('Anna'))
print(pruefe_palindrom('Uwe'))
