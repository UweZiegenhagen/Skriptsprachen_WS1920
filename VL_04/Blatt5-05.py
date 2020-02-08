# Wandel Namen der Form "Mustermann, Max" in "Max Mustermann" um

def drehe_um(text):
    return text[text.index(',')+2:] + ' ' + text[:text.index(',')]

print(drehe_um('Duck, Donald'))
