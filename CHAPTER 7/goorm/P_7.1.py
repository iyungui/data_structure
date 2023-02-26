# Linked List.
class ArrayList:
    def __init__( self ):
        self.items = []

    def insert(self, pos, elem) : self.items.insert(pos, elem)
    def delete(self, pos) : self.items.pop(pos)
    def isEmpty( self ): return self.size() == 0
    def getEntry(self, pos) : return self.items[pos]
    def size( self ): return len(self.items)
    def clear( self ) : self.items = []
    def find(self, item) : return self.items.index(item)
    def replace(self, pos, elem) : self.items[pos] = elem
    #def sort(self) : self.items.sort()
    def merge(self, lst) : self.items.extend(lst)
    def display(self, msg='ArrayList:' ):
        print(msg, '항목수=', self.size(), self.items)
    def sort(self) :
        insertion_sort(self.items)

def insertion_sort(A):
	n = len(A)
	for i in range(1, n):
		key = A[i]
		j = i-1
		while j>=0 and A[j] > key:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key
				
				
				
				
				
				


s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10);		s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40);	s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")
s.replace(2, 90)
s.display("파이썬 리스트로 구현한 List(교체x1): ")
s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("파이썬 리스트로 구현한 List(삭제x3): ")
lst = [ 1, 2, 3 ]
s.merge(lst)
s.display("파이썬 리스트로 구현한 List(병합+3): ")
s.clear()
s.display("파이썬 리스트로 구현한 List(정리후): ")


"""
big3 = []
big4 = [ '쿠드롱', '야스퍼스', '브롬달', '산체스', [0,1,2]]
lotto = [23, 34, 11, 42, 9]

big3.append("조코비치")
big3.append("페더러")
big3.append("나달")

print("테니스 빅3   = ", big3)
print("당구 4대천왕 = ", big4)
print("다음 로또번호= ", lotto)

big4[2] = '이기범'
print("당구 4대천왕 = ", big4)
"""

