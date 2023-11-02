import sys
with open('test.txt') as f:
    data = [line.strip() for line in f]

class ArrayStack:
    def __init__(self, capacity) :
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            pass

    def pop(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: 
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass
    def evalPostfix(self, expr):
        for token in expr:
            if token in ('+','-','*','/','%'):
                if self.top >= 1:
                    val2 = self.pop()
                    del self.array[self.top]
                    self.top -= 1
                    val1 = self.pop()
                    del self.array[self.top]
                    self.top -= 1
                    if (token == '+') : self.push(val1 + val2)
                    elif (token == '-'): self.push(val1 - val2)
                    elif (token == '*'): self.push(val1 * val2)
                    elif (token == '/'): 
                        if val2 != 0:
                            self.push(val1 // val2)
                        else:
                            print('divide by 0')
                    else : 
                        if val2 != 0:
                            self.push(val1 % val2)
                        else:
                            print('divide by 0')
                else:
                    print('stack empty')
                
            elif token in ('++', '--'):
                if not self.isEmpty():
                    val2 = self.pop()
                    del self.array[self.top]
                    self.top -= 1
                    if (token == "++"):
                        val2 += 1
                        self.push(val2)
                    else:
                        val2 -= 1
                        self.push(val2)
                else:
                    print('stack empty')
                
            elif token in ('p', 'q', 'l', 'c'):
                if (token == 'p'):
                    if not self.isEmpty():
                        print(self.peek())
                    else:
                        print('stack empty')
                elif (token == 'q'):
                    exit()
                elif (token == 'l'):
                    for i in range(self.top,-1, -1): # top부터 0까지 -1씩 감소
                        print(self.array[i])
                else:
                    self.array.clear()
                    self.array=[None] * self.capacity # array를 clear() 하면 array가 empty 됨. 따라서 새로운 배열 생성
                    self.top = -1 # top을 -1로 초기화
            else:
                self.push(int(token))

a = ArrayStack(len(data))
a.evalPostfix(data)