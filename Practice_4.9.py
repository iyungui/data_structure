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
        else:  #4.11
            print("underflow")
            exit()
						
    def peek( self ):
        if not self.isEmpty():
            return self.top[-1]
        else:  #4.11
            print("underflow")
            exit()
						
    def __str__(self ):
        return str(self.top[::-1])

    def display(self, i=0):
        if i==len(self.top) : return
        print(self.top[-(i+1)], end=' ')   # self.top[-(i+1)]
        self.display(i+1)       

odd = Stack()				        
even = Stack()				        
for i in range(10):		    	    
    if i%2 == 0 : even.push(i) 		
    else : odd.push(i)			    
	
odd.display()
print()
even.display()