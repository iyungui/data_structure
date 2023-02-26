# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 클래스로 구현.
class Polynomial : # 클래스 생성
    def __init__( self ):
        self.coef= [] # 계수를 담을 빈 리스트 생성

    def degree(self) : 
        return len(self.coef) - 1 # 차수 = 계수의 길이 - 1

    def display(self, msg="f(x) = "):
        print("  ", msg, end='')
        deg = self.degree() # 차수

        for n in range(deg, 0, -1) : # 입력받은 차수부터 0 전까지 거꾸로
            print("%5.1f x^%d + " % (self.coef[n], n), end='')
        print("%4.1f"%self.coef[0])

    def add(self, b):
        p = Polynomial()
        if self.degree() > b.degree() : # 입력한 차수가 매개변수로 들어온 차수보다 크면
            p.coef = list(self.coef)
            for i in range(b.degree()+1) : # 매개변수로 들어온 차수 만큼의 범위
                p.coef[i] += b.coef[i] # 계수가 들어온 리스트에 차수가 보다 낮은 리스트를 각각 더한다
        else : # 입력한 차수보다 매개변수로 들어온 차수가 크거나 같으면
            p.coef = list(b.coef) 
            for i in range(self.degree()+1) : # 입력한 차수 만큼의 범위
                p.coef[i] +=  self.coef[i]  
        return p

    def eval(self, x):
        result = 0.0
        for i in range(self.degree()+1) : # 입력한 차수만큼의 범위
            result += self.coef[i] * (x**i) 
						# i=0 일 때, self.coef[0] * x의 0제곱
						# i=1 일 때, self.coef[1] * x의 1제곱
						#... 이런 식을 다 더하여 result 반환
        return result

    
def read_poly(): 
    p = Polynomial()
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    for n in range(deg+1) :
        coefficient = float(input(  "\tx^%d의 계수 : " % (deg-n))) # d는 최고차수-n를 가리킴
        p.coef.append(coefficient) # 리스트에 계수를 추가
    p.coef.reverse() # 리스트 요소를 거꾸로 (방법2)
    return p

# 테스트 코드
a = read_poly() # 키보드로 다항식 a를 입력받음
b = read_poly() # 키보드로 다항식 b를 입력받음
c = a.add(b) # c=a+b
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
print(" C(2) = ", c.eval(2)) # 다항식 c의 미지수에 2를 대입한 결과 계산 및 출력

