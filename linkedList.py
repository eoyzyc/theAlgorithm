class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printLinkedList(self):
        temp = self.head
        
        while temp != None:
            print(temp.data)
            temp = temp.next
    def insertAfter(self, currentNode, data):
        newNode = Node(data)
        currentNode.next = newNode
    def insertFront(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def insertLast(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp != None:
                if temp.next != None:
                    temp = temp.next
                else:
                    temp.next = newNode
                    break
    def length(self):
        temp = self.head
        count = 1
        while temp != None:
            if temp.next != None:
                count += 1
            temp = temp.next
        return count 
    def removeFront(self):
        if self.head == None:
            return "Empty List"
        else:
            front = self.head 
            if front.next == None:
                self.head = None
                return"List is now empty"
            else:
                self.head = front.next
                            
numList = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

numList.head = n1
n1.next = n2
n2.next = n3

numList.insertLast("twenty one")
numList.removeFront()
numList.printLinkedList()
