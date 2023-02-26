# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Set.
class Set:
    def __init__( self ):
        self.items = []

    def size( self ):
       return len(self.items)

    def contains(self, item) :
#       return item in self.items
# P3.3(1)
        for i in range(len(self.items)) : # self.items의 모든 항목에 대해
            if self.items[i] == item : # item이 self.items[i]와 같으면
                return True # 집합 내에 있으므로 return True
        return False # 없음. return False

    def insert(self, elem) :
#        if elem not in self.items :
# P3.3(3)
        if self.contains(elem) == False : # 객체 안에 elem 가 없어야 append 하므로, False
           self.items.append(elem) # 리스트 맨 뒤에 elem 추가

    def delete(self, elem) :
#        if elem in self.items :
#            self.items.remove(elem)
# P3.3(2)
        for i in range(len(self.items)) : # self.items의 모든 항목에 대해
            if self.items[i] == elem : # elem가 self.items[i]와 같으면
              self.items.pop(i) # i번째 요소인 elem 제거
                       
#    def __eq__( self, setB ):
#        if self.size() != setB.size() :
#            return False
#        else :
#            return self.isSubsetOf( setB )

#    def isSubsetOf( self, setB ):
#        for elem in self.items :
#           if elem not in setB : return False
#       return True

    def isProperSubsetOf( self, setB ):
        for elem in self.items :
           if elem not in setB : return False

        if self.size() == setB.size() : return False
        else: return True


    def union( self, setB ):                # C = self U  B
        newSet = Set()
        newSet.items = list(self.items)
        for elem in setB.items :
#            if elem not in self.items :
# P3.3(3)
            if not self.contains(elem) : # 
                newSet.items.append(elem)
        return newSet

    def intersect( self, setB ):            # C = self ^ B
        setC = Set()
        for elem in setB.items :
#            if elem in self.items :
# P3.3(3)
            if self.contains(elem): # 
                setC.items.append(elem)
        return setC

    def difference( self, setB ):           # C = self - B
        setC = Set()
        for elem in self.items:
#            if elem not in setB.items:
# P3.3(3)
            if not setB.contains(elem): # 
               setC.items.append(elem)
        return setC

# P3.3(4)
    def __sub__( self, setB ):           # C = self - B
          return self.difference(setB)

# P3.3(5)
    def isSubsetOf( self, setB ):
        for elem in self.items :
           if  elem not in setB : return False
        return True

    def display(self, msg):
        print(msg, self.items)

#    def __iter__( self ):
#        return _SetIterator( self.items )

#======================================================================
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A - B:')
(setA-setB).display('A - B:')


s1 = { 1,2,3 }
s2 = { 2,3,4,5 }
s3 = s1.union(s2)
s4 = s1.intersection(s2)
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)
#print("range(1,9):", range(1,9))
#c1 = 1 + 2j
#c1 = complex(1,2)
# c2 = complex(3,4)
# c3 = c1 + c2
# print("c1:",c1)
# print("c2:",c2)
# print("c3:",c3)

