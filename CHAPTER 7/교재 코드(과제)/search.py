# # 순차탐색
# def sequential_search(A, key, low, high):
#     for i in range(low, high+1):
#         if A[i].key == key:
#             return i
#     return None

# 이진 탐색 순환 구조
def binary_search(A, key, low, high):
    if (low <= high):               # 항목들이 남아 있으면 (종료 조건)
        middle = (low + high) // 2  # 중앙에 있는 값 조사. 이 때 정수나눗셈 //
        if key == A[middle].key:    # 탐색 성공
            return middle
        elif (key < A[middle].key): # 왼쪽 부분 리스트 탐색
            return binary_search(A, key, low, middle - 1)
        else:                       # 오른쪽 부분 리스트 탐색
            return binary_search(A, key, middle + 1, high)
        return None                 # 탐색 실패


# 이진 탐색 반복 구조
def binary_search_iter(A, key, low, high):
    while (low <= high):            # 항목들이 남아 있으면 (종료 조건)
        middle = (low + high) // 2
        if key == A[middle].key:    # 탐색 성공
            return middle
        elif (key > A[middle].key): # key가 middle의 값보다 크면
            low = middle + 1        # middle + 1 ~ high 사이 검색
        else:                       # key가 middle의 값보다 작으면
            high = middle - 1       # low ~ middle - 1 사이 검색
    return None


def interpolation_search(A, key, low, high):  # 보간 탐색 순환
    if (low <= high):               # 항목들이 남아 있으면 (종료 조건)
        middle = int(low + (high-low) * (key-A[low]) / (A[high]-A[low]))        # 찾는 값과 위치가 비례한다고 가정.
        if key == A[middle]:
            return middle
        elif (key<A[middle]):
            return binary_search(A, key, low, middle - 1)
        else:
            return binary_search(A, key, middle + 1, high)
    return None

def interpolation_search_iter(A, key, low, high):  # 보간 탐색 반복
    while (low <= high):
        middle = int(low + (high-low) * (key-A[low]) / (A[high]-A[low]))
        if key == A[middle]:
            return middle
        elif (key > A[middle]):
            low = middle + 1
        else:
            high = middle - 1
    return None
