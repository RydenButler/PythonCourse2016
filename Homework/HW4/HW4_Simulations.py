import timeit
from HW4_Ryden import *

Times = []
for i in range(1, 101):

	randomize = '''
import random
from HW4_Ryden import Insertion_Sort

random.seed(82565)
sort_this = [int(random.random()) for j in range(%d)]
Insertion = Insertion_Sort
''' % i

	Times.append(timeit.Timer('test = sort_this; Insertion(test)', setup = randomize).repeat(100, 1000))

import numpy
Avg_Times = []
for k in Times:
	Avg_Times.append(numpy.mean(k))

Min_Times = []
for l in Times:
	Min_Times.append(min(l))

Max_Times = []
for m in Times:
	Max_Times.append(max(m))

Merge_Times = []
for i in range(1, 101):

	randomize = '''
import random
from HW4_Ryden import Merge_Sort

random.seed(82565)
sort_this = [int(random.random()) for j in range(%d)]
Merge = Merge_Sort
''' % i

	Merge_Times.append(timeit.Timer('test = sort_this; Merge(test)', setup = randomize).repeat(100, 1000))

import numpy
Avg_Merge_Times = []
for k in Merge_Times:
	Avg_Merge_Times.append(numpy.mean(k))

Min_Merge_Times = []
for l in Merge_Times:
	Min_Merge_Times.append(min(l))

Max_Merge_Times = []
for m in Merge_Times:
	Max_Merge_Times.append(max(m))

import matplotlib.pyplot as plt
plt.plot(range(1,101), Avg_Times, 'r--', range(1,101), Avg_Merge_Times, 'b-.')
plt.ylabel('Run time (seconds)')
plt.xlabel('Number of sorted values')
plt.annotate('Insertion Sort: O(n^2)', xy=(20, 0.03), xytext=(20, 0.03),
            )
plt.annotate('Merge Sort: O(n log(n))', xy=(35, .5), xytext=(35, .5),
            )
plt.show()