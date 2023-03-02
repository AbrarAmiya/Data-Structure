class Node:
    def __init__(self,e,n):
        self.elem=e
        self.next=n
class LinkedList:
    def __init__(self,a):
        self.head=None
        self.tail=None
        n=a[1]
        if type(a) == list:
            for i in a:
                if self.head == None:
                    node=Node(i,None)
                    self.head = node
                    self.tail = node
                else:
                    node=Node(i,n)
                    self.tail.next=node
                    self.tail=node


        else:
            self.head = a

    def Print(self):
        print(self.head.elem,end="--> ")
        print(self.head.next.elem, end="--> ")
        h=self.head.next.next
        while h!=self.head.next:
            print(h.elem,end='--> ')
            h=h.next
        print()

    # def count(self):
    #     count=1
    #     h = self.head.next
    #     while h != self.head:
    #         count+=1
    #         h = h.next
    #     return count


a=[8, 12, 10, 5, 4, 1,6,3]
h1=LinkedList(a)
h1.Print()
# print(h1.count())