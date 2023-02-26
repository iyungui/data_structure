# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class ArrayList:
    def __init__( self ):
        self.items = []

    def insert(self, pos, elem) : self.items.insert(pos, elem)
    def delete(self, pos) : self.items.pop(pos)
    def isEmpty( self ): return self.size() == 0
    def getEntry(self, pos) : return self.items[pos]
    def size( self ): return len(self.items)
    def clear( self ) : self.items = []
    def find(self, item) : return self.items.index(item)
    def replace(self, pos, elem) : self.items[pos] = elem
    def sort(self) : self.items.sort()
    def merge(self, lst) : self.items.extend(lst)
    def display(self, msg='ArrayList:' ):
        print(msg, '항목수=', self.size(), self.items)

def myLineEditor() :
    list = ArrayList()
    while True :
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-문자열 라인 찾기, q-종료=> ")

        if command == 'i' :
            pos = int( input("  입력행 번호: ") )
            str = input("  입력행 내용: ")
            list.insert(pos, str)

        elif command == 'd' :
            pos = int( input("  삭제행 번호: ") )
            list.delete(pos)

        elif command == 'r' :
            pos = int( input("  변경행 번호: ") )
            str = input("  변경행 내용: ");
            list.replace(pos, str)

        elif command == 'p' :
            print('Line Editor')
            for line in range (list.size()) :
                print('[%2d] '%line, end='')
                print(list.getEntry(line))
            print()

        elif command == 'q' : return

        elif command == 'l' :
            #filename = 'test.txt'
#P3.2(1)
            filename = input("  읽어들일 파일 이름: ") # 읽어들일 파일 이름 입력하여 filename 변수에 지칭
            infile = open(filename, "r", encoding="utf-8") # filename 이라는 파일을 읽기(r)모드로 open, 파일 내에 한글이 있을 경우 encoding="utf-8" 들어가야함
            lines = infile.readlines();  # 파일의 모든 줄을 읽어서 한 라인씩 리스트로 값을 반환
            for line in lines: 
                list.insert(list.size(), line.rstrip('\n')) #각 라인 끝에 있는 '\n' 제거
            infile.close()

        elif command == 's' :
            #filename = 'test.txt'
#P3.2(2)
            filename = input("  저장할 파일 이름: ") # 저장할 파일 이름 입력
            outfile = open(filename, 'w') # filename 파일을 쓰기(w)모드로 open
            len = list.size() 
            for i in range(len) :
                outfile.write(list.getEntry(i)+'\n') # i번째 항목마다 getEntry를 쓰고 \n(줄바꾸기) 넣고, 저장
            outfile.close() 

#P3.2(3)
        elif command == 'f' : # 문자열 라인 찾기
            str = input("  찾는 문자열: ")
            for line in range (list.size()) :
                if list.getEntry(line).find(str) >= 0 : # 해당 문자열이 있는 line을 찾기
                    print(list.getEntry(line))

myLineEditor()

