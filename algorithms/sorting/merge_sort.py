import math


def merge(arrB, arrC):
    arrD = [0 for _ in range(len(arrB)+len(arrC))]
    i,j = 0,0
    arrB.append(math.inf)
    arrC.append(math.inf)
    for k in range(len(arrD)):
        if arrB[i] < arrC[j]:
            arrD[k] = arrB[i]
            i += 1
        else:
            arrD[k] = arrC[j]
            j += 1
    return arrD

# sorts arrA[m], arrA[m+1], ..., arrA[n-1] returning result in arrD of size n-m
def merge_sort(arrA, start, end):
    if end-start==1:
        return [arrA[start]]
    else:
        mid_point = int((start + end) // 2)  # roughly halving arrays
        arrB = merge_sort(arrA, start, mid_point)
        arrC = merge_sort(arrA, mid_point, end)
        arrD = merge(arrB, arrC)
        return arrD

def merge_sort_all(arr):
    return merge_sort(arr, 0, len(arr))

if __name__ == '__main__':
    print(merge_sort_all([5,23,3,14,2]))
    print(merge_sort_all([5, 22, 23, 4, 6, 1, 3, 6, 23, 17, 14, 2]))
