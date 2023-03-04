class Node:
    def __init__(self,e,n,p):
        self.elem = e
        self.next = n
        self.prev = p

class DoublyList:
    def __init__(self,a):
        self.head = None
        self.tail = None
        if type(a) == list:
            for i in a:
                new = Node(i, None, None)
                if self.head is None:
                    self.head = new
                    self.tail = new
                else:
                    self.tail.next = new
                    self.tail.next.prev = self.tail
                    self.tail = new
        else:
            self.head=a

        # self.tail.next = self.head
        # self.head.prev = self.tail

    def reversedPrint(self):
        print(self.tail.elem, end=' ')
        h1 = self.tail.prev
        while h1!=None:
            print(h1.elem,end=' ')
            h1=h1.prev
        print()

    def forwardPrint(self):
        h1 = self.head
        while h1 is not None:
            print(h1.elem,end=' ')
            h1=h1.next
        print()


    def count(self):
        counter = 1
        h1 = self.tail.prev
        while h1 != None:
            counter+=1
            h1 = h1.prev
        return counter

    def NodeAt(self,idx):
        count = 0
        h = self.head
        while h is not None:
            if idx == count:
                return h.elem
            h = h.next
            count+=1
        return counter

    def Palindrome(self):
        if self.count()%2==0:
            mid = (self.count()//2)-1
            i = mid
            j = mid+1
            count=0
            for x in range(mid+1):
                if self.NodeAt(i) == self.NodeAt(j):
                    count += 1
                    i -= 1
                    j += 1
            if mid+1 == count:
                return True
            return False

        else:
            mid = (self.count()//2)+1
            i = mid-1
            j = mid-1
            count=0
            for x in range(mid):
                if self.NodeAt(i) == self.NodeAt(j):
                    count+=1
                    i-=1
                    j+=1

            if count == mid:
                return True
            return False

    # def reverseList(self):
    #     # head = self.NodeAt(self.count()-1)
    #     # print(head)
    #     newHead = None
    #     newTail = None
    #     n = self.head
    #     while newTail is not None:
    #         node = Node(n,None,None)
    #
    #         newTail=node
    #         newTail.prev = n.next
    #         newTail.prev.next=newTail
    #         newTail=newTail.prev
    #
    #         n=n.next
    #
    #     newHead = newTail
    #
    #     h = newHead
    #     while h!= None:
    #         print(newHead.elem,end=',')
    #         h=h.next
    def reverseList(self):
        newHead = None
        newTail = None
        n = self.head
        while n is not None:
            node = Node(n.elem, None, None)
            if newTail is None:
                newTail = node
            node.next = newHead
            if newHead is not None:
                newHead.prev = node
            newHead = node
            n = n.next
        h = newHead
        print("Reversed List: ",end=" ")
        while h is not None:
            print(h.elem,end='--> ')
            h=h.next
        print()



        # mid = self.count()//2






a= [10,20,30,40,50]
a1 = DoublyList(a)
a1.reversedPrint()
a1.forwardPrint()
print("Count: ",a1.count())
print("Node at index of",a1.NodeAt(2))
print("Palindrome Check:",a1.Palindrome())
a1.reverseList()
# a1.forwardPrint()
