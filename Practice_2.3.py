# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
height = int(input("피라미드의 높이를 입력하세요: ")) # 피라미드의 높이를 height에 정수형으로 입력
for i in range(1, height+1) : # i는 세로(높이)만큼 반복해야함. 1부터 (height+1)-1 까지 반복
    for j in range(height-i) : # i번째일 때, j가 0부터 height-i 만큼 반복
        print("   ", end='')            # 공백 출력
    for j in range(i) : # i번째일 때, j는 증가하는 숫자 즉, 왼쪽 숫자와 가운데 숫자를 i개 출력
        print("%3d" % (j*2+1), end='')  # %3d는 앞에 3개의 공백을 두고 d를 출력한다는 뜻, d는 (j*2+1)를 말함. 증가하는 숫자 출력
    for j in range(i-2, -1, -1) : 
        # i번째일 때, j는 가운데를 제외한 오른쪽 숫자들 즉, i-1개의 숫자 출력해야함.
        # i = 1 일 때, for j in range(-1, -1, -1)이므로 실행 안함 (감소하는 숫자를 출력하지 않음)
        # i = 2 일 때, for j in range(0, -1 , -1)이므로 j가 0인 경우 한 번 반복
        # i = 3 일 때, for j in range(1, -1, -1)이므로 j가 1과 0인 경우 즉 두 번 반복
        print("%3d" % (j*2+1), end='')  # 감소하는 숫자 출력
    print('')                           # 다음 줄로 이동


