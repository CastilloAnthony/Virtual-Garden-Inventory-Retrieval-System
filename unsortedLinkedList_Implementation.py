'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  10/12/2022
  CS-3100
  Professor Hatem
'''
# File was previously was named: abstractClassesImplementation.py
from abstractClasses import LinkedList_Node, dictAbstract
#from abstractClasses import dictAbstract
class LinkedListNode_Imp(LinkedList_Node):
    def __init__(self): # Initializes up the variables dataKey, dataValue, nextNode
        # Implemented by Anthony Castillo
        self.__dataKey = None
        self.__dataValue = None
        self.__nextNode = None

    def __del__(self): # The default Deconstructor
        # Implemented by Anthony Castillo
        del self.__dataKey
        del self.__dataValue
        del self.__nextNode
      
    def getKey(self): # Returns the dataKey
        # Implemented by Anthony Castillo
        return self.__dataKey

    def getValue(self): # Returns the dataValue
        # Implemented by Anthony Castillo
        return self.__dataValue

    def getNext(self): # Returns the nextNode
        # Implemented by Anthony Castillo
        return self.__nextNode

    def setKey(self, key): # Sets the dataKey
        # Implemented by Anthony Castillo
        self.__dataKey = key

    def setValue(self, value): # Sets the dataValue
        # Implemented by Anthony Castillo
        self.__dataValue = value

    def setNext(self, node): # Sets the nextNode
        # Implemented by Anthony Castillo
        self.__nextNode = node

    def clear(self):
        # Implemented by Anthony Castillo
        self.__dataKey = None
        self.__dataValue = None
        self.__nextNode = None

class UnsortedDictAbstract_Imp(dictAbstract): #
    def __init__(self):
        # Implemented by Anthony Castillo
        self.__head = LinkedListNode_Imp()
        self.__size = 0

    def __del__(self): # The default Deconstructor
        # Implemented by Anthony Castillo
        self.clear() # Clear the LinkedList
        del self.__head # Delete all variable handled by the UnsortedDictAbstract_Imp
        del self.__size
      
    def __len__(self): 
        # Returns the length/size of the list
        # Implemented by Anthony Castillo
        return self.__size

    def __str__(self):
        # Returns a string of all the data contained within the nodes
        # Implemented by Anthony Castillo
        information = ''
        currentNode = self.__head
        i = 0
        while (i < self.__size):
            information = information + str(currentNode.getValue()) + '\n'
            if (currentNode.getNext() != None):
                currentNode = currentNode.getNext()
            i = i + 1
        return information

    def __contains__(self, key):
        # Returns true/false if the key is contained within the list
        # Implemented by Anthony Castillo
        currentNode = self.__head
        i = 0
        while (i < self.__size):
            if (currentNode.getKey() == key):
                return True # The requested key was found
            else:
                currentNode = currentNode.getNext()
                i = i + 1
        return False # The key was not found

    def __getitem__(self, key): # variable = list['key']
        # Returns the dataValue for the given key
        # Implemented by Anthony Castillo
        currentNode = self.__head
        i = 0
        if (isinstance(key, int)): # If the key is an integer (for loop)
            if (key >= self.__size): # If the for loop goes out of bounds
                raise IndexError
            elif (key < 0): # If the key is negative (also out of bounds)
                raise IndexError
            while (i < self.__size):
                if (i == key):
                    return currentNode.getValue()
                else:
                    currentNode = currentNode.getNext()
                    i = i + 1
            return None # Node wasn't found
        elif (isinstance(key, slice)): # WIP; also might not be needed
            while (i < self.__size):
                #print(str(currentNode))
                if (currentNode.getKey() == key):
                    return currentNode.getValue() # The node that the key is paired with
                else:
                    currentNode = currentNode.getNext()
                    i = i + 1
            return None # Node wasn't found
          
    def __setitem__(self, crop): # list['key'] = object
        # Sets the crop into the list
        # Implemented by Anthony Castillo
        # This function is not currently used
        currentNode = self.__head
        i = 0
        while (i < self.__size):
            if (currentNode.getNext() == None):
                newNode = LinkedListNode_Imp()
                newNode.setKey(crop.get_name())
                newNode.setValue(crop)
                currentNode.setNext(newNode)
                self.__size = self.__size + 1
                return True # Crop was added
            else:
                currentNode = currentNode.getNext()
            i = i + 1
        return False # Crop wasn't added
              
    def append(self, crop): # Appends a new crop to the end of the list
        # Implemented by Anthony Castillo
        currentNode = self.__head
        if (self.__head.getValue() == None): # If there is no head, then we'll set the head first
            self.__head.setKey(crop.get_name())
            self.__head.setValue(crop)
            self.__size = self.__size + 1
        else: # Otherwise we'll append it to the end of the list
            newNode = LinkedListNode_Imp()
            newNode.setKey(crop.get_name()) # We'll use crop names for our keys
            newNode.setValue(crop) # And the value will be the crop itself
            i = 0
            while(i <= self.__size):
                if (currentNode.getNext() == None):
                    currentNode.setNext(newNode)
                    self.__size = self.__size + 1
                    return True # Crop was added
                else:
                    currentNode = currentNode.getNext()
                i = i + 1
        return False # Crop wasn't added

    def remove(self, key): # Removes the crop that has the matching key
        # Implemented by Anthony Castillo
        currentNode = self.__head
        preNode = None
        i = 0
        while (i < self.__size):
            if (currentNode.getKey().lower() == key.lower()): # This is the node we want to remove
                if (preNode == None): # Removing the head
                    if (currentNode.getNext() != None): # Move the head forwards by one node
                        self.__head = currentNode.getNext()
                    removal = currentNode # Removing the "old" head
                    removal.clear()
                    self.__size = self.__size - 1 # Decrement Size
                    return True
                elif (currentNode.getNext() == None): # Removing the tail
                    removal = currentNode
                    removal.clear()
                    del removal # Deletes the node entirely
                    preNode.setNext(None)
                    self.__size = self.__size - 1
                    return True # Crop was removed and cleared
                else: # Removing any inbetween the two
                    removal = currentNode # We want to clear this node
                    preNode.setNext(currentNode.getNext()) # Sets the previous nodes nextNode to the next node
                    removal.clear() # Sets all the parts of a node to None
                    del removal # Deletes the node entirely
                    self.__size = self.__size - 1
                    return True # Crop was removed and cleared
            else:
                preNode = currentNode
                currentNode = currentNode.getNext()
                i = i + 1
        return False

    def clear(self): # Clears the entire list
        # Implemented by Anthony Castillo
        if (self.__head.getKey() == None):
            return True # List is already empty
        head = self.__head
        currentNode = self.__head
        preNode = None
        while (head.getNext() != None): # If the node after the head is None then the list is almost empty
            if (currentNode.getNext() == None): # If the next node is equal to None then this is the tail node
                currentNode.clear() # Clear the current node
                del currentNode # Deletes the node entirely
                preNode.setNext(None) # Set the previous node's next to None
                currentNode = head # Go back to the head
                self.__size = self.__size - 1 # Decrement the list size
            else:
                preNode = currentNode # Move forwards thru the list
                currentNode = currentNode.getNext() # Move forwards thru the list
        if (head.getNext() == None): # Now we'll empty the head
            head.clear()
            self.__size = self.__size - 1 # Decrement the size (Note: This sets the size to -1)
            return True # List is now empty
        return False

