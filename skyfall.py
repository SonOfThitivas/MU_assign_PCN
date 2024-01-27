import time, timeit, math, random
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [10, 6] # set size of plot
example_data = [random.randint(1,500) for _ in range(10**9)]
    
def time_diff(time_start):
    return (time.time() - time_start) * (10**6)

def array_length(arr): # O(1)
    time_data = []
    time_start = time.time()
    # print("{:,}".format(time_diff(time_start)))
    
    length = len(arr); time_data.append(time_diff(time_start))
    return time_data

def search(arr, target=None): # O(n)
    time_data = []
    time_start = time.time()
    
    for i in range(len(arr)):
        print(i, "{:,}".format(time_diff(time_start)))
        time_data.append(time_diff(time_start))
        if arr[i] == target:
            break
        
    return time_data

def insertion_sort(_arr): # O(n^2)
    arr = _arr.copy()
    time_data = []
    time_start = time.time()
    
    for i in range(1, len(arr)):
        print(i, "{:,}".format(time_diff(time_start)))
        time_data.append(time_diff(time_start))
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
            
    return time_data

def mergeSort(_arr, time_start):
    arr = _arr.copy()
    time_data = []
    
    if len(arr) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(arr)//2
        L = arr[:r]
        M = arr[r:]

        # Sort the two halves
        tl = mergeSort(L, time_start)
        for o in tl:
            time_data.append(o)
        tr = mergeSort(M, time_start)
        for p in tr:
            time_data.append(p)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1
    
    time_data.append(time_diff(time_start))
    return time_data

# time_data_al = array_length(example_data)
# time_data_s = search(example_data)      
# time_data_is = insertion_sort(example_data)
time_data_ms = mergeSort(example_data, time_start=time.time())
time_data_ms.sort()

for k in time_data_ms:
    print(k)

ax = plt.axes()

plt.setp(ax.spines.values(), color="black")
ax.set_facecolor("white")

plt.title("brabrabra")
plt.xlabel("n")
plt.ylabel("time")

# plt.xlim(right=10**4)

# plt.xticks(range(1,10**5+1))
# plt.yticks(range(1,10**3+1))
# plt.axis((0,10**4,0,10**6))

# print(np.array(time_data))
# print(np.linspace(min(time_data), max(time_data), num=len(example_data)))
# plt.plot(np.linspace(1,1,len(example_data)), label="O(1)")
# plt.plot(time_data_s, label="O(n)")
# plt.plot(time_data_is, label="O(n^2)")
plt.plot(time_data_ms, label="O(nlogn)")
# plt.plot(np.linspace(min(time_data), max(time_data), num=len(example_data)))
plt.legend()
plt.show()

# def insertion_sort(lst):
#     for i in range(1, len(lst)):
#         for j in range(i, 0, -1):
#             if lst[j-1] > lst[j]:
#                 lst[j-1], lst[j] = lst[j], lst[j-1]
#             else:
#                 break
            
#     return lst
# # 15 values
# ns = np.linspace(100, 2000, 15, dtype=int)

# ns = insertion_sort(ns)
# ns = np.array(ns)
# print(ns)
# ts = [timeit.timeit('insertion_sort(lst)',
#                     setup='lst=list(range({})); random.shuffle(lst)'.format(n),
#                     globals=globals(),
#                     number=1)
#         for n in ns]
# plt.plot(ns, ts, 'or');
# degree = 4
# coeffs = np.polyfit(ns, ts, degree)
# p = np.poly1d(coeffs)
# plt.plot(ns, [p(n) for n in ns], '-r')

# plt.show()