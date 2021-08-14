import math
ab, bc = int(input()), int(input())
# mbc = int(math.degrees(math.radians(45)*((ab**2)/(bc**2))))
# mbc = int(45*((ab**2)/(bc**2)))
mbc = round(math.degrees(math.atan(ab/bc)))
deg_sign = u"\N{DEGREE SIGN}"
print(f"{mbc}{deg_sign}")