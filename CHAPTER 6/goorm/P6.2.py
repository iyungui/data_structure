# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Linked List.
class Node:
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next

class LinkedList:
    def __init__( self ):
        self.head = None

    def isEmpty( self ): return self.head == None
    def clear( self ) : self.head = None
    def size( self ) :
        node = self.head
        count = 0
        while node is not None :
            node = node.link
            count += 1
        return count
    def display(self, msg='LinkedList:' ):
        print(msg, end='')
        node = self.head
        while node is not None :
            print(node.data, end='->')
            node = node.link
        print('None')

    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None :
            node = node.link
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
        node = self.head
        while node is not None:
            if node.data == val : return node
            node = node.link
        return node

    def insertNext(before, node) :
        node.link = before.link
        before.link = node
    def deleteNext(before) :
        if before.link != None :
            before.link = before.link.link

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞에 삽입함
            self.head = Node(elem, self.head)
        else :
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞 노드를 삭제
            if self.head is not None :
                self.head = self.head.link
        elif before.link != None :
            before.link = before.link.link

#P6.2 ----------
    def merge(self, B) :
        before = self.getNode(self.size()-1) # 맨 마지막 노드의 링크
        if before == None : # 공백인 경우
            before.link = B.head                                              # 문제 부분. 두 연결리스트의 head끼리 연결하기
        else: # print 함수를 이용해서 이해를 도움
            before.link = B.head                                            # 문제 부분. 연결구조이므로, 병합(merge) 하려면 insert가 아니라, '연결'을 생각해야 함.
        B.head = None


#======================================================================
s = LinkedList()
s.display('단순연결리스트로 구현한 리스트(초기상태):')
s.insert(0, 10);		s.insert(0, 20);     s.insert(1, 30)
s.insert(s.size(), 40);	s.insert(2, 50)
s.display("단순연결리스트로 구현한 리스트(삽입x5): ")

s.replace(2, 90)
s.display("단순연결리스트로 구현한 리스트(교체x1): ")
s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("단순연결리스트로 구현한 리스트(삭제x3): ")

s2 = LinkedList()
s2.insert(0, 15);       s2.insert(1, 25);       s2.insert(2, 35);

s.merge(s2)
s.display("s 병합: ")
s2.display("s2 병합: ")

s.clear()
s.display("s 정리: ")
