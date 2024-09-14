import math

print("Adj mega kör átmérőjét:")
atmer = int(input("1.szám: "))

r = atmer/2
ter = (r*r)*math.pi
ker = 2 * math.pi*r

print("A kör területe: "+str(ter) + "\n")
print("A kör kerülete: "+str(ker))
