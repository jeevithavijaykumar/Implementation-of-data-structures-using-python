#Stack is a linear data structure which stores element as LIFO. Operations associated with stack are:
# 1. Push
# 2. Pop
# 3.Peek

class Stack():
    max_size = 5
    my_stack = [None]*max_size
    top = -1

    def push(self,num):
        if(self.top < self.max_size-1):
            self.top = self.top+1
            self.my_stack[self.top]=num
            print('Element pushed is ',self.my_stack[self.top])
        else:
            print('Stack is full')

    def pop(self):
        if(self.top>-1):
            print('Element popped is ',self.my_stack[self.top])
            self.top = self.top-1
        else:
            print('Stack is empty')

    def peek(self):
        if(self.top >-1):
            print('The top element is ',self.my_stack[self.top])
        else:
            print('Stack is empty')

s = Stack()
s.push(2)
s.push(3)
s.peek()
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.pop()
s.peek()




