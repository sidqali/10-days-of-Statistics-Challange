

## Mean, Median and Mode
"""

import numpy as np
from scipy import stats

#Take input from user, It is the size of the N
size = int(input())
#Take numbers from user as input
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
