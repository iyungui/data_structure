

#P8_7 ----------------
def isMinHeapRecur(A, id) :
    n = len(A)-1
    l = id * 2
    r = id * 2 + 1
    if id >= n: return True
# True or False 중에서 선택하세요.
    if l <= n and A[l] < A[id] : return False
    if r <= n and A[r] < A[id] : return False

    if not isMinHeapRecur(A, l) : return False
    if not isMinHeapRecur(A, r) : return False
    return True

def isMaxHeapRecur(A, id) :
    n = len(A)-1
    l = id * 2
    r = id * 2 + 1
    if id >= n : return True

    if l <= n and A[l] > A[id] : return False
    if r <= n and A[r] > A[id] : return False

    if not isMaxHeapRecur(A, l) : return False
    if not isMaxHeapRecur(A, r) : return False
    return True


#P8_8 ----------------
def isMinHeapIter(A) :
    n = len(A)-1
    for i in range(1, n) :
        l = i * 2
        r = i * 2 + 1
        if l <= n and A[l] < A[i] : return False
        if r <= n and A[r] < A[i] : return False
    return True


def isMaxHeapIter(A) :
    n = len(A)-1
    for i in range(1, n) :
        l = i * 2
        r = i * 2 + 1
        if l <= n and A[l] > A[i] : return False
        if r <= n and A[r] > A[i] : return False
    return True



minHeap = [-1, 1, 4, 2, 7, 5, 3, 3, 7, 8, 9]
maxHeap = [-1, 9, 7, 6, 5, 4, 3, 2, 2, 1, 3]
noHeap = [-1, 9, 7, 2, 5, 4, 3, 2, 2, 1, 3]

print(minHeap)
print("isMinHeapRecur:", isMinHeapRecur(minHeap, 1))
print("isMaxHeapRecur:", isMaxHeapRecur(minHeap, 1))
print("isMinHeapIter:", isMinHeapIter(minHeap))
print("isMaxHeapIter:", isMaxHeapIter(minHeap))

print(maxHeap)
print("isMinHeapRecur:", isMinHeapRecur(maxHeap, 1))
print("isMaxHeapRecur:", isMaxHeapRecur(maxHeap, 1))
print("isMinHeapIter:", isMinHeapIter(maxHeap))
print("isMaxHeapIter:", isMaxHeapIter(maxHeap))

print(noHeap)
print("isMinHeapRecur:", isMinHeapRecur(noHeap, 1))
print("isMaxHeapRecur:", isMaxHeapRecur(noHeap, 1))
print("isMinHeapIter:", isMinHeapIter(noHeap))
print("isMaxHeapIter:", isMaxHeapIter(noHeap))
