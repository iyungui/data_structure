# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Linked List.
class ArrayList:
    def __init__( self ):
        self.items = []	
#   def insert(self, pos, elem) : self.items.insert(pos, elem)
# P3.1(1)
    def insert(self, pos, elem) : # 예를 들어 insert(1, 10)
        self.items.append(elem)   # 리스트 맨 뒤에 요소 elem 추가
        for i in range(len(self.items)-2, pos-1, -1) : # (pos-1)-1 즉, (원래 삽입할 위치 -1)-1 부터 len(self.items)-2 즉, (리스트 총 길이 - 2) 만큼 반복
            self.items[i+1] = self.items[i] # 위 범위에 포함된 요소들을 +1 만큼 즉, 오른쪽으로 한칸씩 이동 
        self.items[pos] = elem # elem 을 원래 삽입할 위치로 이동

#   def delete(self, pos) : self.items.pop(pos)
# P3.1(2)
    def delete(self, pos) :
        for i in range(pos, len(self.items)-1): # pos 부터 (len(self.items)-1)-1 까지의 범위
            self.items[i] = self.items[i+1] # 위 범위의 요소들을 -1만큼 즉, 왼쪽으로 한칸씩 이동->이동하면서 pos자리에 있던 요소는 지워짐
        self.items.pop(-1)   # 원래 맨 뒤에 있던 요소는 이동했다고 해서 사라지지 않았으므로, pop(-1)                                     		                                                              
    def isEmpty( self ): return self.size() == 0
    def getEntry(self, pos) : return self.items[pos]
    def size( self ): return len(self.items)
    def clear( self ) : self.items = []	# (3)

#   def find(self, item) : return self.items.index(item)
# P3.1(3)
    def find(self, item) :
        for i in range(len(self.items)): # 0부터 리스트 길이-1 만큼 반복
            if item == self.items[i] : return i # i번째가 찾으려던 item이 맞는지 확인, 맞으면 i 반환
                                
    def replace(self, pos, elem) : self.items[pos] = elem
    def sort(self) : self.items.sort()

#   def merge(self, lst) : self.items.extend(lst)
# P3.1(4) 리스트 덧셈 사용
    def merge(self, lst) :
       	self.items += lst # 리스트 lst의 모든 요소를 리스트 items에 추가

		                     	
    def display(self, msg='ArrayList:' ):
        print(msg, '항목수=', self.size(), self.items)

s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")
s.replace(2, 90)
s.display("파이썬 리스트로 구현한 List(교체x1): ")

print("find 90 pos: ", s.find(90))
print("find 15 pos: ", s.find(15))

s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("파이썬 리스트로 구현한 List(삭제x3): ")
lst = [ 1, 2, 3 ]
s.merge(lst)
s.display("파이썬 리스트로 구현한 List(병합+3): ")
s.clear()
s.display("파이썬 리스트로 구현한 List(정리후): ")