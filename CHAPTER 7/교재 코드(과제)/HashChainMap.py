# 노드 클래스: 연결리스트를 사용하는 체이닝은 노드가 필요함
class Node:
    def __init__(self, elem, link=None):    # 생성자. 디폴트 인수 사용
        self.data = elem        # 데이터 멤버 생성 및 초기화
        self.link = link        # 링크 생성 및 초기화


# 엔트리 클래스: 맵은 엔트리의 집합
class Entry:        
    def __init__( self, key, value ):       # 생성자. 엔트리는 키(key), 값(value) 필요
        self.key = key
        self.value = value

    def __str__( self ):    # 연산자 중복 사용. 엔트리 객체를 필요시 이 메서드를 이용하여 문자열로 변환
        return str("%s:%s" %(self.key, self.value))

# 해시 체인 맵
class HashChainMap:
    def __init__( self, M ):
        self.table = [None]*M   # 크기 M인 테이블을 먼저 만들어서 해시 테이블 준비
        self.M = M              # M은 테이블의 크기를 나타냄
    
    def hashFn(self, key):      # 엔트리의 키가 문자열일 때, 사용하는 해시 함수
        sum = 0
        for c in key:           # 문자열의 모든 문자에 대해
            sum += ord(c)       # 아스키 코드 값을 모두 더함
        return sum % self.M     # 테이블의 크기로 나눈 나머지를 반환

    def insert(self, key, value):   # 삽입 연산: 해시 주소 계산 후, 삽입할 노드를 해당 연결 리스트의 '맨 앞'에 추가 -> O(1)
        idx = self.hashFn(key)      # 해시 함수 이용하여 해시 주소 계산
        self.table[idx] = Node(Entry(key, value), self.table[idx])  # 생성한 엔트리를 데이터로 갖고, 위에서 계산한 해시 주소를 링크로 갖는 노드 생성. 전단 삽입
                                                                    # entry = Entry(key, value)  # (1) 엔트리를 생성
                                                                    # node = Node(entry) # (2) 엔트리로 노드를 생성
                                                                    # node.link = self.table[idx]  # (3) 노드의 링크필드 처리
                                                                    # self.table[idx] = node  # (4) 테이블의 idx 항목: node로 시작
    
    def search(self, key):          # 탐색 연산: 해시 주소 계산 후, 해당 주소의 연결 리스트에 있는 모든 노드에 대해 찾는 키를 가진 노드의 데이터 반환
        idx = self.hashFn(key)      # 해시 주소 계산
        node = self.table[idx]      
        while node is not None:     # 해당 해시 주소에 있는 모든 노드
            if node.data.key == key:    # 탐색 성공
                return node.data
            node = node.link        # 다음 노드
        return None

    def delete(self, key):          # 연결리스트이므로, 삭제할 노드의 선행 노드 찾은 후, 해당 노드 삭제
        idx = self.hashFn(key)      # 해시 주소 계산
        node = self.table[idx]
        before = None               # ?
        while node is not None:     # None이 아닐 때 까지
            if node.data.key == key:    # 삭제할 레코드 찾음
                if before == None:  # 첫 번째 항목 삭제하는 경우
                    self.table[idx] = node.link # 삭제
                else:               # 두 번째 이후 항목 삭제
                    before.link = node.link
                return              # 함수 종료
            before = node           # before 갱신
            node = node.link        # node 갱신

    def display(self, msg):         # 맵 출력 함수
        print(msg)
        for idx in range(len(self.table)):  # 맵 전체 출력
            node = self.table[idx]
            if node is not None:        # 마지막 노드가 아니라면 
                print("[%2d] -> " %idx, end='')
                while node is not None: # None이 아닐 때까지
                    print(node.data, end=' -> ')        # 엔트리 클래스의 연산자 중복함수(__str__) 사용
                    node = node.link    # 다음 노드로 이동
                print()                 # 다음 줄로


# 테스트 코드
map = HashChainMap(13)  # 맵 객체를 만듦, 이 때 변수 M 필요
map.insert('data', '자료')  # 맵에 엔트리를 삽입
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game','게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장: ")  # 맵 출력

print("탐색:game --> ", map.search('game'))  # 탐색 테스트
print("탐색:over --> ", map.search('over'))
print("탐색:data --> ", map.search('data'))

map.delete('game')
map.display('나의 단어장: ')


        
        


        


