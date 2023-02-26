# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Bag.
class Bag:
		#bag = []
    def __init__( self ): # 가방 생성
        self.bag = [] # 리스트 생성

    def contains(self, e) : # 가방에 e가 있으면 참 아니면 거짓
        return  e in self.bag # 리스트에 e가 있으면 true 아니면 false

    def insert(self, e) : # 가방에 물건 e를 넣는다
        self.bag.append(e) # 리스트에서 요소 e를 넣는다

    def remove(self, e) : # 가방에서 물건 e를 없앤다
        self.bag.remove(e) # 리스트에서 요소 e를 지운다
				

    def count(self): # 가방에 든 물건의 개수를 출력한다
        return len(self.bag) # 리스트의 길이를 출력한다

#====================================
myBag = Bag()
myBag.insert('휴대폰')    
myBag.insert('지갑')
myBag.insert('손수건')    
myBag.insert('빗')
myBag.insert('자료구조')  
myBag.insert('야구공')
print('가방속의 물건:', myBag.bag)

myBag.insert('빗')
myBag.remove('손수건')
print('가방속의 물건:', myBag.bag)

#print(myBag.contains(' '), myBag.contains('휴대폰'))