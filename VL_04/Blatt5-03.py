def plus_sign(text):
    first_char = text[0]
    leere_variable = text.replace(first_char.lower(),'+')
    leere_variable = leere_variable.replace(first_char.upper(),'+')
    return leere_variable 

print(plus_sign('Ritter'))