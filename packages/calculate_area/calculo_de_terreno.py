from sympy import *


class Rectangle:
    @staticmethod
    def calculate_area_rectangle(x_extra, y_extra, area_lote):
        x = symbols('x')

        al = (x_extra + area_lote / x) * (y_extra + x)

        d_al = diff(al, x)

        pc = solve(Eq(d_al, 0), x)

        for n in pc:
            if n > 0:
                pc = n

        area_interna_y = area_lote / pc

        x_area_final = pc + y_extra
        y_area_final = area_interna_y + x_extra

        area_final = round(x_area_final * y_area_final)
        print(N(area_final))
        return [x_area_final, y_area_final, area_final]

    @staticmethod
    def calculate_cost(area_final, custo):
        return custo * area_final


class Elipse:
    @staticmethod
    def calculate_area_elipse(x_extra, y_extra, area_lote):
        r = symbols('r')

        al = (x_extra + 2 * (area_lote / (pi * r))) * (y_extra + 2 * r)

        d_al = diff(al, r)

        pc = solve(Eq(d_al, 0), r)

        for n in pc:
            if n > 0:
                pc = n

        area_interna_y = area_lote / pc
        x_area_final = pc + y_extra
        y_area_final = area_interna_y + x_extra

        area_final = round(x_area_final * y_area_final)
        print(N(area_final))
        return [x_area_final, y_area_final, area_final]

    @staticmethod
    def calculate_cost(area_final, custo):
        return custo * area_final
