class TNode:        # 이진트리를 위한 노드 클래스
    def __init__ (self, data, left, right):     # 생성자
        self.data = data        # 노드의 데이터
        self.left = left        # 왼쪽 자식을 위한 링크
        self.right = right      # 오른쪽 자식을 위한 링크

MAX_QSIZE = 10
class CircularQueue :
    def __init__( self ) :		
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE	

    def isEmpty( self ) : return self.front == self.rear # 큐가 비어있으면 True를 아니면 False를 반환한다
    def isFull( self ) : return self.front == (self.rear+1)%MAX_QSIZE # 큐가 가득찼는지 검사
    def clear( self ) : self.front = self.rear # 큐를 공백상태로 만든다.

    def enqueue( self, item ): # item을 큐의 맨 뒤에 추가
        if not self.isFull():			            # 큐가 가득차 있지 않다면
            self.rear = (self.rear+1)% MAX_QSIZE	
            self.items[self.rear] = item		     # 

    def dequeue( self ):  # 큐의 맨 앞에 있는 항목을 꺼내 반환
        if not self.isEmpty():			            # 큐가 비어있지 않다면
            self.front = (self.front+1)% MAX_QSIZE	
            return self.items[self.front] # 	        

    def peek( self ): # 큐의 맨 앞에 있는 항목을 삭제하지 않고 반환한다
        if not self.isEmpty(): # 큐가 비어있지 않다면
            return self.items[(self.front + 1) % MAX_QSIZE] #dequeue 다음이 peek

    def size( self ) : # 큐의 모든 항목들의 개수를 반환
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display( self ):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
						    + self.items[0:self.rear+1]		#
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)


# 트리 순회: 트리에 속하는 모든 노드를 방문하여 노드의 데이터 처리
def preorder(n):        # 전위 순회 향수 - 순환 이용
    if n is not None:
        print(n.data, end = ' ')    # 먼저 루트 노드 처리 (화면 출력)
        preorder(n.left)            # 왼쪽 서브트리 처리
        preorder(n.right)           # 오른쪽 서브트리 처리

def inorder(n):         # 중위 순회 함수
    if n is not None:
        inorder(n.left)             # 왼쪽 서브트리 처리
        print(n.data, end = ' ')    # 루트노드 처리 (화면 출력)
        inorder(n.right)            # 오른쪽 서브트리 처리

def postorder(n):       # 후위 손회 함수
    if n is not None:
        postorder(n.left)           # 왼쪽 서브트리 처리
        postorder(n.right)          # 오른쪽 서브트리 처리
        print(n.data, end = ' ')    # 루트노드 처리 (화면 출력)
        
def levelorder(n):      # 레벨 순회 함수 ( 큐 사용 ): 레벨 순회는 큐에서 노드를 꺼내 방문하고, 그 자식들을 큐에 삽입한다. 큐가 공백상태가 될 때까지. 순환은 사용되지 않는다.
    queue = CircularQueue() # 큐 객체 초기화
    queue.enqueue(root)     # 최초의 큐에는 루트 노드만 들어있음
    while not queue.isEmpty():  # 큐가 공백상태가 아닌 동안,
        n = queue.dequeue()     # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data, end = ' ')    # 먼저 노드의 정보를 출력
            queue.enqueue(n.left)       # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)      # n의 오른쪽 자식 노드를 큐에 삽입

def count_node(n):          # 순환을 이용해 트리의 노드 수를 계산하는 함수
    if n is None:           # n이 None이면 공백 트리이므로 0 반환
        return 0
    else:                   # 좌우 서브트리의 노드 수 + 1 반환 ( 순환 이용 )
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):          # 단말 노드(리프 노드) 개수 구하기
    if n is None:           # 공백 트리 -> 0 반환
        return 0
    elif n.left is None and n.right is None:    # 단말노드 -> 1 반환
        return 1
    else:                                       # 비단말 노드: 좌우 서브트리의 결과 합을 반환
        return count_leaf(n.left) + count_leaf(n.right) 

def calc_height(n):         # 트리의 높이 구하기
    if n is None:           # 공백 트리는 0 반환
        return 0
    hLeft = calc_height(n.left) # 왼쪽 트리의 높이 설정 . 마찬가지로 순환 함수 사용
    hRight = calc_height(n.right) # 오른쪽 트리의 높이 설정

    if (hLeft > hRight):        # 왼쪽 서브트리의 높이가 더 크다면 그 트리의 높이에 1(루트 노드) 더하여 반환
        return hLeft + 1
    else:
        return hRight + 1


# 테스트 코드 1)이진트리 연산 프로그램(전위 중위 후위 순회 결과 출력 및 트리의 노드 수, 리프 노드의 수, 트리의 높이 출력) ---------------
d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('\n  In_order : ', end='')
inorder(root)
print('\n  Pre_order : ', end='')
preorder(root)
print('\n  Post-order : ', end='')
postorder(root)
print('\nLevel-order : ', end='')
levelorder(root)
print()

print(" 노드의 개수 = %d개" % count_node(root))
print(" 단말의 개수 = %d개" % count_leaf(root))
print(" 트리의 높이 = %d" % calc_height(root))



