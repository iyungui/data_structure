# 노드 클래스
class Node:
    def __init__(self, elem, link=None):    # 생성자. 디폴트 인수 사용
        self.data = elem        # 데이터 멤버 생성 및 초기화
        self.link = link        # 링크 생성 및 초기화

# 연결된 리스트 클래스(6.3절)
class LinkedList:
    def __init__ ( self ):  # 생성자
        self.head = None    # head 생성 및 초기화
    
    def isEmpty( self ): return self.head == None   # 공백상태 검사
    def clear( self ): self.head = None     # 리스트 초기화

    def size( self ):       # 리스트 항목 수 계산: 맨 마지막 노드까지 움직여서 세보기
        node = self.head     # 시작 노드는 head
        count = 0
        while not node == None: # node가 None이 아닐 때 까지 (마지막 노드까지)
            node = node.link    # 다음 노드로 이동
            count += 1          # count 증가
        return count            # count 반환

    def display( self, msg = 'LinkedList:'):   # 리스트의 항목 출력
        print(msg, end='')      # 메시지를 먼저 출력
        node = self.head     # 시작노드 node가 head를 가리키도록 함
        while not node == None: # node가 None이 아닐 때 까지 (마지막 노드까지)
            print(node.data, end='->')    # node의 데이터 멤버 출력, 노드마다 '->' 출력
            node = node.link    # 다음 노드로 이동
        print('None')   # 마지막 노드의 링크 표시
    
    def getNode(self, pos):       # pos 번째 노드를 반환. head부터 pos까지 즉, pos번 움직여야 접근 가능. O(n)
        if pos < 0: return None
        node = self.head    # node는 head부터 시작
        while pos > 0 and node != None:     # pos번 반복
            node = node.link    # node를 다음노드로 이동
            pos -= 1            # 남은 반복 횟수 1씩 줄임
        return node         # pos번째 노드 반환.

    def getEntry(self, pos):      # pos 번째 노드의 데이터를 반환, O(n)
        node = self.getNode(pos)    # pos 번째 노드 찾기
        if node == None: return None    # 찾는 노드가 없다면 None
        else: return node.data      # 그 노드의 데이터 필드 반환

    def replace(self, pos, elem):   # pos번째 노드의 데이터를 다른 데이터로 변경
        node = self.getNode(pos)    # pos 번째 노드 찾기
        if node != None: node.data = elem   # 그 노드의 데이터 필드에 elem으로 변경

    def find(self, data):       # 데이터로 data를 갖는 노드 찾기(하나씩 이동. 방문하며 찾기)
        node = self.head    # 시작노드는 head
        while node is not None:     # 마지막 노드까지.(모든 노드에서 찾는다.)
            if node.data == data: return node   # data 갖는 노드 찾으면 반환
            node = node.link    # 다음 노드로 이동
        return None     # 못찾으면 None 반환

    def insert(self, pos, elem):  # 삽입 연산. pos 위치에 새로운 노드를 삽입 위해서는 선행 노드 알아야 함.
        before = self.getNode(pos-1)        # before 노드를 찾음
        if before == None:      # 맨 앞에 삽입하는 경우
            self.head = Node(elem, self.head)   # 맨 앞에 삽입함
        else:       # 중간에 before 앞에 삽입하는 경우
            node = Node(elem, before.link)  # 노드 생성, node.link = before.link
            before.link = node      # before.link = node

    def delete(self, pos):   # 삭제 연산. pos 번째 위치한 노드 삭제, 선행노드 알아야 함
        before = self.getNode(pos - 1)      # before 노드 찾기
        if before == None:      # 시작노드를 삭제하는 경우
            if self.head is not None:       # 공백이 아니면
                self.head = self.head.link  # head를 다음 노드의 링크로 이동
        elif before.link != None:       # 중간에 있는 노드 삭제하는 경우
                before.link = before.link.link  # before의 link가 삭제할 노드의 다음 노드를 가리키도록 함

#P6.2 ----------
    def merge(self, B) :    # 연결 리스트의 맨 뒤에 리스트 B를 추가하는 연산
        before = self.getNode(self.size()-1) # 맨 마지막 노드의 링크
        if before == None : # 공백인 경우
            self.head = B.head
        else:
            before.link = B.head
        B.head = None
    # sort 연산 -- 7.2절 참고

# 테스트 코드------------------------------------------
s = LinkedList()
s.display('단순연결리스트로 구현한 리스트(초기상태):')
s.insert(0, 10);            s.insert(0, 20);    s.insert(1, 30)
s.insert(s.size(), 40);     s.insert(2, 50)
s.display("단순연결리스트로 구현한 리스트(삽입x5): ")
s.replace(2, 90)
s.display("단순연결리스트로 구현한 리스트(교체x1): ")
s.delete(2);    s.delete(s.size() -1);      s.delete(0)
s.display("단순연결리스트로 구현한 리스트(삭제x3): ")
s.clear()
s.display("단순연결리스트로 구현한 리스트(정리 후): ")
#---------------------------------------------------