# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def drawTree(row, left, right) :
	mid = (left + right) // 2
	if (left <= right and row<ROWS) : # 만약 왼쪽 끝이 오른쪽 끝보다 작거나 같고 row가 ROWS(6)보다 작으면
		map[row][mid] = 1 # 체크하는 행의 mid번째, 즉 정 가운데의 값을 1로 변경
		drawTree(row+1, left, mid-1) # 'X'가 들어가는 map[##][mid] 를 제외하고 왼쪽 끝부터 mid 직전까지 drawtree를 다시 실행
		drawTree(row+1, mid+1, right) # map[##][mid] 를 제외하고 mid+1 부터 오른쪽 끝까지 drawTree를 다시 실행

def printTree() :
    for i in range(ROWS) : # 0부터 ROW-1까지 반복
        for j in range(COLS) : #0부터 COLS-1 까지 반복
            if map[i][j] == 0 : print('-',end='') # 리스트 값이 0이면, '-' 출력, 'end=''는 이어쓰기
            else: print('X',end='') # 0이 아닌 경우, 즉 1이면 "X" 출력
        print() #줄바꿈

ROWS = 6 # 행 개수
COLS = 64 # 열 개수
map = [[0 for x in range(COLS)] for x in range(ROWS)] # 리스트 두 개 생성(행과 열 표현), 0부터 COLS-1까지, 0부터 ROWS-1까지
drawTree(0, 0, COLS-1) # 위에 생성한 drawTree 함수 사용. 0부터 ROWS-1까지의 행 리스트, 왼쪽 끝은 0, 오른쪽 끝은 COLS-1
printTree()


