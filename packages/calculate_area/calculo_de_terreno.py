from sympy import *


class Rectangle:
    def calculate_area_rectangle(self, xExtra, yExtra, areaLote):
        x = symbols('x')

        al = (xExtra + areaLote / x) * (yExtra + x)

        d_al = diff(al, x)

        pc = solve(Eq(d_al, 0), x)

        for n in pc:
            if n > 0:
                pc = n

        area_interna_y = areaLote / pc

        x_area_final = pc + yExtra
        y_area_final = area_interna_y + xExtra

        area_final = round(x_area_final * y_area_final)
        print(N(area_final))
        return [x_area_final, y_area_final, area_final]

    def calculate_cost(self, area_final, custo):
        return custo * area_final


class Elipse:
    def calculate_area_elipse(self, xExtra, yExtra, areaLote):
        r = symbols('r')

        al = (xExtra + 2 * (areaLote / (pi * r))) * (yExtra + 2 * r)

        d_al = diff(al, r)

        pc = solve(Eq(d_al, 0), r)

        for n in pc:
            if n > 0:
                pc = n

        area_interna_y = areaLote / pc
        x_area_final = pc + yExtra
        y_area_final = area_interna_y + xExtra

        area_final = round(x_area_final * y_area_final)
        print(N(area_final))
        return [x_area_final, y_area_final, area_final]

    def calculate_cost(self, area_final, custo):
        return custo * area_final