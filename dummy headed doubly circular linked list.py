class Node:
    def __init__(self,e,n,p):
        self.elem = e
        self.next = n
        self.prev = p

class DoublyList:
    def __init__(self,a):
        self.head = None
        self.tail = None
        for i in a:
            new = Node(i,None,None)
            if self.head is None:
                self.head = new
                self.tail = new
            else:
                self.tail.next = new
                self.tail.next.prev = self.tail
                self.tail = new

        self.tail.next = self.head
        self.head.prev = self.tail

    def reversedPrint(self):
        print(self.head.prev.elem, end=' ')
        h1=self.head.prev.prev
        while h1!=self.head.prev:
            print(h1.elem,end=" ")
            h1=h1.prev
        print()

    def forwardPrint(self):
        h=self.head.next
        while h != self.head:
            print(h.prev.elem,end=' ')
            h=h.next
        print(self.head.prev.elem)
        print()

    def Highest(self):
        high = self.head.elem
        h= self.head.next
        while h!=self.head:
            if h.elem>high:
                high = h.elem
            h=h.next
        print("Highest:",high)

    def leftRotate(self,k):
        for i in range(k):
            self.head = self.head.next
        return self.head

    def rightRotate(self,k):
        for i in range(k):
            self.head = self.head.prev
        return self.head













a= [10,20,30,40,50]
a1 = DoublyList(a)
a1.reversedPrint()
print("Forward  Printing: ",end=' ')
a1.forwardPrint()
a1.Highest()
a1.leftRotate(2)
print("Rotating to Left k-times: ")
a1.forwardPrint()
a1.rightRotate(3)
print("Rotating to Right k-times: ")
a1.forwardPrint()