import matplotlib.pyplot as plt
import numpy as np
import timeit
import math
import random

plt.rcParams['figure.figsize'] = [10, 6] # set size of plot

ns = np.linspace(10, 10_000, 50, dtype=int)
ts = [timeit.timeit('sum(range({}))'.format(n), number=100) for n in ns]
plt.plot(ns, ts, 'or')
plt.show()