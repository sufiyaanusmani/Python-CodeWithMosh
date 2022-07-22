# does not stores value, spits out value in every iteration, saves memory
from sys import getsizeof
values = (x*2 for x in range(1000))
print(getsizeof(values))

values = (x*2 for x in range(1000000))
print(getsizeof(values))
