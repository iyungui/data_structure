MAX_QSIZE = 10				    
class CircularQueue :
    def __init__( self ) :		
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE	

    def isEmpty( self ) : return self.front == self.rear
    def isFull( self ) : return self.front == (self.rear+1)%MAX_QSIZE
    def clear( self ) : self.front = self.rear

    def enqueue( self, item ):
        if not self.isFull():			            
            self.rear = (self.rear+1)% MAX_QSIZE	
            self.items[self.rear] = item		    

    def dequeue( self ):
        if not self.isEmpty():			            
            self.front = (self.front+1)% MAX_QSIZE	
            return self.items[self.front]	        

    def peek( self ):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size( self ) :
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display( self ):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]		
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)


q = CircularQueue()			       
for i in range(8): q.enqueue(i)		
q.display()			            	
for i in range(5): q.dequeue();		
q.display()
for i in range(8,14): q.enqueue(i)	
q.display()

class CircularDeque(CircularQueue) :	      # CircularDeque에서 상속     
    def __init__( self ) :		              # CircularDeque의 생성자
        super().__init__()		              # 부모 클래스의 생성자를 호출함    

    def addRear( self, item ): self.enqueue(item ) # enqueue 호출
    def deleteFront( self ): return self.dequeue() # 반환에 주의
    def getFront( self ): return self.peek()	   # 반환에 주의
   
    def addFront( self, item ):			           # 새로운 기능: 전단 삽입
        if not self.isFull():
            self.items[self.front] = item          # 항목 저장
            self.front = self.front - 1		       # 반시계 방향으로 회전
            if self.front < 0 : self.front = MAX_QSIZE - 1

    def deleteRear( self ):			               # 새로운 기능: 후단 삭제
        if not self.isEmpty():
            item = self.items[self.rear];          # 항목 복사
            self.rear = self.rear - 1		       # 반시계 방향으로 회전
            if self.rear < 0 : self.rear = MAX_QSIZE - 1
            return item			                   # 항목 반환

    def getRear( self ):			               # 새로운 기능: 후단 peek
        return self.items[self.rear]
        

dq = CircularDeque()		                       # 덱 객체 생성, f=r=0
for i in range(9):			                       # i : 0,1,2, ... 8
	if i%2==0 : dq.addRear(i)		               # 짝수는 후단에 삽입:
	else : dq.addFront(i)		                   # 홀수는 전단에 삽입
dq.display()				                       # front=6, rear=5
for i in range(2): dq.deleteFront()	               # 전단에서 두 번의 삭제: f=8
for i in range(3): dq.deleteRear()	               # 후단에서 세 번의 삭제: r=2
dq.display()
for i in range(9,14): dq.addFront(i)               # i : 9,10,...13 : f=3
dq.display()

class PQueueSorted :
    def __init__( self ):
        self.items = []

    def isEmpty( self ):
        return len( self.items ) == 0
    def size( self ): return len(self.items)
    def clear( self ): self.items = []

    def enqueue( self, item ):
        pos = len(self.items)-1
        while pos > 0 and self.items[pos] > item :
            pos -= 1
        self.items.insert(pos+1, item)

    def dequeue( self ):
        return self.items.pop(-1)

    def peek( self ):
        return self.items[-1]

q = PQueueSorted()
q.enqueue( 1 )
q.enqueue( 34 )
q.enqueue( 18 )
q.enqueue( 27 )
q.enqueue( 45 )
q.enqueue( 15 )

print("PQueue:", q.items)
while not q.isEmpty() :
    print("Max Priority = ", q.dequeue()	)





