# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
freq=[] # 빈 리스트 생성
def fibo(n): # freq[n]에 값을 넣는 함수
	freq[n] += 1 # freq[n] 에 1을 더한다
	if n <= 1 : return n # freq[0], freq[1] 은 n을 반환
	return fibo(n-1)+fibo(n-2) 

def initFreq(n) : # n개의 요소로 리스트를 만드는 함수
    global freq # freq 를 전역변수로 불러옴
    freq = [0]*n # 요소 0이 n개인 리스트로 freq에 입력
    #print(freq)
initFreq(7)
fibo(6)

for i in range(len(freq)-1, -1, -1) : # (6, -1, -1) 
    print("Fibo(%d) = %d"%(i, freq[i]))
#print(freq)