# adelantos.py


# Ejercicio 1.8


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mesAdelanto = 12
contadorMeses = 0

while saldo > 0:
    if mesAdelanto >= 1:
        saldo = saldo * (1+tasa/12) - pago_mensual - 1000
        total_pagado = total_pagado + pago_mensual + 1000  
        mesAdelanto -= 1
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    contadorMeses += 1

print('El total pagado', round(total_pagado, 2), "en un total de ", contadorMeses, "meses")

# Output:
# "Total pagado 929965.62 en un total de  342 meses"