aves = int(input("Cuantas aves tiene en el galpon de su granja: "))
gallinas = int(aves / 3)
pollos = aves - gallinas
gallinas_1 = gallinas / 2
gallinas_2 = gallinas / 2

g_1_H = (30 / 3) * gallinas_1
g_2_H = (30 / 5) * gallinas_2

pro_total = g_1_H + g_2_H
print("En el galpon hay ",gallinas," gallinas")
print("En el galpon hay ",pollos," pollos")
print("Total de huevos que producen sus gallinas en un mes es: ",pro_total)