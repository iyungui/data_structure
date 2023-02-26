# 선형조사법: 버킷에 빈 

# LinearProbMap.
class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

    def __str__( self ):
        return str("%s:%s"%(self.key, self.value) )


class LinearProbMap:
    def __init__( self, M ):
        self.table = [None]*M
        self.M = M

    def hashFn(self, key) :
        sum = 0
        for c in key : sum = sum +  ord(c)
        return sum % self.M

    def insert(self, key, value) :
        id = self.hashFn(key)
        count = self.M
        while count>0 and (self.table[id] != None and self.table[id] != -1) :  # -1은 삭제한 자리 표시
            id = (id + 1 + self.M) % self.M
            count -= 1
        if count > 0 :
            self.table[id] = Entry(key,value)
        return

    def search(self, key) :
        id = self.hashFn(key)
        count = self.M
        while count>0 :
            if self.table[id] == None : return None
            if self.table[id] != -1 and self.table[id].key == key : 
               return self.table[id]
            id = (id + 1 + self.M) % self.M
            count -= 1
        return None

    def delete(self, key) :
        id = self.hashFn(key)
        count = self.M
        while count>0 :
            if self.table[id] == None : return None
            if self.table[id] != -1 and self.table[id].key == key : 
                self.table[id] = -1
                return
            id = (id + 1 + self.M) % self.M
            count -= 1

    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)) :
            node = self.table[idx]
            print("[%2d] -> "%idx, self.table[idx])


#======================================================================
map = LinearProbMap(13)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장: ")

print(" 탐색:game --> ", map.search('game'))
print(" 탐색:over --> ", map.search('over'))
print(" 탐색:data --> ", map.search('data'))

map.delete('game')
map.display("나의 단어장: ")
print(" 탐색:game --> ", map.search('game'))
