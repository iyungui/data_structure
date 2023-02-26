# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Linked Queue.
class Node:
    def __init__ (self, elem, next):
        self.data = elem 
        self.link = next

class LinkedQueue:
    def __init__( self ):
        self.front = None
        self.rear = None

    def isEmpty( self ): return self.front == None

    def enqueue( self, item ):                                      # 처음으로 생각할 부분은 큐에서 삽입은 '후단'을 통해 이루어진다는 것!
        if( self.isEmpty()):
            self.front = self.rear = Node(item, None)		        # 공백이므로, 전단과 후단 모두 삽입할 노드를 가리켜야함. 삽입할 노드는 처음에 None링크
        else :
            self.rear.link = Node(item, None)                       # Node를 삽입(생성?) 하는데, 이것은 후단노드의 다음링크를 받고 있음
            self.rear = self.rear.link

    def peek( self ):
        if not self.isEmpty():
            return self.front.data

    def dequeue( self ):                                            # 처음으로 생각할 부분은 큐에서 삭제는 '전단'을 통해 이루어진다는 것!        
        if not self.isEmpty():
            data = self.front.data                                  # 삭제할 노드(front)의 데이터 필드 복사.
            self.front = self.front.link	                        # front가 다음 노드를 가리키게 함
            return data

    def print( self, msg='LinkedQueue:' ):
        print(msg, end='')
        node = self.front
        while not node == None :
            print(node.data, end=' ')
            node = node.link
        print()

#======================================================================
def testLinkedQueue() :
    print('연결된 구조의 큐 구현\n')
    queue = LinkedQueue()
    for i in range(10):
        queue.enqueue(i)
    queue.print('큐 enqueue 9회:')
    print('\tdequeue() --> ', queue.dequeue())
    print('\tdequeue() --> ', queue.dequeue())
    print('\tdequeue() --> ', queue.dequeue())
    queue.print('큐 dequeue 3회:')

    queue.enqueue('홍길동')
    queue.enqueue('이순신')
    queue.enqueue('김연아')
    queue.enqueue('황희')
    queue.print('큐 enqueue 4회:')
    print('\tdequeue() --> ', queue.dequeue())
    queue.print('큐 dequeue 1회:')
    print('\tpeek()--> ', queue.peek())

testLinkedQueue()
