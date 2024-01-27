import time, random
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [10, 6] # set size of plot
    
def time_delta(time_start):
    return (time.time() - time_start) * (10**6)

def array_length(arr): # O(1)
    time_data = []
    time_start = time.time()
    # print("{:,}".format(time_delta(time_start)))
    
    length = len(arr); time_data.append(time_delta(time_start))
    return time_data

def search(arr, target=None): # O(n)
    time_data = []
    time_start = time.time()
    
    for i in range(len(arr)):
        print(i, "{:,}".format(time_delta(time_start)))
        time_data.append(time_delta(time_start))
        if arr[i] == target:
            break
        
    return time_data

def insertion_sort(_arr): # O(n^2) ref: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
    arr = _arr.copy()
    time_data = []
    time_start = time.time()
    
    for i in range(1, len(arr)):
        print(i, "{:,}".format(time_delta(time_start)))
        time_data.append(time_delta(time_start))
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
            
    return time_data


def mergeSort(_arr, time_start): # O(nlogn) ref: https://www.programiz.com/dsa/merge-sort#google_vignette
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
    
    time_data.append(time_delta(time_start))
    return time_data

# def nlogn(n):
#     time_start = time.time()
#     time_data = []
#     for i in range(len(n)):
#         if time_delta(time_start) == 0:
#             time_data.append(0)
#         else:
#             time_data.append(time_delta(time_start) * math.log10(time_delta(time_start)))
#     return time_data

if __name__ == "__main__":
    
    size = 10**4
    example_data = [random.randint(1,500) for _ in range(size)]
    
    time_data_al = array_length(example_data)
    time_data_s = search(example_data)      
    time_data_is = insertion_sort(example_data)
    time_data_ms = mergeSort(example_data, time_start=time.time()); time_data_ms.sort()
    # time_data_ms = nlogn(example_data)

    ax = plt.axes()

    plt.setp(ax.spines.values(), color="black")
    ax.set_facecolor("white")

    # plt.title("brabrabra")
    plt.xlabel("n")
    plt.ylabel("time(ms)")

    plt.plot(np.linspace(time_data_al[0],time_data_al[0],len(example_data)), label="O(1)")
    plt.plot(time_data_s, label="O(n)")
    plt.plot(time_data_is, label="O(n^2)")
    plt.plot(time_data_ms, label="O(nlogn)")
    
    plt.xlim(left=1, right=size)
    plt.legend()
    plt.show()