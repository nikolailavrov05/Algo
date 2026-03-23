
class Node:
    def __init__(self, val = 0, next_node = None):
        self.data = val
        self.next = next_node

class LinkedList:
    def __init__(self, head = None, tail = None, size = 0):
        self.head = head
        self.tail = tail
        self.size = size

linkedlistA = LinkedList()

def AddNewHead(linkedlist: LinkedList, el):
    node = Node(el)
    if (linkedlist.head == None):
        linkedlist.tail = node
    else:
        node.next = linkedlist.head
    linkedlist.head = node
    linkedlist.size += 1

def AddnewTail(linkedlist: LinkedList, el):
    node = Node(el)
    if (linkedlist.tail == None):
        linkedlist.head = node
    else:
        linkedlist.tail.next = node
    linkedlist.tail = node
    linkedlist.size += 1

AddNewHead(linkedlistA, 4)
AddnewTail(linkedlistA, 1)
AddnewTail(linkedlistA, 8)
AddnewTail(linkedlistA, 4)
AddnewTail(linkedlistA, 5)

linkedlistB = LinkedList()
AddNewHead(linkedlistB, 5)
AddnewTail(linkedlistB, 6)
AddnewTail(linkedlistB, 1)
AddnewTail(linkedlistB, 8)
AddnewTail(linkedlistB, 4)
AddnewTail(linkedlistB, 5)

def peresechenie(headA, headB):

    if headA is None or headB is None:
        return None
    currentA = headA
    currentB = headB

    while True:
        if currentA is None and currentB is None:
            return None
        if currentA is None:
            currentA = headB
            currentB = currentB.next
            continue
        if currentB is None:
            currentB = headA
            currentA = currentA.next
            continue
        if currentA.data == currentB.data:
            return currentA.data
        currentA = currentA.next
        currentB = currentB.next


print(linkedlistA.head.data, linkedlistA.tail.data, linkedlistA.size)
print(linkedlistB.head.data, linkedlistB.tail.data, linkedlistB.size)

print(peresechenie(linkedlistA.head, linkedlistB.head))