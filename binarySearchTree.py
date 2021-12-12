class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []      
class Node: 
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def printBFS(self):
        if self.data == None:
            print("Tree is empty")
        else:
            nodeQueue = Queue()
            nodeQueue.enqueue(self)
            while nodeQueue.size() > 0:
                currNode = nodeQueue.dequeue()
                print(currNode.data)
                if currNode.left != None:
                    nodeQueue.enqueue(currNode.left)
                if currNode.right != None:
                    nodeQueue.enqueue(currNode.right)

            
    def insert(self, number):
        newNode = Node(number)
        if self.data == None:
            self.data = number
        else:
            if self.data > number:
                if self.left == None:
                    self.left = newNode
                else:
                    self.left.insert(number)
            else:
                if self.right == None:
                    self.right = newNode
                else:
                    self.right.insert(number)
    def findLargest(self):
        if self.right == None:
            return self.data
        else:
            return self.right.findLargest() 
    def printDFS(self):
        if self.left != None:
            self.left.printDFS() 
        print(self.data)
        if self.right != None:
            self.right.printDFS()
                   
n1 = Node(5)
n1.insert(1)
n1.insert(9)
n1.insert(5)
n1.insert(3)
n1.insert(2)
n1.insert(3)
n1.insert(11)
n1.insert(15)
n1.insert(13)

n1.printBFS()
