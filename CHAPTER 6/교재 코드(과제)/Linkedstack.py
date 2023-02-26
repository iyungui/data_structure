# 노드 클래스
class Node:
    def __init__(self, elem, link=None):    # 생성자. 디폴트 인수 사용
        self.data = elem        # 데이터 멤버 생성 및 초기화
        self.link = link        # 링크 생성 및 초기화

# 연결된 스택 클래스(6.2절)
class LinkedStack:
    def __init__( self ):       # 생성자
        self.top = None         # top 생성 및 초기화

    def isEmpty( self ): return self.top == None      # 공백상태 검사
    def clear( self ): self.top = None      # 스택 초기화

    def push( self, item ):      # 연결된 스택의 삽입연산
        n = Node(item, self.top)  # 삽입할 데이터로 새로운 노드 n을 생성하고, n의 링크가 시작노드인 top을 가리키도록 함
        self.top = n            # top이 n을 가리키도록 함

    def pop( self ):        # 연결된 스택의 삭제연산: 상단항목의 데이터를 꺼내서 반환
        if not self.isEmpty():  # 공백이 아니면
            n = self.top        # n이 시작노드를 가리키도록 함
            self.top = n.link   # top이 다음노드를 가리키도록 함
            return n.data       # n이 가리키는 노드의 데이터를 반환함

    def peek( self ):       # 연결된 스택의 peek 연산, 시작 노드의 데이터를 반환
        if not self.isEmpty():  # 공백이 아니면
                return self.top.data    # 시작 항목의 데이터 반환

    def size( self ):       # 스택의 항목 수 계산: 맨 마지막 노드까지 움직여서 세보기
        node = self.top     # 시작 노드는 top
        count = 0
        while not node == None: # node가 None이 아닐 때 까지 (마지막 노드까지)
            node = node.link    # 다음 노드로 이동
            count += 1          # count 증가
        return count            # count 반환

    def display( self, msg = 'LinkedStack:'):   # 스택의 항목 출력
        print(msg, end='')      # 메시지를 먼저 출력
        node = self.top     # 시작노드 node가 top을 가리키도록 함
        while not node == None: # node가 None이 아닐 때 까지 (마지막 노드까지)
            print(node.data, end='')    # node의 데이터 멤버 출력
            node = node.link    # 다음 노드로 이동
        print()

# 테스트 코드(4장 참고)----------------------------------
odd = LinkedStack()     # 홀수 저장을 위한 스택
even = LinkedStack()    # 짝수 저장을 위한 스택

for i in range(10):
    if i%2 == 0: even.push(i)   # 짝수는 even에 push
    else: odd.push(i)              # 홀수는 odd에 push

print('스택 even push 5회', end=('  -  '))
even.display()
print('스택 odd push 5회', end=('  -  '))
odd.display()
print('스택 even     peek', end=('  -  '))
print(even.peek())
print('스택 odd     peek', end=('  -  '))
print(odd.peek())
for _ in range(2): even.pop()
for _ in range(3): odd.pop()
print('스택 even pop 2회', end=('  -  '))
even.display()
print('스택 odd pop 2회', end=('  -  '))
odd.display()
#---------------------------------------------------




    




    






