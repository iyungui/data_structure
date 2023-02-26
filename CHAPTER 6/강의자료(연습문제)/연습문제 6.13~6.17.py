class Node:                                
    def __init__ (self, elem, link=None):  
        self.data = elem                    
        self.link = link    

def printList(head, msg="생성된 연결 리스트:"):
    print(msg, end="")
    n = head
    while n != None :
        print(n.data, end="->")
        n = n.link
    if n == None: print('None')
    print()

head = None
tail = None
count = int(input("노드의 개수 :"))

for i in range(count):
    data = int(input("노드 %d의 데이터 :"%(i+1)))
    n = Node(data, None)
    if head==None :
        head = tail = n
    else :
        tail.link = n
        tail = n

#6.13       
# printList(head)

#6.14
# data = int(input("끝에 추가할 데이터 :"))
# n = Node(data, None)
# tail.link = n
# tail = n
# printList(head)

#6.15
# head = head.link
# printList(head, "첫 번째 노드 삭제 후 연결 리스트 :")

#6.16
# sum = 0
# n = head
# while n != None :
#     sum += n.data
#     n = n.link
# print("연결 리스트의 데이터 합:", sum)

#6.17
# data = int(input("탐색할 값을 입력하시오:"))
# count = 0
# n = head
# while n != None :
#     if n.data == data : count += 1
#     n = n.link
# print("%d는 연결 리스트에서 %d번 나타납니다"%(data, count))