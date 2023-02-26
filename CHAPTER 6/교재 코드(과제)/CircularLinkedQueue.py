# 노드 클래스
class Node:
    def __init__(self, elem, link=None):    # 생성자. 디폴트 인수 사용
        self.data = elem        # 데이터 멤버 생성 및 초기화
        self.link = link        # 링크 생성 및 초기화

# 원형연결리스트로 구현한 연결된 큐 (6.4절)
class CircularLinkedQueue:
    def __init__ ( self ):      # 생성자 함수
        self.tail = None        # tail: 유일한 데이터, 생성 및 초기화

    def isEmpty( self ): return self.tail == None   # 공백상태 검사
    def clear( self ): self.tail = None     # 큐 초기화
    def peek( self ):
        if not self.isEmpty():      # 공백이 아니면
            return self.tail.link.data      # front의 data 반환

    def enqueue( self, item ):      # 삽입 연산 (후단을 통해)
        node = Node(item, None)     # 데이터 item로 새로운 노드 node 생성
        if self.isEmpty():          # Case 1: 큐가 공백상태
            node.link = node        # node 링크가 자신을 가리키도록 함
            self.tail = node        # tail이 node 가리키도록 함
        else:                       # Case 2: 큐가 공백이 아님
            node.link = self.tail.link      # node 링크가 front 가리키도록 함. (삽입위치는 tail이므로)
            self.tail.link = node           # tail의 링크가 node를 가리킴
            self.tail = node                # tail이 n을 가리키도록 함

    def dequeue( self ):            # 삭제 연산 (전단을 통해), tail.link를 연결구조에서 꺼내고 데이터 필드를 반환
        if not self.isEmpty():
            data = self.tail.link.data  # front의 데이터 저장
            if self.tail.link == self.tail:     # Case1: 큐가 하나의 항목만을 갖는 경우
                self.tail == None       # tail이 None을 가리키도록 함
            else:       # Case2: 큐가 두 개 이상 항목을 갖는 경우
                self.tail.link = self.tail.link.link        # tail의 링크가 front의 링크를 가리키도록 함
            return data     # front의 데이터 반환

    def size( self ):   # 큐의 크기 구하기: tail 전까지 노드 따라가며 한 바퀴 방문
        if self.isEmpty(): return 0     # 공백이면 0 반환
        else:
            count = 1   # 공백이 아니면, 카운트는 최소 1
            node = self.tail.link   # node는 front 부터 출발
            while not node == self.tail:    # node가 rear이 아닐 때까지
                node = node.link    # 이동
                count += 1          # count 증가
            return count            # 최종 count 반환

    def display( self, msg = 'CircularLinkedQueue:' ):      # 디폴트 인수 사용
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link   # node는 front 부터 출발
            while not node == self.tail:        # node가 rear이 아닐 때까지
                print(node.data, end=' ')       # node 출력
                node = node.link                # 이동
            print(node.data, end=' ')           # 마지막 노드인 tail 출력
        print()

# 테스트 코드(5장 참고)---------------------------
q = CircularLinkedQueue()       # 연결된 원형큐 만들기
for i in range(8): q.enqueue(i)
q.display()
for i in range(5): q.dequeue()
q.display()
for i in range(8, 14): q.enqueue(i)
q.display()

    