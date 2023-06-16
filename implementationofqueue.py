#Implementation of FIFO queque. Operations associated with queque are:
#Insert
#Delete
#Front
#Rear

class Queue():
    max_size=5
    q=[None]*max_size
    f=-1
    r=0

    def insert(self,val):
        if(self.f<self.max_size-1):
            self.f=self.f+1
            self.q[self.f]=val
        else:
            print('Queue is full')

    def delete(self):
        if(self.r<=self.f and self.r<=self.max_size-1):
            self.q[self.r]=0
            self.r=self.r+1
        else:
            print('Queue is empty')

    def front(self):
        if(self.r<=self.f):
            print('front element is ',self.q[self.r])
        else:
            print('Queue is empty')

    def rear(self):
        if(self.r<=self.f):
            print('rear element is',self.q[self.f])
        else:
            print('Queue is empty')

q=Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.front()
q.rear()
q.delete()
q.front()
q.rear()
q.delete()
q.front()
q.rear()
q.insert(1)
q.delete()
q.front()
q.rear()
q.delete()
q.front()
q.rear()
q.delete()
q.front()
q.rear()
q.delete()





