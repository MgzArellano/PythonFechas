# Trabajando con fechas resulta complicado sobre
# Toodo si vamos a hacer comparaciones por ejemplo de fechas manejando a la vez timezones
# Seguí en este programa un tutorial (enlace abajo) para aprender a manejar las fechas

# https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python

#datetime.datetime
#datetime.timedelta
#datetime.timezone  ( para python 3.2 + )

# importamos el módulo datetime que ya incluye las clases datetime, timedelta, timezone  ... o podemos importarlas individualmente
# por ejemplo:   from datetime import timedelta

import datetime

ahora = datetime.datetime.now()
# imprime la fecha/timing actual en formato como el siguiente ejemplo: 2018-02-27 16:55:10.775528
print(ahora)

## importando a datetime mi fecha de cumpleaños
mi_cumple = datetime.datetime(1984, 9, 7, 0, 0, 0, 0)
# imprime mi fecha de cumpleaños en formato datetime python:  1984-09-07 00:00:00
print(mi_cumple)

## Dando un formato personalizado
mi_cumple2 = datetime.datetime(1984, 9, 7, 9, 30)
# Imprimiendo en el formato siguiente: September 07, 1984
print(mi_cumple2.strftime('%B %d, %Y'))

# Imprimiendo como: 1984/09/07
print(mi_cumple2.strftime('%Y/%m/%d'))

# Imprimiendo como: 07/09/1984
print(mi_cumple2.strftime('%d/%m/%Y'))

# Imprimiendo como:
print('%s')