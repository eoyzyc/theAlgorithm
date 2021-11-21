class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def clear(self):
        self.items = []
    def printStack(self):
        print(self.items)
        
class groceryList:
    def __init__(self):
        self.items = []
        self.history = Stack()  
    
    def add(self, item):
        self.history.push(self.items)
        self.items = self.items[:]   
        self.items.append(item)
        print("Added: "+str(item))
        
    def remove (self, item) :
        self.history.push (self.items)
        self.items = self.items[:] 
        self.items.remove (item)
        print ("Removed: "+ str(item))
        
    def undo (self):
        self.items = self.history.pop()
        print ("Undo command used.")

    def view (self) :
        print (self.items)
        
    def viewHistory (self) :
        self.history.printstack()

glist = groceryList()
glist.add ("chimkin")
glist.add ("unagi" )
glist.add ("sosig")
glist.add ("human beans")
glist.view()
glist.undo()
glist.view()
glist.remove("chimkin")
glist.view()
glist.undo()
glist.view()
