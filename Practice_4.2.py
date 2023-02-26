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
			

instr = input("문자열 입력: ")
s = Stack()

instr = instr.lower() # 모두 소문자로 변경
for ch in instr: # ord()는 하나의 문자를 받아 대응하는 유니코드 정수
    if ord(ch) < ord('a') or ord(ch) > ord('z') :
        continue # 알파벳 소문자가 아닌 경우는 통과
    s.push(ch)  # ch를 스택에 넣는다.

for ch in instr:
    if ord(ch) < ord('a') or ord(ch) > ord('z') :
        continue
    if ch != s.pop() : # ch가 스택에서 꺼낸 문자와 같지 않으면
        print("회문이 아님")
        exit()
print("회문이 맞음")