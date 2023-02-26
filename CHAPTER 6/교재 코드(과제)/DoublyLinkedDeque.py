# 이중연결리스트를 위한 노드
class DNode:
    def __init__ (self, elem, prev = None, next = None):    # 생성자. 디폴트 인수 사용. 노드는 각각 두개의 링크를 갖는다.
        self.data = elem    # 데이터 멤버 생성 및 초기화
        self.prev = prev    # 링크 생성 및 초기화
        self.next = next    # 링크 생성 및 초기화

# 이중연결리스트로 구현한 연결된 덱 (6.5절)
class DoublyLinkedDeque:
    def __init__ (self):    # 생성자
        self.front = None   # front 생성 및 초기화 
        self.rear = None    # rear 생성 및 초기화

    def isEmpty( self ): return self.front == None  # 공백상태 검사
    def clear( self ): self.front = self.rear = None    # 초기화
    def size( self ):
        node = self.front   # 시작 노드
        count = 0
        while not node == None:     # 노드가 None이 아닐 때까지
            node = node.next
            count += 1
        return count
    def display(self, msg='LinkedDeque:'):
        print(msg, end='')
        node = self.front   # 시작 노드 설정
        while not node == None:
            print(node.data, end=' ')
            node = node.next
        print()

    # getFront, getRear 연산 추가

    def addFront( self, item ): # 전단 삽입
        node = DNode(item, None, self.front)   # 노드 생성 및 prev, next 초기화 (전단삽입이므로 prev는 None, next는 front)
        if self.isEmpty():  # 공백이면
            self.front = self.rear = node   # front, rear 모두 node 가리킴
        else:   # 공백이 아니면
            self.front.prev = node  # front가 선행노드로 node 가리킴
            self.front = node       # front가 node 가리킴
    
    def addRear( self, item ):  # 후단 삽입
        node = DNode(item, self.rear, None)    # 노드 생성 및 prev, next 초기화 (후단삽입이므로 prev는 rear, next는 None)
        if self.isEmpty():  # 공백이면
            self.front = self.rear = node   # front, rear 모두 node 가리킴
        else:   # 공백이 아니면
            self.rear.next = node   # rear가 다음노드로 node 가리킴
            self.rear = node    # 이제 rear가 node 가리킴
    
    def deleteFront( self ):    # 전단 삭제
        if not self.isEmpty():
            data = self.front.data  # 삭제할 노드(front)의 데이터 복사
            self.front = self.front.next    # front를 다음 노드로 옮김
            if self.front == None:  # 만약 여기서 노드가 하나 뿐이면
                self.rear == None   # rear도 None으로 설정해야 한다.
            else:
                self.front.prev = None  # front의 이전노드를 None에 가리키게 함
            return data     # 처음에 복사한 데이터 반환

    def deleteRear( self ): # 후단 삭제
        if not self.isEmpty():
            data = self.rear.data   # 삭제할 노드(Rear)의 데이터 복사
            self.rear = self.rear.prev      # rear를 이전 노드로 옮김
            if self.rear == None:   # 노드가 하나 뿐이면
                self.front = None   # front도 None으로 설정
            else:
                self.rear.next = None   # rear의 다음노드를 None에 가리키게 함
            return data     # 데이터 반환

# 테스트 코드 (5장 참고)--------------------
dq = DoublyLinkedDeque()    # 연결된 덱 만들기
for i in range(9):			        
	if i%2==0 : dq.addRear(i)		
	else : dq.addFront(i)		    
dq.display()				        
for i in range(2): dq.deleteFront()	
for i in range(3): dq.deleteRear()	
dq.display()
for i in range(9,14): dq.addFront(i)
dq.display()

        


