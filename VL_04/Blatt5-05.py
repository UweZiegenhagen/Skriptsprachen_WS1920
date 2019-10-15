def drehe_um(text):
    return text[text.index(',')+2:] + ' ' + text[:text.index(',')]

print(drehe_um('Duck, Donald'))
