# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#------------------------------------------------
class Stack :
    def __init__( self ):   
        self.top = []       

    def isEmpty( self ): return len(self.top) == 0
    def size( self ): return len(self.top)
    def clear( self ): self.top = []	

    def push( self, item ):
        self.top.append(item)

    def pop( self ):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek( self ):
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self ):
        return str(self.top[::-1])
#------------------------------------------------
def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
#        if ch in '{[(':
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty() :
                return False
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False

    return stack.isEmpty()

#------------------------------------------------
def isValidSource( srcfile ): # 소스파일을 입력을 받아 스택 객체 생성
    s = Stack()
    ccnt = 0    # 문자 수
    lcnt = 0    # 라인 수
    eCode= 0    # 에러 코드
#4.4
    b1 = False  # '
    b2 = False  # "
    for line in srcfile : # 소스파일 안의 모든 line
        lcnt += 1 # 각각 라인.수+1
        for token in line :
            if token == '#' : break   # '#'를 만나면 break로 for문 벗어나기(다른 line 으로)  # 한줄 문자열 처리

            if token == "'" :           # '\'' ==> "'", '"'
                if b1 : b1 = False
                else : b1 = True
                continue
            if token == '"' : 
                if b2 : b2 = False
                else : b2 = True
                continue

            if b1 or b2 : continue      # 닫히는 문자가 나올 때 까지 무시
#------------------------------------------------
            ccnt += 1 # 문자수 세기
            if token in "{[(" :
                 s.push( token )
            elif token in "}])" :
                if s.isEmpty() :
                    return  2, lcnt, ccnt  # 조건 2 위반, (에러코드, 라인수, 문자수) 반환
                else :
                    left = s.pop()
                    if (token == "}" and left != "{") or \
                       (token == "]" and left != "[") or \
                       (token == ")" and left != "(") :
                        return  3, lcnt, ccnt # 조건 3 위반

        if not s.isEmpty() : return 1, lcnt, ccnt   # 조건 1 위반     
    return eCode, lcnt, ccnt            # 결과 반환

#------------------------------------------------
filename = input("검사할 파일 이름:")

infile = open(filename , "r", encoding="utf-8")   # 파일 읽기모드로 open, 한글 encoding
lines = infile.readlines()
infile.close()

eCode, lcnt, ccnt =  isValidSource(lines)
print(filename, " ---> ", eCode)
print(" 라인수 = ", lcnt)
print(" 문자수 = ", ccnt)



