import math
def f(a:float, b:float, c:float) -> float:
  if a==0:
    raise Exception("a no puede ser cero")
  if b*b< 4*a*c:
    raise Exception("Esos valores dan un resultado complejo")
  try:
    d=(-b + math.sqrt(b*b - 4*a*c))/(2*a)
  except:
    print("Hay un error")
  return d
a=0
b=3
c=-3
print(f(a,b,c))