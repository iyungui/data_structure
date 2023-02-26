# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Stack :
    def __init__( self ):   
        self.top = []       

    def isEmpty( self ): return len(self.top) == 0
    def size( self ): return len(self.top)
    def clear( self ): self.top = []	

    def push( self, item ):
        self.top.append(item)

    def pop( self ):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek( self ):
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self ):
        return str(self.top[::-1])


instr = input("문자열 입력 : ") # 문자열 입력
s = Stack() #스택 사용

for ch in instr: # 입력받은 문자열 하나씩 삽입, push
    s.push(ch)

print("역순 문자열 : ", end = "")
while not s.isEmpty(): # 스택이 비어있지 않을 때 까지
    print(s.pop(), end = " ") # pop을 통해 스택에서 꺼내옴