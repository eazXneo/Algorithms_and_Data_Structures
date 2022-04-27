
def insert_sort(arr):  # O(n**2)
    arr_length = len(arr)
    for i in range(1,arr_length):
        curr = arr[i]
        j = i-1
        while(j>=0 and arr[j]>curr):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr
    return arr

def insert_sort_2(arr):  # O(n**2)
    n = len(arr)
    for i in range(1, n):  # O(n) iterations
        t = arr[i]
        for j in range(i - 1, -2, -1):  # O(n) iterations
            if arr[j] < t: break
            arr[j + 1] = arr[j]
        arr[j+1] = t
    return arr

"""
mark first element as sorted

for each unsorted element X

  'extract' the element X

  for j = lastSortedIndex down to 0

    if current element j > X

      move sorted element to the right by 1

    break loop and insert X here
"""

if __name__ == '__main__':
    print(insert_sort([5,23,3,14,2]))
    print(insert_sort_2([5, 23, 3, 14, 2]))
    print(insert_sort([5,23,3,14,2])==insert_sort_2([5, 23, 3, 14, 2]))
