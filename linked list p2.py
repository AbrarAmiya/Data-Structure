class Node:
    def __init__(self,e,n):
        self.elem=e
        self.next=n
class LinkedList:
    def __init__(self,a):
        self.head=None
        self.tail=None
        if type(a) == list:
            for i in a:
                node=Node(i,None)
                if self.head == None:
                    self.head = node
                    self.tail = node
                else:
                    self.tail.next = node
                    self.tail = node
        else:
            self.head = a
    def indexof(self,elem):
        h=self.head
        idx=0
        while h!=None:
            if h.elem==elem:
                return idx
            idx+=1
            h=h.next
    def nodeAt(self,idx):
        if idx>self.count() or idx<0:
            return None
        h=self.head
        count=0
        while h!=None:
            if count==idx:
                return h
            count+=1
            h=h.next


    def count(self):
        h=self.head
        count=0
        while h!=None:
            count+=1
            h=h.next
        return count

    def printList(self):

        h = self.head
        while h!= None:
            print('|',h.elem,'|-->',end =' ')
            h=h.next
        print()

    def remove(self,idx):

        if idx>self.count() or idx<0:
            return None
        else:
            if idx == 0:
                x= self.head.elem
                self.head=self.head.next
                return x
            elif idx>1 and idx<self.count()-1:
                prev = self.nodeAt(idx - 1)
                rmv = self.nodeAt(idx)
                prev.next = rmv.next
            elif idx == self.count()-1:
                prev = self.nodeAt(self.count()-2)
                prev.next=None


            return rmv.elem

    def insert(self,elem,idx):
        if idx == 0:
            new = Node(elem,self.head)
            self.head = new
        if idx < self.count() and idx>1:
            prev = self.nodeAt(idx-1)
            current = self.nodeAt(idx)
            new=Node(elem,None)
            prev.next = new
            new.next=current
        elif idx==self.count():
            new = Node(elem, None)
            prev = self.nodeAt(self.count()-1)
            prev.next = new
        else:
            print("Error -- Invalid ")

        return self.head

    def evenRemove(self):
        pred = None
        h = self.head
        while h!=None:
            if h.elem%2==0:
                if pred==None:
                    self.head=h.next
                else:
                    pred.next=h.next
                h = h.next


            else:
                pred=h
                h=h.next
        return self.head

    def Middle(self):
        l=self.count()

        if l%2==0:
            point=(l/2)
            # print(point)
        else:
            point=l//2
            # print(point)

        return self.nodeAt(point)


        # while s
        #else:
        # pred.next=h.next

    def KnodeSwap(self,k):
        last=((self.count()-1)-k)
        first = self.nodeAt(k)
        end = self.nodeAt(last)
        print(first.elem,"----",end.elem)

        if k==0:
            self.remove(k)
            self.insert(end.elem,k)
            #removing prev head

            self.remove(end)
            #self.insert(first.elem,last)


        return self.head


a=[10,20,30,40,50,60,70,80]
h1=LinkedList(a)
print(h1.nodeAt(1).elem)
print(h1.indexof(10))
# print("Middle point: ",h1.Middle())
print('Middle: ',h1.Middle().elem)
h1.printList()
# h1.evenRemove()

print(h1.remove(3))
h1.printList()
h1.insert(77,7)
h1.printList()
h1.KnodeSwap(0)
h1.printList()
