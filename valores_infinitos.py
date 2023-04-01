from decimal import Decimal
import math

infinito_positivo = float('inf')
infinito_negativo = float('-inf')
infinito_positivo = math.inf
infinito_negativo = -math.inf
infinito_positivo = Decimal('Infinity')
infinito_negativo = Decimal('-Infinity')
print(infinito_negativo)
print(f'es infinito? {math.isinf(infinito_positivo)}')
