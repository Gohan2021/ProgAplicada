#En este kata, debe escribir una función que tome una cadena y una letra como entrada y luego devuelva el índice de la segunda aparición de esa letra en la cadena. Si no hay tal letra en la cadena, entonces la función debería devolver -1. Si la letra aparece solo una vez en la cadena, también se debe devolver -1.
def second_symbol(s, symbol):
    count = 0
    index = -1

    for i, char in enumerate(s):
        if char == symbol:
            count += 1
            if count == 2:
                index = i
                break
    return index
