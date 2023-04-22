#Tome 2 cadenas s1 y s2 que incluyan solo letras de la a a la z. Devuelve una nueva cadena ordenada, la más larga posible, que contiene letras distintas, cada una tomada solo una vez, provenientes de s1 o s2.

def longest(a1, a2):
    a = a1 + a2
    result = ''.join(sorted(set(a)))
    return result