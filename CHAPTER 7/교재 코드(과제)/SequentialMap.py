# 엔트리 클래스: 맵은 엔트리의 집합
class Entry:        
    def __init__( self, key, value ):       # 생성자. 엔트리는 키(key), 값(value) 필요
        self.key = key
        self.value = value

    def __str__( self ):    # 연산자 중복 사용. 엔트리 객체를 필요시 이 메서드를 이용하여 문자열로 변환
        return str("%s:%s" %(self.key, self.value)) 

# 순차탐색 함수
def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i].key == key:
            return i
    return None

# 리스트를 이용한 순차탐색 맵 구현 -> 단어장 만들기
class SequentialMap:
    def __init__( self ):
        self.table = []                         # 맵의 레코드 테이블

    def size( self ): return len(self.table)    # 레코드의 개수
    def display(self, msg):                     # 보기좋게 출력
        print(msg)
        for entry in self.table:                # 테이블의 모든 엔트리에 대해
            print(" ", entry)                   # 출력(연산자 중복함수 사용)

    def insert(self, key, value):               # 삽입 연산
        self.table.append(Entry(key, value))    # 순차탐색은 리스트 정렬x 이므로, append 사용 -> O(1)
        
    def search(self, key):                      # 순차탐색 -> O(n)
        pos = sequential_search(self.table, key, 0, self.size()-1)  # 순차탐색 함수 호출
        if pos is not None: return self.table[pos]  # 탐색 성공
        else: return None                       # 탐색 실패

    def delete(self, key):                      # 삭제 연산: 항목 위치를 찾아 pop() -> O(n)
        for i in range(self.size()):
            if self.table[i].key == key:        # 삭제할 key를 가진 레코드 위치 찾기
                self.table.pop(i)               # 해당 레코드를 리스트에서 삭제
                return                          # 함수 종료

# 테스트 코드
map = SequentialMap()  # 맵 객체를 만듦
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


