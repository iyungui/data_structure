# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def merge(A, B) :
    C = []
    i = 0
    j = 0
    while i<len(A) and j<len(B) :
        if A[i] <= B[j] :
            C.append( A[i] )  #append(item)는 리스트의 마지막에 인자로 전달된 아이템을 추가
            #print(C)
            i = i+1
        else:
            C.append( B[j] )
            #print(C)
            j = j+1
    if i < len(A):
        C.extend( A[i:len(A)] )    
    else :
        C.extend( B[j:len(B)] ) #extend(iterable)는 인자로 전달된 iterable의 모든 아이템을 리스트에 추가. 
                              #iterable이기 때문에 list, tuple 모두 가능
    return C

A = [1, 2, 4, 8]
B = [3, 5, 7, 10]
print(merge(A, B))