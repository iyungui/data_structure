# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#from stackClass import Stack
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
        return str(self.top)

def precedence (op):
    if   (op=='(' or op==')') : return 0
    elif (op=='+' or op=='-') : return 1
    elif (op=='*' or op=='/') : return 2
    else : return -1

def Infix2Postfix( expr ): # 입력 리스트
    s = Stack() # 연산자를 스택에 저장
    output = [] # 출력 리스트
    for term in expr :        
        if term in '(' : # 왼쪽 괄호는 무조건 스택에 삽입
            s.push('(')

        elif term in ')' : # 오른쪽 괄호를 만나면
            while not s.isEmpty() : # 스택 빈자리 없을 때까지
                op = s.pop() 
                if op=='(' : # 왼쪽 괄호가 삭제될 때까지
                    break
                else :
                    output.append(op) # 왼쪽 괄호가 아니면 모든 연산자 출력

        elif term in "+-*/" : # 연산자는 일단 출력 보류, 스택에 저장
            while not s.isEmpty() :
                op = s.peek()
								#우선순위가 높거나 같은 연산자는 먼저 출력
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term) # 연산자는 일단 출력 보류, 스택에 저장

        else :                  # 피연산자는 바로 출력
            output.append(term)

    while not s.isEmpty() :
        output.append(s.pop()) # 스택에 남은 연산자 모두 꺼내서 출력

    return output

#------------------------------------------------
def evalPostfix( expr ): # 후위표기 수식 계산
    s = Stack()
    for token in expr :
        if token in "+-*/" : # 연산자
            val2 = s.pop() # 피연산자2
            val1 = s.pop() # 피연산자1
            if (token == '+'): s.push(val1 + val2) # 결과는 스택에 다시 저장
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :
            s.push( float(token) ) # 피연산자를 스택에 저장

    return str(s.pop()) # 최종결과 역순으로 반환

#-----------      -------------------------------------
expr = input("입력 수식(공백문자로 분리)= ")
infix = expr. split(' ') # 공백문자로 나눠주기 split(' ')

print('  중위표기: ', infix)

postfix = Infix2Postfix(infix)
print('  후위표기: ', postfix)

result = evalPostfix(postfix)
print('  계산결과: ', result)

