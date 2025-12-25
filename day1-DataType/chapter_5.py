import sys
from fractions import Fraction
from decimal import Decimal
item= 95.5
citem=95.49 

print(f"IdealTemp {item}")
print(f"IdealTemp {citem}")
print(f"DiffrentTemp {citem-item}")
print(sys.float_info)