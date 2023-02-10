#import math
a = float(input("ingrese el valor de la nota a:"))
b = float(input("ingrese el valor de la nota b:"))
c = float(input("ingrese el valor de la nota c:"))
def f(d1, d2, d3):
  m = min(d1, d2, d3)
  s = (d1 + d2 + d3 -m)/2
  return s
  if d1 > d2: 
    if d2 > d3:
      s = (d1 + d2)/2
    else:
      s = (d1 + d3)/2
  else: 
    if d1 > d3:
      s = (d2 + d1)/2
    else: 
      s = (d2 + d3)/2
      
prom = f(a,b,c)
print("El promedio de las dos mejores notas es:", prom)

# Los cambios realizados fueron en las lineas 6 a 8 con respecto a las condiciones if, debido a que en el programa que realicé en el papel tenia de primeras las condicones y después las lienas de la 6 a 8, también la identación en los if y los ":" al final de cada condición

#Nicolas Moreno Ovalle - 20212005140