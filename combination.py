import itertools
# import numpy as np
import psutil
import time
from estresse import bench

numbers = list(range(0, psutil.cpu_count()))
group_size = int(input("Enter the group size: "))
combinations = list(itertools.combinations(numbers, group_size))

bench( combinations)
# for combination in combinations:
#     print(combination)

