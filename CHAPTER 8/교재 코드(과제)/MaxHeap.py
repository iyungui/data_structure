# 최대 힙 클래스
class MaxHeap:
    def __init__(self):     # 배열 구조인 파이썬의 리스트 사용, 이 때 0번 인덱스 사용x
        self.heap = []
        self.heap.append(0)
        
    def size(self): return len(self.heap) - 1       # 힙의 크기
    def isEmpty(self): return self.size() == 0      # 공백 검사
    def Parent(self, i):    return self.heap[i//2]  # 부모노드 반환
    def Left(self, i): return self.heap[i*2]        # 왼쪽 자식 반환
    def Right(self, i): return self.heap[i*2+1]     # 오른쪽 자식 반환
    def display(self, msg = '힙 트리: '):
        print(msg, self.heap[1:])                   # 파이썬 리스트의 슬라이싱 이용 (인덱스 1부터.)

    def insert(self, n):            # 힙의 삽입 연산: 업힙 과정에서 두 노드 바꿀 필요 없음, 부모 노드만 끌어내리고 삽입할 노드를 마지막에 처리
        self.heap.append(n)         # 맨 마지막 노드로 일단 삽입 (신입 말단 사원->승진)
        i = self.size()             # 노드 n의 마지막 위치. 인덱스
        while (i != 1 and n > self.Parent(i)):      # 삽입노드가 부모노드 보다 크다면 
            self.heap[i] = self.Parent(i)           # 부모를 끌어내림 (반복)
            i = i // 2          # i를 부모의 인덱스 ( i //2 ) 로 변경
        self.heap[i] = n        # 마지막 위치에 n 삽입

    def delete(self):                       # 힙의 삭제 연산: 루트 노드 반환.  큰 자식 노드만 계속 올리고 마지막 노드는 한번만
        parent = 1
        child = 2 # 왼쪽노드가 기본
        if not self.isEmpty():              # 공백 아니라면
            hroot = self.heap[1]            # 삭제할 루트노드를 복사해 둠
            last = self.heap[self.size()]   # 마지막 노드 (말단 사원 -> 사장 -> 순차적 강등)
            while (child <= self.size()):   # 마지막 노드 이전까지
                # 만약 오른쪽 노드가 더 크면 child를 1 증가 ( 기본은 왼쪽 노드 )
                if child<self.size() and self.Left(parent)<self.Right(parent):
                    child += 1
                if last >= self.heap[child]:    # 두 자식 노드 중 더 큰 자식이 더 작으면
                    break                   # 삽입 위치 찾음. down heap 종료
                self.heap[parent] = self.heap[child]    # 그게 아니면 down heap 계속
                parent = child
                child *= 2

            self.heap[parent] = last        # 맨 마지막 노드를 parent 위치에 복사
            self.heap.pop(-1)               # 맨 마지막 노드 삭제
            return hroot                    # 저장해두었던 루트를 반환
            
# 테스트 코드
heap = MaxHeap()                    
data = [2, 5, 4, 8, 9, 3, 7, 3]    
print("[삽입 연산]: ", data)
for elem in data :                  
    heap.insert(elem)              # 최대 힙의 삽입 연산
heap.display('[ 삽입 후 ]: ')      
heap.delete()                       # 최대 힙의 삭제 연산   
heap.display('[ 삭제 후 ]: ')      
heap.delete()                      
heap.display('[ 삭제 후 ]: ')





