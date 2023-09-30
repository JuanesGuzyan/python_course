import math
from decimal import Decimal

# NaN - Not a Number
# no es sensible a mayusculas / minusculas
# es un tipo de dato numerico indefinido
a = float('NaN')
print(a)
print(f'Es NaN?: {math.isnan(a)}')

a = Decimal('NaN')
print(a)
print(f'Es NaN?: {math.isnan(a)}')
