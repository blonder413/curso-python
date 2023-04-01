from decimal import Decimal
import math

a = float('NaN')    # No sensible a minúsulas
a = Decimal('NaN')  # No sensible a minúsulas
a = math.nan

print(f'NaN? {math.isnan(a)}')
