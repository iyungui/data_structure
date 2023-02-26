#연습문제 6.12
class Node:
    def __init__ (self, elem, next):
        self.data = elem
        self.link = next

class LinkedQueue:
    def __init__( self ):
        self.front = None
        self.rear = None

    def isEmpty( self ): return self.front == None
    def clear( self ): self.front = None
    def enqueue( self, item ):
        if( self.isEmpty()):
            self.front = self.rear = Node(item, None)
        else :
            self.rear.link = Node(item, None)
            self.rear = self.rear.link

    def peek( self ):
        if not self.isEmpty():
            return self.front.data

    def dequeue( self ):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.link
            return data

    def print( self, msg='LinkedQueue:' ):
        print(msg, end='')
        node = self.front
        while not node == None :
            print(node.data, end='->')
            node = node.link
        if node == None: print('None')
        print()

myQ = LinkedQueue()
while True:
    data = int(input("양의 정수를 입력하세요(종료:-1):"))
    if data == -1 : break
    myQ.enqueue(data)

myQ.print()