# Example7.py
# Calcula la distancia entre dos puntos en un plano cartesiano
# Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

import math
    
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
    
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The distance is", distance)
