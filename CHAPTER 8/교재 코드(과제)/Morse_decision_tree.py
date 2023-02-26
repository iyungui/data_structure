class TNode:        # 이진트리를 위한 노드 클래스
    def __init__ (self, data, left, right):     # 생성자
        self.data = data        # 노드의 데이터
        self.left = left        # 왼쪽 자식을 위한 링크
        self.right = right      # 오른쪽 자식을 위한 링크

# 모르스 코드표
table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

# 모르스 코드표를 이용해 결정트리를 만들고, 루트 노드 반환
def make_morse_tree():      
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1]        # 각 tp의 첫번째 인덱스는 '모르스 코드'를 나타냄
        node = root         # 루트 노드 부터.
        for c in code:      # 모르스 코드에 대하여, 맨 마지막 문자 이전까지. 이동
            if c == '.':     # . 만나면 왼쪽으로 이동
                if node.left == None:   # 비었다면 빈 노드 만들기
                    node.left = TNode(None, None, None)
                node = node.left # 왼쪽으로 이동
            elif c == '-':  # - 만나면 오른쪽으로 이동
                if node.right == None:
                    node.right = TNode(None, None, None)
                node = node.right   # 오른쪽으로 이동
                
        node.data = tp[0]       # 각 코드의 알파벳
    return root
    

def decode(root, code):     # 모르스 코드 -> 문자 찾기
    node = root
    for c in code:          # 모르스 코드에서, 맨 마지막 문자 이전까지 이동
        if c == '.': node = node.left   # . 만나면 왼쪽으로
        elif c== '-': node = node.right # - 만나면 오른쪽으로 이동
    return node.data            # 최종 노드가 가지고 있는 데이터 즉, 문자 반환

def encode(ch):             # 문자 -> 모르스 코드 찾기
    idx = ord(ch)-ord('A')  # 리스트에서 해당 문자의 인덱스
    return table[idx][1]    # 해당 문자의 모르스 코드 반환


# 테스트 코드--------
morseCodeTree = make_morse_tree()
str = input("입력 문장 : ")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("Morse Code: ", mlist)
print("Decoding  : ", end='')
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')
print()
    