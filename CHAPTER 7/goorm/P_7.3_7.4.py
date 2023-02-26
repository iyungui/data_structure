class Set:                      
    def __init__( self ):      
        self.items = []        

    def size( self ):          
        return len(self.items)  

    def display(self, msg):    
        print(msg, self.items)  

    def contains(self, item) :         # item이 self.items에 있는지 검사, O(n)
       return item in self.items

    # def contains(self, item) :
    #     for i in range(len(self.items)): # self.items의 모든 항목에 대해
    #         if self.items[i] == item :     # item이 self.items[i]와 같으면
    #             return True              # 집합 내에 있으므로 return True
    #     return False                   # 없으므로 return False

    # def insert(self, elem) :            
    #     if elem not in self.items :      # 삽입할 항목이 없으면(중복 허용 X)
    #        self.items.append(elem)       # 삽입 
    def insert(self, elem) :        # O(n)  --> 수정 --> 여전히 O(n)
        if elem in self.items : return      # 이미 있음
        for idx in range(len(self.items)) : # loop: n번
            if elem < self.items[idx] :     # idx위치에 삽입
                self.items.insert(idx, elem)
                return
        self.items.append(elem)             # 맨 뒤에 삽입
 
    def delete(self, elem) :             # O(n)
        if elem in self.items :          # 삭제할 항목이 있으면
           self.items.remove(elem)       # 삭제

    def __eq__( self, setB ):            # O(mn) ---> O(n+m)
        if self.size() != setB.size() :
            return False
        for idx in range(len(self.items)):  # loop: n번      
            if self.items[idx] != setB.items[idx] :
                return False
        return True
       
    # def union( self, setB ):          
    #     setC = Set()                   # 결과 집합
    #     setC.items = list(self.items)  # self 의 리스트를 setC에 복사(deep copy:새로운 객체 형성)
    #     for elem in setB.items :       # 외부 루프: setB의 모든 항목에 대해
    #         if elem not in self.items :    # 내부 루프:self에 없으면
    #             setC.items.append(elem)    # 중복이 아니므로 추가
    #     return setC                       
    def union( self, setB ):            # O(mn) ---> O(n+m)
        newSet = Set()                  
        a = 0                          
        b = 0                          
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]      
            valueB = setB.items[b]      
            if valueA < valueB :        
                newSet.items.append( valueA )  
                a += 1                  
            elif valueA > valueB :      
                newSet.items.append( valueB )  
                b += 1          
            else :   # Only one of the two duplicates are appended.            
                newSet.items.append( valueA )  
                a += 1                  
                b += 1
        while a < len( self.items ):    
             newSet.items.append( self.items[a] )
             a += 1
        while b < len( setB.items) :    
             newSet.items.append( setB.items[b] )
             b += 1
       
        return newSet              
    # def intersect( self, setB ):  
    #     setC = Set()
    #     for elem in setB.items :       # 외부 루프: setB의 모든 항목에 대해
    #         if elem in self.items :        # 내부 루프:self에 있으면
    #             setC.items.append(elem)    # 양쪽에 모두 있으므로 추가
    #     return setC
    #p7.3
    def intersect( self, setB ):        # O(mn) ---> O(n+m)
        newSet = Set()
        a = 0
        b = 0
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :
                a += 1
            elif valueA > valueB :
                b += 1
            else : # Only one of the two duplicates are appended.
                newSet.items.append( valueA )
                a += 1
                b += 1
        
        return newSet

    # def difference( self, setB ):     
    #     setC = Set()
    #     for elem in self.items:            # 외부 루프: self의 모든 항목에 대해
    #         if elem not in setB.items:     # 내부 루프:setB에 없으면
    #             setC.items.append(elem)    # 추가
    #     return setC
    #p7.4
    def difference( self, setB ):        # O(mn) ---> O(n+m)
        newSet = Set()
        a = 0
        b = 0
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :
                newSet.items.append( valueA )
                a += 1
            elif valueA > valueB :
                b += 1
            else : 
                a += 1
                b += 1

        while a < len( self.items ) :
             newSet.items.append( self.items[a] )
             a += 1
        
        return newSet
#===========================================================================
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
setA.difference(setB).display('A – B:')