# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def factorial(n): # 팩토리얼 값을 계산하는 함수
	result = 1
	for n in range (1, n+1) :  # 1부터 n까지 반복
		 result *= n # result에 1부터 n까지 차례로 곱한다
	return result # result(팩토리얼 값) 변수 반환

def binomial( n, k ): # 이항계수 계산 함수
	if k == 0 or k == n : return 1 # 만약 k=0 이거나 k=n 이면 1 반환

	return factorial(n) / (factorial(k) * factorial(n-k)) # 팩토리얼 함수를 활용
    # return binomial(n-1, k-1) + binomial(n-1, k) # 순환함수


print(binomial(10, 5))