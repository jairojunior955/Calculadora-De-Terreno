from sympy import *

x = symbols('x')
terr_x = float(input("Insira os valores para o X do terreno: "))
terr_y = float(input("Insira os valores para o Y do terreno: "))
tam_ar = float(input("Insira os valores para a Área do terreno: "))

al = (terr_x + tam_ar / x) * (terr_y + x)

d_al = diff(al, x)

pc = solve(Eq(d_al, 0), x)

for n in pc:
    if n > 0:
        pc = n

area_interna_y = tam_ar / pc

x_area_final = pc + terr_y
y_area_final = area_interna_y + terr_x

area_final = x_area_final * y_area_final
