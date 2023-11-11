class LinkedList:
    def __init__( self ):
        self.head = None

    def isEmpty( self ): return self.head == None
    def isFull( self ): return False

    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None :
            node = node.next
            pos -= 1
        return node

    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞에 삽입함
            self.head = Term(elem, self.head)
        else :
            node = Term(elem, before.next)
            before.next = node

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞 노드를 삭제
            if self.head is not None :
                self.head = self.head.next
        elif before.next != None :
            before.next = before.next.next

    def size( self ) :
        node = self.head
        count = 0
        while node is not None :
            node = node.next
            count += 1
        return count

    def __str__( self ) :
        arr = []
        node = self.head
        while node is not None :
            arr.append(node.data)
            node = node.next
        return str(arr)
    
    def replace(self, pos, elem) :
        node = self.getNode(pos)
        if node != None : node.data = elem

    def find(self, val) :
        node = self.head
        while node is not None:
            if node.data == val : return node
            node = node.next
        return node
    
class Term:
    def __init__(self, coef, expo, link = None):
        self.coef = coef # 항의 계수
        self.expo = expo # 항의 지수
        self.next = link
   
class SparsePoly(LinkedList): 
    def __init__(self):
        super().__init__()

    def polynomial(self, newCoef, newExpo):
        newNode = Term(newCoef, newExpo)
        if self.head is None:
            self.head = newNode
        else:
            curNode = self.head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = newNode
        
    def read(self):
        while True:
            coef = input("계수 차수 입력(종료:-1 -1): ")
            if coef == "-1 -1":
                break
            split_input = coef.split()
            if len(split_input) != 2:
                print("잘못된 입력입니다. 다시 입력하세요")
            else:
                self.polynomial(float(split_input[0]), int(split_input[1]))

    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            curNode = self.head
            while curNode is not None:
                    print(str(curNode.coef)+"x^"+str(curNode.expo),end="")
                    curNode = curNode.next
                    if curNode is not None:
                        print(" + ", end = "")
            print("\n", end="")
    
    def __add__(self, polyB):
        polA = self.head
        polB = polyB.head
        result = SparsePoly()

        while polA is not None and polB is not None:
            if polA.expo == polB.expo:
                result.polynomial(polA.coef + polB.coef, polA.expo)
                polA = polA.next
                polB = polB.next
            elif polA.expo > polB.expo:
                result.polynomial(polA.coef, polA.expo)
                polA = polA.next
            else:
                result.polynomial(polB.coef, polB.expo)
                polB = polB.next

        while polA is not None:
                result.polynomial(polA.coef, polA.expo)
                polA = polA.next
        
        while polB is not None:
                result.polynomial(polB.coef, polB.expo)
                polB = polB.next

        return result
        
    def degree(self):      
        if self.head is None:
            return -1
        else:
            return self.head.expo
        
    def evaluate(self, scalar):
        curNode = self.head
        result = 0 
        while curNode is not None:
            result += curNode.coef * (scalar ** curNode.expo)
            curNode = curNode.next
        return result
        
a = SparsePoly()
a.read()
print("\t입력 다항식: ", end="")
a.display()
print("\tA= " + f"{a.degree()}차식 입니다")

b = SparsePoly()
b.read()
print("\t입력 다항식: ", end="")
b.display()
print("\tB= " + f"{b.degree()}차식 입니다")

c = a + b
print(f"\tA= ", end="")
a.display()
print(f"\tB= ", end="")
b.display()
print(f"\tA+B= ", end="")
c.display()
print("\tA+B= " + f"{c.degree()}차식 입니다")

scalar = float(input("scalar 값을 입력하세요: "))
resultA = a.evaluate(scalar)
resultB = b.evaluate(scalar)
resultC = c.evaluate(scalar)

print(f"\tA({int(scalar)})= {resultA}")
print(f"\tB({int(scalar)})= {resultB}")
print(f"\tA+B({int(scalar)})= {resultC}")