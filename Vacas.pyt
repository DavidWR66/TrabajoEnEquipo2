n=40
m=20
l=m*n#espacio
k=5#pasto necesario por vaca

v= int(input("cuantas vacas tiene en su granaja"))

x=l/(v*k)#litro producidos por dia
n=x*7 #litros por semana

print("las vacas producen",n,"litros en la semana")
