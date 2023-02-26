MAX_QSIZE = 10
class CircularQueue :
    def __init__( self ) :		
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE	

    def isEmpty( self ) : return self.front == self.rear # 큐가 비어있으면 True를 아니면 False를 반환한다
    def isFull( self ) : return self.front == (self.rear+1)%MAX_QSIZE # 큐가 가득찼는지 검사
    def clear( self ) : self.front = self.rear # 큐를 공백상태로 만든다.

    def enqueue( self, item ): # item을 큐의 맨 뒤에 추가
        if not self.isFull():			            # 큐가 가득차 있지 않다면
            self.rear = (self.rear+1)% MAX_QSIZE	
            self.items[self.rear] = item		     # 

    def dequeue( self ):  # 큐의 맨 앞에 있는 항목을 꺼내 반환
        if not self.isEmpty():			            # 큐가 비어있지 않다면
            self.front = (self.front+1)% MAX_QSIZE	
            return self.items[self.front] # 	        

    def peek( self ): # 큐의 맨 앞에 있는 항목을 삭제하지 않고 반환한다
        if not self.isEmpty(): # 큐가 비어있지 않다면
            return self.items[(self.front + 1) % MAX_QSIZE] #dequeue 다음이 peek

    def size( self ) : # 큐의 모든 항목들의 개수를 반환
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display( self ):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
						    + self.items[0:self.rear+1]		
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)


class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

def preorder(n) :
    if n is not None :
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)
    return

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)
    return

def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')
    return

def levelorder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
    return

def count_node(n) :
    if n is None : 
        return 0
    else : 
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n) :
    if n is None : return 0
    elif n.isLeaf() : return 1
    else : return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

class BinaryTree:
    def __init__ (self, root = None):
        self.root = root

    def isEmpty( self ): return self.root == None
    def clear( self ) : self.root = None

    def printInOrder(self, msg='   In-Order : '):
        print(msg, end='')
        inorder(self.root)
        print('')
    def printPreOrder(self, msg='  Pre-Order : '):
        print(msg, end='')
        preorder(self.root)
        print('')
    def printPostOrder(self, msg=' Post-Order : '):
        print(msg, end='')
        postorder(self.root)
        print('')
    def printLevelOrder(self, msg='Level-Order : '):
        print(msg, end='')
        levelorder(self.root)
        print('')
#p8.4
def checkBalanced(p) :	#True or False 중에서 선택하시오.
	if p == None : 
		return True

	diff = calc_height(p.left) - calc_height(p.right)
	if diff < -1 or diff > 1 :
		return False

	if not checkBalanced(p.left):
		return False
	return checkBalanced(p.right)

def is_balanced(root) :
    ret = checkBalanced(root)
    if ret==False : 
        print(" 불균형적인 트리입니다.")
    else :
        print(" 균형잡힌 트리입니다.")
    return ret

def testP8_2() :
    c = TNode('C', None, None)
    d = TNode('D', None, None)
    f = TNode('F', None, None)
    #f = TNode('F', TNode('G'), None)
    b = TNode('B', c, d)
    e = TNode('E', None, f)
    # e = TNode('E', f, None)
    a = TNode('A', b, e)

    tree = BinaryTree(a)
    tree.printInOrder   ('   In-Order : ')
    tree.printPreOrder  ('  Pre-Order : ')
    tree.printPostOrder (' Post-Order : ')
    tree.printLevelOrder('Level-Order : ')
    print(" 노드의 개수 = %d" % count_node(tree.root))
    print(" 단말의 개수 = %d" % count_leaf(tree.root))
    print(" 트리의 높이 = %d" % calc_height(tree.root))

    is_balanced(tree.root)
    
    tree.printLevelOrder('Level-Order : ')


testP8_2()
