with open('test.txt') as f:
    data = [line.strip() for line in f]

data_list = [int(x) if x.isdigit() else x for x in data]

binary_operator = ["+", "-", "/", "%", "*"]
unary_operator = ["++", "--"]

class ArrayList:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.list = []
    def isEmpty(self):
        return len(self.stack) == 0
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("stack empty")
    def print_in_LIFO(self): # stack의 내용을 LIFO 순으로 출력
        temp_stack = self.stack.copy() # stack의 내용을 temp_stack에 저장
        while temp_stack:
            print(temp_stack.pop())

    def calculate(self, inputs):
        for a in inputs:
            if type(a) is int:
                self.stack.append(a)
            else:
                operator = a
                if operator in binary_operator:
                    if len(self.stack) >= 2:
                        x1 = self.stack.pop()
                        x2 = self.stack.pop()
                        if operator == "+":
                            self.stack.append(x2 + x1)
                        elif operator == "-":
                            self.stack.append(x2 - x1)
                        elif operator == "*":
                            self.stack.append(x2 * x1)
                        else:
                            if x1 != 0:
                                self.stack.append(int(x2 / x1))
                            else:
                                print("divide by 0")
                    else:
                        print("stack empty")
                        
                elif operator in unary_operator:
                    if len(self.stack) >= 1:
                        x1 = self.stack.pop()
                        if operator == "++":
                            x1 = x1 + 1
                            self.stack.append(x1)
                        else:
                            x1 = x1 - 1
                            self.stack.append(x1)
                    else:
                        print("stack empty")
                else:
                    if operator == "p":
                        print(self.peek())
                    elif operator == "c":
                        self.stack.clear()
                    elif operator == "l":
                        self.print_in_LIFO()
                    else:
                        exit()
a = ArrayList()
a.calculate(data_list)