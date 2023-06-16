#Implementing quue using two stacks : 
#push(int x) - Pushes element x to the back of the queue.
# pop() - Removes the element from the front of the queue and returns it.
# peek() - Returns the element at the front of the queue.
# boolean empty() - Returns true if the queue is empty, false otherwise.

class Queueusingstacks():
    input =[]
    output = []

    def push(self,x):
        self.input.append(x)

    def pop(self):
        self.peek()
        if(self.input!=[] or self.output!=[]):
            return(self.output.pop())

    def peek(self):
        if(self.output==[] and self.input!=[]):
            while(self.input!=[]):
                self.output.append(self.input.pop())
            return(self.output[-1])
        elif (self.output != []):
            return (self.output[-1])
        else:
            print('Queue is empty')

    def empty(self):
        return((self.output==[] and self.input==[]))

i = Queueusingstacks()
i.push(1)
i.push(2)
i.push(3)
i.push(4)
i.push(5)
print(i.pop())
print(i.peek())
print(i.pop())
print(i.peek())
print(i.pop())
print(i.peek())
print(i.pop())
print(i.pop())
print(i.peek())




