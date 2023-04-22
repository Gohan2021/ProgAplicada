#Su tarea es crear una función que pueda tomar cualquier número entero no negativo como argumento y devolverlo con sus dígitos en orden descendente. Esencialmente, reorganiza los dígitos para crear el número más alto posible.
def descending_order(num):

    num = list(str(num))

    num.sort(reverse=True)

    result = int(''.join(num))

    return result