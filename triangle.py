#trying to find a right angle triangle with sides a, b, c where a+b+c=1000
#c=1000-a-b, so a^2+b^2=(1000-a-b)^2 or 1000000-1000a-1000b-1000a+a^2+ab-1000b+ab+b^2
#this can be simplified to a^2+b^2=1000000-2000a-2000b+a^2+b^2+2ab
#or 0=1000000-2000a-2000b+2ab OR 2000(a+b)=1000000+2ab OR a+b=500+ab/1000
import math
for x in range(1,1000):
    for y in range(1,1000):
        if x+y==500+x*y/1000:
            print(f"{x}, {y}, {math.sqrt(x**2+y**2)}")
