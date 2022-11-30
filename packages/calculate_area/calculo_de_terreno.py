from sympy import *


class Rectangle:
    def calculate_area(self, terreno_x, terreno_y, tamanho_area):
        x = symbols('x')
        al = (terreno_x + tamanho_area / x) * (terreno_y + x)

        d_al = diff(al, x)

        pc = solve(Eq(d_al, 0), x)

        for n in pc:
            if n > 0:
                pc = n

        area_interna_y = tamanho_area / pc

        x_area_final = pc + terreno_y
        y_area_final = area_interna_y + terreno_y

        area_final = x_area_final * y_area_final
        return [area_final,x_area_final,y_area_final]
