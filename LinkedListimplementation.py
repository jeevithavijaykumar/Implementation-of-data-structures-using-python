#A linked list is represented by a pointer to the first node of the linked list. The first node is called the head of the linked list.
# If the linked list is empty, then the value of the head points to NULL.
#Each node in a list consists of at least two parts:
#A Data Item (we can store integer, strings, or any type of data).
#Pointer (Or Reference) to the next node or An address of another node

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None

    def insertatlast(self,data):
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = Node(data)

    def insertatgivenposition(self,data,position):
        count =1
        temp = self.head
        while(count<position-1):
            temp = temp.next
            count+=1
        tempnode = Node(data)
        tempnext = temp.next
        temp.next = tempnode
        tempnode.next = tempnext

    def deletenode(self,position):
        temp = self.head
        count = 1
        while(count<position-1):
            temp = temp.next
            count+= 1
        delnode = temp.next
        tempnext = delnode.next
        temp.next = tempnext
        del delnode

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = Linkedlist()
llist.head = Node(1)  # Node1 as head node
second = Node(2)  # Creating new node as second node
third = Node(2)   # creating new node as third node
forth = Node(1)
llist.head.next = second
second.next = third
third.next = forth
llist.insertatlast(4)
llist.printlist()
llist.insertatgivenposition(6,3)
llist.printlist()
llist.deletenode(3)
llist.printlist()



















