class Node:
    def __init__(self, e, n):
        self.elem = e
        self.next = n


class LinkedList:
    def __init__(self, a):
        self.head = None
        tail = None

        if type(a) == list:
            for i in a:
                node = Node(i, None)
                if self.head is None:
                    self.head = node
                    tail = node

                tail.next = node
                tail = node
    def head(self):
        return self.head

    def PrintLinkedList(self):
        counter = 0
        node = self.head
        while node != None:
            print('[', node.elem, ']-->', end=' ')
            counter += 1
            node = node.next

    # def traverseList(self):
    #     s = ''
    #     temp = self.head
    #     while temp != None:
    #         if temp.next != None:
    #             s += str(temp.element) + " "
    #         else:
    #             s += str(temp.element)
    #         temp = temp.next
    #     return s

    def count(self):
        counter = 0
        node = self.head
        while node != None:
            counter += 1
            node = node.next
        return counter
    
    def indexof(self,idx):
        counter=0
        h=self.head
        while h!=None:
            if idx==counter:
                return h
            counter+=1
            h=h.next


    def remove(self, idx):
        if idx > self.count() or idx < 0:
            return None
        if idx == 0:
            i = self.head.elem
            self.head=self.head.next
            return i
        counter = 0
        i = self.head
        while not(i == None):
            if counter==idx-1:
                x=i.next.elem
                i.next=i.next.next
                return x
            i=i.next
            counter+=1

    def first2last(self):
        i= self.head
        counter=0
        while i!=None:
            if counter == self.count()-2:
                i.next.next=self.head
                self.head = i.next
                i.next=None
            i=i.next
            counter+=1
    def merge2(self,l2):
        pass
    #     h1=self.head
    #     h2=l2.head
    #     counter=0
    #     newhead=None
    #     tail=None
    #     while h1!=None:
    #         count=0
    #         while h2!=None:
    #             if h1.elem == h2.elem:
    #                 node=Node(h2.elem,None)
    #                 if newhead == None:
    #                     newhead=node
    #                     tail=node
    #                 else:
    #                     tail.next=node
    #                     tail=node
    #
    #             count+=1
    #
    #         h1=h1.next
    #         counter+=0
    #         return newhead














a = [1, 2, 3, 3, 4, 5, 6, 7, 8]
l = LinkedList(a)
print()
print("Before Methods: ")
(l.PrintLinkedList())
print()
print()
print("Node Count:", l.count())
print()
print("Removed: [", l.remove(2), ']')
(print("After removing: "),l.PrintLinkedList())
(l.first2last())
print()
(print("last node to the front: "),l.PrintLinkedList())

#another Terminal
b = [2,3,4,5,6]
c = [2,3,5,7]
l1=LinkedList(b)
l2=LinkedList(c)
print("new list representing the intersection of the two lists:")
l1.merge2(l2)

# print((l.traverseList())
