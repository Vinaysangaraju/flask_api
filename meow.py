class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
     
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.next = n2
n2.next = n3

temp = n1
while temp:
    print(temp.data, end="->")
    temp = temp.next