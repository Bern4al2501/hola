porcentaje_interes = 0.03
porcentaje_perder = 0.02
def CDT (usuario: str, capital: int, tiempo: int) :
    if tiempo > 2:
        valor_intereses = capital * porcentaje_interes * tiempo / 12
        valor_total = valor_intereses + capital
        return ("Para el usuario {} La cantidad de dinero a recibir, "
                "segun el monto inicial {} para un tiempo de {} "
                "meses es: {}".format(usuario, capital, tiempo, valor_total))
    elif tiempo <= 2:
        valor_perder = capital * porcentaje_perder
        valor_total_perder = capital - valor_perder
        return ("Para el usuario {} La cantidad de dinero a recibir,"
                "segun el monto inicial {}"
                "para un tiempo de {} meses es: {}".format(usuario, capital, tiempo, valor_total_perder))

print(CDT("AB123", 300000, 2))