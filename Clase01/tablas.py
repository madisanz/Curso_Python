# Name: Margarita Sanchez
# Update Tablas

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
contadorMeses = 0

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    contadorMeses += 1
    if contadorMeses  >= pago_extra_mes_comienzo and contadorMeses <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra  
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    print(contadorMeses, round(total_pagado, 2), round(saldo, 2))

print('Total pagado', round(total_pagado, 2))
print("Meses:", contadorMeses)



