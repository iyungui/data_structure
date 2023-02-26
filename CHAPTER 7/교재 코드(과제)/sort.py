# 선택 정렬
def selection_sort(A):
    n = len(A)  # n: 리스트 A의 길이
    for i in range(n-1):  # [outer loop]: (0~n-2) n-1 회 비교, 즉 정렬이 다 될 때 까지 반복
        least = i
        for j in range(i+1, n):  # [inner loop]: i+1,...,n-1
            # (1~n-1)+(2~n-1)+...+1(n-1~n-1)=n(n-1)/2 => O(n^2)
            if (A[j]<A[least]):  # 비교 연산
                least = j  # 최소 항목 변경 (정렬이 된 리스트로)
        A[i], A[least] = A[least], A[i]  # 배열 항목 교환(튜플)
        printStep(A, i+1)  # 중간과정 출력용 문장

# 중간 과정 출력용 함수
def printStep(arr, val):
    print(" Step %2d = " %val, end='')
    print(arr)

# 테스트 코드
data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
selection_sort(data)
print("Selection :", data)
#-------------------------------
print()

# 삽입 정렬
def insertion_sort(A):
    n = len(A)
    for i in range(1, n):  # [outer loop]: (1~n-1) n-1회 비교
        # 첫 번째 원소 앞에는 어떤 원소도 갖고 있지 않기 때문에, 두 번째 위치부터 탐색을 시작
        key = A[i]  # key에 임시로 해당 위치 값을 저장하고,
        j = i-1  # j에는 해당 위치의 이전 위치를 저장
        while j>=0 and A[j] > key:  # [inner loop]: 이전 위치를 가리키는 j가 음수가 되지 않고, 이전 위치의 값이 key 값 보다 크다면,
            A[j + 1] = A[j]  # 항목 이동(뒤로 한칸)
            j -= 1  # j를 더 이전 위치를 가리키게 한다
        A[j + 1] = key  # 항목 삽입
        printStep(A, i)
        # while 반복문이 끝난 후 j는 현재 key값보다 작은 값들 중 제일 큰 값의 위치를 가리키게 된다.
        # 따라서 (j+1)에 key값을 삽입한다.

# 테스트 코드
data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
insertion_sort(data)
print("Insertion :", data)
#-------------------------------
print()


# 버블 정렬
def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):  # 외부 루프: n-1, n-2, ..., 2, 1
        bChanged = False
        for j in range(i):  # 내부 루프: 0, 1, ..., i-1
            if (A[j]>A[j+1]): 
                A[j], A[j+1] = A[j+1], A[j]  # 교환(swap)
                bChanged = True  # 교환이 발생했음
        if not bChanged:  
            break  # 교환이 없으면 종료
        printStep(A, n-i)

# 테스트 코드
data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
bubble_sort(data)
print("Bubble :", data)
#-------------------------------