

# 이진탐색트리를 위한 노드 클래스
class BSTNode:
    def __init__(self, key, value):     # 생성자. 키와 값을 받음
        self.key = key                  # 키
        self.value = value              # 값
        self.left = None                # 왼쪽 자식에 대한 링크
        self.right = None               # 오른쪽 자식에 대한 링크

def search_bst(n, key):                 # 탐색 연산
    if n == None:
        return None
    elif key == n.key:                  # n의 키 값이 찾으려는 key. 탐색 성공
        return n
    elif key < n.key:                   # key < n 의 키
        return search_bst(n.left, key)  # 순환 호출, 왼쪽 서브트리 탐색
    else:
        return search_bst(n.right, key) # 순환 호출, 오른쪽 서브트리 탐색

def search_bst_iter(n, key):            # 탐색 연산 (반복 함수)
    while n != None:
        if key == n.key:                # n의 키 값이 찾으려는 key. 탐색 성공
            return n
        elif key < n.key:               # key < n 의 키
            n = n.left                  # n을 왼쪽 서브트리의 루트로 이동
        else:                           # key > n 의 키
            n = n.right                 # n을 오른쪽 서브트리의 루트로 이동
    return None

def search_value_bst(n, value):         # 값을 이용한 탐색. preorder을 사용한 함수
    if n == None : return None
    elif value == n.value:	            # n의 value와 동일: 탐색 성공				
        return n                        # 결과 반환
    res = search_value_bst(n.left, value) 	# 왼쪽 서브트리에서 탐색
    if res is not None :					# 탐색 성공 하면
       return res							# 결과 반환
    else :									# 왼쪽에서 탐색 실패 하면
       return search_value_bst(n.right, value)  # 오른쪽을 탐색하여 결과 반환

def search_max_bst(n) :	                # 최대 값의 노드 탐색, 최댓값은 가장 오른쪽에 있음
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n) :	                # 최소 값의 노드 탐색, 최솟값은 가장 왼쪽에 있음
    while n != None and n.left != None:
        n = n.left
    return n
#-----------
#P_9.1 최대최소값 찾기. 순환 구조
#-----------

# 삽입 연산: 탐색을 하다 실패한 위치에 삽입
def insert_bst(r, n):                   # 순환 구조
    if n.key < r.key:                   # 삽입할 노드의 키가 루트보다 작으면
        if r.left is None:              # 루트의 왼쪽 자식이 없으면
            r.left = n                  # n은 루트의 왼쪽 자식이 됨.
            return True                 # 삽입
        else:                           # 루트의 왼쪽 자식이 있으면
            return insert_bst(r.left, n)    # 왼쪽 자식에게 삽입하도록 함. 순환
    elif n.key > r.key:                 # 삽입할 노드의 키가 루트보다 크면  
        if r.right is None:             # 루트의 오른쪽 자식이 없으면
            r.right = n                 # n은 루트의 오른쪽 자식이 됨.
            return True                 # 삽입
        else:                           # 루트의 오른쪽 자식이 있으면
            return insert_bst(r.right, n) # 오른쪽 자식에게 삽입하도록 함
    else:                               # 키가 중복되면
        return False                    # 삽입 하지 않음

# 삭제 연산_1 : 부모가 parent인 단말노드 node를 삭제하는 경우 -> 부모 노드의 링크 중 하나를 None 으로 변경 (2가지 경우)
def delete_bst_case1 (parent, node, root):
    if parent is None:          # 부모노드가 없음: 삭제할 단말 노드가 루트이면
        root = None             # 삭제 시 공백 트리가 됨
    else:
        if parent.left == node: # 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None  # 부모의 왼쪽 링크를 None
        else:                   # 오른쪽 자식이면
            parent.right = None # 부모의 오른쪽 링크를 None

    return root                 # 삭제 후, root가 변경될 수도 있으므로 root 반드시 반환

# 삭제 연산_2 : 삭제할 노드의 자식이 하나인 경우 -> 삭제할 노드 대신, 자식을 자신의 부모 노드에 연결 (4가지 경우)
def delete_bst_case2 (parent, node, root):
    if node.left is not None:       # 삭제할 노드가 왼쪽 자식만을 가지는 경우
        child = node.left           # child는 왼쪽 자식
    else:                           # 삭제할 노드가 오른쪽 자식만을 가지는 경우
        child = node.right          # child는 오른쪽 자식

    if node == root:                # 삭제할 노드가 루트이면
        root = child                # 이제 child가 새로운 루트가 됨
    else:
        if node is parent.left:     # 삭제할 노드가 부모의 왼쪽 자식
            parent.left = child     # 부모의 왼쪽 링크를 변경
        else:                       # 삭제할 노드가 부모의 오른쪽 자식
            parent.right = child    # 부모의 오른쪽 링크를 변경

    return root                     # root가 변경될 수도 있으므로 반환

# 삭제 연산_3 : 두 개의 자식을 모두 갖는 노드를 삭제하는 경우 -> 삭제할 노드와 킷값이 가장 '비슷한' 노드 찾기 -> 삭제할 노드의 서브트리에서 최대/최소 키 탐색 이용
# 실제로 삭제되는 것은 삭제할 노드가 아니라, 후계자 노드임에 유의. (후계자 내용으로 교체 하는 코드임)
def delete_bst_case3 (parent, node, root):
    succp = node                    # 후계자의 부모노드
    succ = node.right               # 후계자 노드
    while (succ.left != None):      # 후계자와 부모 노드 탐색 (STEP 1)
        succp = succ
        succ = succ.left            # 이동

    if (succp.left == succ):        # 후계자가 왼쪽 자식이면
        succp.left = succ.right    # 후계자의 오른쪽 자식 연결
    else:                           # 후계자가 오른쪽 자식이면
        succp.right = succ.right    # 후계자의 왼쪽 자식을 연결

    node.key = succ.key             # 후계자의 키와 값을 삭제할 노드에 복사
    node.value = succ.value 
    node = succ;        

    return root                     # 일관성을 위해 root 반환

# 모든 경우에 대한 삭제연산
def delete_bst(root, key):
    if root == None: return None     # 공백 트리

    parent = None                   # 삭제할 노드의 부모 탐색
    node = root                     # 삭제할 노드 탐색
    while node != None and node.key != key: # parent 탐색
        parent = node
        if key < node.key : node = node.left
        else : node = node.right;

    if node == None : return None       		   # 삭제할 노드가 없음
    if node.left == None and node.right == None:    # case1: 단말 노드
        root = delete_bst_case1 (parent, node, root)
    elif node.left==None or node.right==None :	    # case2: 유일한 자식
        root = delete_bst_case2 (parent, node, root)
    else :                                          # case3: 두 개의 자식
        root = delete_bst_case3 (parent, node, root)
    return root                                     # 변경된 루트 노드를 반환


# 이진탐색트리를 이용한 맵
class BSTMap():                    
    def __init__ (self):            
        self.root = None            

    def isEmpty (self): return self.root == None        # 맵 공백 검사
    def clear(self): self.root = None                   # 맵 초기화
    def size(self): return count_node(self.root)        # 레코드(노드) 수 계산

    def search(self, key): return search_bst(self.root, key) # 키를 이용한 탐색
    def searchValue(self, key): return search_value_bst(self.root, key) # 값을 이용한 탐색
    def findMax(self): return search_max_bst(self.root) # 최댓값의 키 가진 노드 탐색
    def findMin(self): return search_min_bst(self.root) # 최솟값의 키 가진 노드 탐색

    def insert(self, key, value=None):                  # 삽입 연산
        n = BSTNode(key, value)                         # 키와 값으로 새로운 노드 생성
        if self.isEmpty() :                             # 공백이면
           self.root = n                                # 루트노드로 삽입
        else :                                          # 공백이 아니면
           insert_bst(self.root, n)                     # insert_bst() 호출

    def delete(self, key):                              # 삭제 연산
        delete_bst (self.root, key)                     # delete_bst() 호출

    def display(self, msg = 'BSTMap :'):                # 맵 출력.(중위순회 사용)
        print(msg, end='')
        inorder(self.root)
        print()

def count_node(n):          # 순환을 이용해 트리의 노드 수를 계산하는 함수
    if n is None:           # n이 None이면 공백 트리이므로 0 반환
        return 0
    else:                   # 좌우 서브트리의 노드 수 + 1 반환 ( 순환 이용 )
        return 1 + count_node(n.left) + count_node(n.right)

def inorder(n):         # 중위 순회 함수
    if n is not None:
        inorder(n.left)             # 왼쪽 서브트리 처리
        print(n.key, end = ' ')    # 루트노드 처리 (화면 출력)
        inorder(n.right)            # 오른쪽 서브트리 처리


#=====================================================
map = BSTMap()
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
#data = [3, 7, 12, 18, 22, 26, 30, 35, 68, 99] #연습문제 9.14
print("[삽입 연산] : ", data)
for key in data :
    map.insert(key)                                   
map.display("[중위 순회] : ")                            

if map.search(26) != None : print('[탐색  26 ] : 성공')
else : print('[탐색  26 ] : 실패')
if map.search(25) != None : print('[탐색  25 ] : 성공')
else : print('[탐색  25 ] : 실패')

map.delete(3);  map.display("[   3 삭제] : ")
map.delete(68); map.display("[  68 삭제] : ")
map.delete(18); map.display("[  18 삭제] : ")
map.delete(35); map.display("[  35 삭제] : ")


