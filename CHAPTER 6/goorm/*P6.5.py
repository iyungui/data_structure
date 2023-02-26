# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Python list를 이용한 Sparse Polynomial 클래스 구현.
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
        node = self.head;
        count = 0;
        while node is not None :
            node = node.link
            count += 1
        return count
    
    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head;
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

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

'''
하나의 항을 나타내기 위한 클래스
'''
class Term :
    def __init__( self, expon, coeff ):
        self.expon = expon
        self.coeff = coeff

'''
희소 다항식 클래스
'''
class SparsePoly(LinkedList):
    def __init__( self ):
        super().__init__()

    def degree(self) :
        if self.head == None : return 0
        else : return self.head.data.expon

    def display(self, msg=""):
        print("\t", msg, end='')
        node = self.head
        while node is not None :
            print("%5.1f x^%d + " % (node.data.coeff, node.data.expon), end='')
            node = node.link
        print()

    def read(self):
        self.clear()
        while True :
            token = input("계수 차수 입력(종료:-1): ").split(" ")
            if token[0] == '-1' :
                self.display("입력 다항식:")
                return
            self.insert(self.size(), Term(int(token[1]), float(token[0])))

    def add(self, B):
        C = SparsePoly()
        a = self.head
        b = B.head
        while a!=None or b!=None :
            if a==None or (b!=None and a.data.expon < b.data.expon) :
                C.insert(C.size(), Term(b.data.expon,b.data.coeff))
                b = b.link

            elif b==None or (a!=None and a.data.expon > b.data.expon) :
                C.insert(C.size(), Term(a.data.expon,a.data.coeff))
                a = a.link

            else :
                term = Term(a.data.expon, a.data.coeff+b.data.coeff)
                C.insert(C.size(), term)
                a = a.link
                b = b.link

        return C


a = SparsePoly()
b = SparsePoly()
a.read()
b.read() 
c = a.add(b)
a.display(" A = ")
b.display(" B = ")
c.display("A+B= ")

