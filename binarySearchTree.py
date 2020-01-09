#This is the node construction class. Nodes are elements of the tree
class Node:

    #Initilization method
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def Insert(self, data):
    
        #Data is the intial value passed in, this block checks to see if the node should go to the left. 
        if self.data:
            if data < self.data:
                if self.left is None:  
                    self.left = Node(data)
                else:
                    self.left.Insert(data)
            #Determing if it should go to the right (its greater)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else: 
                    self.right.Insert(data)
        else:
            self.data = data

    #This method will find any supplied value in the search tree, by comparing the values from left to right
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

    #Printing the value if a supplied value is located
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


#Getting input from the user and inserting values
initRoot = input("Enter the initial value for the root: ") 
root = Node(initRoot)
 
i = 0
while i <= 3:
    insertion = input("Enter a value to insert: ")
    root.Insert(insertion)
    i = i + 1
i = 0
while i <= 3:
    insertion = input("Enter a value to find: ")
    root.findval(insertion)
    i = i + 1