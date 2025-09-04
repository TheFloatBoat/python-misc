import math

smallestDifference = 1000 #arbitrarily large number for comparisons
bestTop = 0
bestBottom = 0
divisibleBy = 1

for top in range(0, 1000, divisibleBy):
  bottom = round(top/math.pi)
  if bottom != 0:#keep seperate to prevent division by 0 in check  
    if abs(top/bottom - math.pi) < smallestDifference:
      smallestDifference = abs(top/bottom - math.pi)
      bestTop = top
      bestBottom = bottom
print(f"Best top number is {bestTop}, best bottom number is {bestBottom}. Smallest difference was {smallestDifference}")
