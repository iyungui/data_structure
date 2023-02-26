# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Linked List.
class Node:
    def __init__ (self, elem, prev=None, next=None):
        self.data = elem 
        self.prev = prev
        self.next = next

def insertNext(before, node) :
    node.next = before.next;
    node.prev = before
    before.next = node
    if node.next != None :
        node.next.prev = node

class LinkedList:
    def __init__( self ):
        self.head = None

    def isEmpty( self ): return self.head == None
    def clear( self ) : self.head = None
    def size( self ) :
        node = self.head;
        count = 0;
        while node is not None :
            node = node.next
            count += 1
        return count
			
    def display(self, msg='LinkedList:' ):
        print(msg, end='')
        node = self.head
        while node is not None :
            print(node.data, end='->')
            node = node.next
        print('None')

    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head;
        while pos > 0 and node != None :
            node = node.next
            pos -= 1
        return node
			
    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

    def replace(self, pos, elem) :
        node = self.getNode(pos)
        if node != None : node.data = elem

    def find(self, val) :
        node = self.head;
        while node is not None:
            if node.data == val : return node
            node = node.next
        return node

#P6.4 -----------------------
    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞에 삽입함
            self.head = Node(elem, None, self.head)
        else :
            insertNext(before, Node(elem))

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞 노드를 삭제
            if self.head is not None :
                self.head = self.head.next
                self.head.prev = None
        elif before.next != None :
            before.next = before.next.next
            if before.next != None:
                before.next.prev = before


#======================================================================
s = LinkedList()
s.display('이중연결리스트로 구현한 리스트(초기상태):')
s.insert(0, 10);		s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40);	s.insert(2, 50)
s.display("이중연결리스트로 구현한 리스트(삽입x5): ")
#s.sort()
#s.display("단순연결리스트로 구현한 List(정렬후): ")
s.replace(2, 90)
s.display("이중연결리스트로 구현한 리스트(교체x1): ")
s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("이중연결리스트로 구현한 리스트(삭제x3): ")
#lst = [ 1, 2, 3 ]
#s.merge(lst)
#s.display("파이썬 리스트로 구현한 List(병합+3): ")
s.clear()
s.display("이중연결리스트로 구현한 리스트(정리후): ")






