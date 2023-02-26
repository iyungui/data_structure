# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link			        

class LinkedStack :
    def __init__( self ):	
        self.top = None	    # top 생성 및 초기화

    def isEmpty( self ): return self.top == None
    def clear( self ): self.top = None		    
    def push( self, item ):	                	
        n = Node(item, self.top)	        	
        self.top = n			

    def pop( self ):			# 연결된 스택의 삭제연산
        if not self.isEmpty():	# 공백이 아니면
            n = self.top		
            self.top = self.top.link	# self.top = n.link 
            return n.data		

    def peek( self ):			# 시작 노드의 데이터 반환
        if not self.isEmpty():	
            return self.top.data

    def size( self ):			
        node = self.top			
        count = 0
        while not node == None :
            node = node.link	
            count += 1			
        return count			

    def display( self, msg='LinkedStack:'): 
        print(msg, end='')		
        node = self.top			
        while not node == None :	 	
            print(node.data, end=' ')	
            node = node.link		    
        print()

instr = input("문자열 입력:")
s = LinkedStack() # 연결된 스택 사용	                                            #

instr = instr.lower()

for ch in instr:
    if ord(ch) < ord('a') or ord(ch) > ord('z') :
        continue
    s.push(ch)                                                                  # 연결된 스택에서 push 삽입연산 사용.

s.display()

for ch in instr:
    if ord(ch) < ord('a') or ord(ch) > ord('z') :
        continue
    if ch != s.pop() :                                                          # 스택에서 꺼냈을 때, 입력한 ch와 동일하지 않을 때: 회문이 아님
        print("회문이 아님")
        exit()
print("회문이 맞음")

