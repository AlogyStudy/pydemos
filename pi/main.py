from random import random
import math
import time

DARTR = 2000000 # 抛洒点越多越精确。
hits = 0

time.clock()

for i in range(1, DARTR):
    x, y = random(), random()
    dist = math.sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / DARTR)

print('pi：%s' % pi)
print('run time: %-5.5ss' % time.clock())
