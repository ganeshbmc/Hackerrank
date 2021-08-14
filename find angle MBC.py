import math
ab, bc = int(input()), int(input())
mbc = round(math.degrees(math.atan(ab/bc)))
deg_sign = u"\N{DEGREE SIGN}"
print(f"{mbc}{deg_sign}")

# This is the first time I used the DEGREE SIGN. See line 4 above.