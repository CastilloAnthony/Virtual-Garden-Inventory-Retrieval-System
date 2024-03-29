'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  10/20/2022
  CS-3100
  Professor Hatem
'''
from abstractClasses import ArrayNodeAbstract, dictAbstract
#from abstractClasses import dictAbstract
#from unsortedLinkedList_Implementation import UnsortedDictAbstract_Imp


class ArrayNode_Imp(ArrayNodeAbstract):

    def __init__(self):
        # Implemented by Anthony Castillo
        self.__key = None
        self.__value = None

    def __del__(
        self
    ):  # The default deconstructor needs to delete all variables handled by this node.
        # Implemented by Sierra
        self.clear()
        del self.__key
        del self.__value

    def __str__(self):
        return str(self.getData())

    def setKey(self, key):  # Sets the node's key
        # Implemented by Sierra
        self.__key = key

    def setData(self, data):  # Set the node's data value
        # Implemented by Sierra
        self.__value = data

    def getKey(self):  # Returns the key
        # Implemented by Anthony Castillo
        return self.__key

    def getData(self):  # Returns the data/crop
        # Implemented by Anthony Castillo
        return self.__value

    def clear(self):  # Sets the node's variables to None
        # Implemented by Sierra
        self.__key = None
        self.__value = None


class SortedDictAbstract_Imp(
        dictAbstract
):  # Inheriting from dict and utilizing some of its functions without modifiying them  (i.e., __len__())

    def __init__(
        self
    ):  # Overloading (overriding) dictAbstract_Imp's __init__() function
        # Implemented by Anthony Castillo
        #self.__head = ArrayNode_Imp() # No head is needed here.
        self.__sortedList = []  # An empty list
        self.__size = 0

    # end __init__()

    def __del__(self):  # Default deconstructor
        # Implemented by Anthony Castillo
        self.clear()  # Clear the array
        del self.__sortedList  # Delete all variables handled by the SortedDictAbstract_Imp
        del self.__size

    #end __del__()

    def __len__(self):  # Returns the length of the sortedList
        return self.__size

    # end __len__()

    def __str__(
        self
    ):  # Returns all of the data contained within the sortedList as a string
        # Might not need, depends on if it runs similarly to the previous one in unsorted
        # Implemented by Sierra
        information = ''
        i = 0
        while (i < self.__size):
            information = information + str(
                self.__sortedList[i].getData()) + '\n'
            i += 1
        return information

    # end __str__()

    def __contains__(
        self, key
    ):  # Needs to return true/false if the key is found inside of the list
        # Implemented by Anthony Castillo
        # Returns true/false if the key is containted within the list
        # this is for 'if ('key' in sortedList):'
        i = 0
        '''
        while (i < self.__size):
            if (self.__sortedList[i].getKey() == key):
                return True
            else:
                i = i + 1
        return False
        '''
        low = 0
        high = self.__size - 1
        while (low <= high):
            if (key.lower() in self.__sortedList[i].getKey().lower()):
                return True
            elif (self.__sortedList[i].getKey() < key):
                low = i + 1
            else:
                high = i - 1
            i = low + (high - low) // 2
        return False

    # end __contains__()

    def __getitem__(self,
                    key):  # Returns the data associated with the requested key
        # Implemented by Anthony Castillo
        # This function is for the "for i in loop" control structure (and similar ones)
        # Must raise an IndexError to stop a for a loop from calling (i.e., when key > self.__size)
        # Needs to be able to handle integers and slices/strings/crops
        #list[5]
        i = 0
        if (isinstance(key, int)):  # If the inputed key is an integer
            if (key > self.__size):  # Key can't be larger than the size
                raise IndexError
            elif (key < 0):  # Negative key is unacceptable
                raise IndexError
            else:
                #print('SortedArray __getitem__: ', key) # Debugging
                return self.__sortedList[key].getData()
            return None
            '''
            while (i < self.__size):
                print('SortedArray __getitem__: ', i) # Debugging
                if (i == key):
                    return self.__sortedList[i].getData() # Returns
                    i = i + 1
                else:
                    i = i + 1
            return None
            '''
        elif (isinstance(key, str)):
            low = 0
            high = self.__size - 1
            while (low <= high):
                if (key.lower() in self.__sortedList[i].getKey().lower()):
                    return self.__sortedList[i].getData()
                elif (self.__sortedList[i].getKey() < key):
                    low = i + 1
                else:
                    high = i - 1
                i = low + (high - low) // 2
            '''
            i = self.__size // 2
            while (key.lower() not in self.__sortedList[i].getKey().lower()):
                print(i)
                if (key.lower() in self.__sortedList[i].getKey().lower()):
                    return self.__sortedList[i].getData()
                elif (key.lower() < self.__sortedList[i].getKey().lower()):
                    i = i // 2
                else:
                    i = i + (i - self.__size) // 2
            '''
            return None
        elif (isinstance(key, slice)
              ):  # If the inputed key is a 'key', crop, or the node itself.
            while (i < self.__size):
                #print('SortedArray __getitem__: ', i) # Debugging
                if (self.__sortedList[i].getKey() == key):
                    return self.__sortedList[i].getData()
                elif (self.__sortedList[i].getData() == key):
                    return self.__sortedList[i].getData()
                elif (self.__sortedList[i] == key):
                    return self.__sortedList[i].getData()
                else:
                    i = i + 1
            return None
        else:
            raise TypeError

    # end __getitem__()

    def __setitem__(self, crop):  # Needs to return true/false
        # Implemented by Anthony Castillo
        # This function isn't really used in our code, but it'll be good practice to setup.
        newNode = ArrayNode_Imp()
        newNode.setKey(crop.get_name())
        newNode.setData(crop)
        self.__sortedList[self.__size] = newNode
        if (self.__sortedList[self.__size].getKey() == crop.get_name()):
            self.__size = self.__size + 1
            self._selfSort()
            return True
        return False

    # end __setitem__()

    def append(
        self, crop
    ):  # Puts crops into a new node and sets their key to the crop's name
        # Implemented by Anthony Castillo
        # Each new node should use the ArrayNode_Imp() class sorted alphabetically by their keys
        # We can sort keys (strings) by comparing them with lesser than (<) greater than (>) and/or (==) to add them alphabetically. Generally if (==) returns true then that means we've got two crops with the same name in our garden but as different entries. Do we want to accept that or decline that?
        # Lower cased strings will be put infront of upper cased strings
        # When inserting between two items, we'll have to shift the whole array down by one to make room for the new item going inbetween the two items. # Not needed since we'll be using a separate sorting function
        # Alternatively, we can append crops to the end/beginning of the array, and then call the sort function to sort the list
        # Don't forget to increment the size of the list by one
        newNode = ArrayNode_Imp()
        newNode.setKey(crop.get_name())  # Setting the Key to the crop's name
        newNode.setData(crop)
        #if (self.__sortedList[self.__size] == None):
        self.__sortedList.append(newNode)
        if (self.__sortedList[self.__size].getKey() == newNode.getKey()):
            self.__size = self.__size + 1
            self._selfSort()
            return True
        #print('Something went wrong while appending. Object: ', self.__size)  # Temporary, delete before submission
        return False

    # end append()

    def remove(self, key):  # Needs to return true/false
        # Implemented by Sierra
        # When we remove a node, we'll want to move all nodes behind it forwards by one
        # Don't forget to decrement the size of the list by one

        #self.__sortedList[self.__value] = self.__value
        #while (i < self.__size):
        #if (self.__sortedList[self.__size].getKey == key)
        #
        #del self.__sortedList[i + ]
        #self.__size = self.__size - 1

        # Implemented by Anthony Castillo
        i = 0
        while (i < self.__size):
            if (self.__sortedList[i].getKey().lower() == key.lower()):
                #temp = self.__sortedList[i]
                #del self.__sortedList[i]
                for j in range(i + 1, self.__size):
                    #print('Moving ', self.__sortedList[j].getKey(), ' from position ', j,' to position ', j-1) # Debugging
                    self.__sortedList[j - 1] = self.__sortedList[j]
                del self.__sortedList[self.__size - 1]
                self.__size = self.__size - 1
                return True
            else:
                i = i + 1
        return False

    # end remove()

    def clear(self):  # Needs to return true/false
        # Implemented by Anthony Castillo
        i = self.__size - 1  # Starting from the last node of the list
        while (i >= 0):
            del self.__sortedList[i]  # Delete the node
            self.__size = self.__size - 1  # Decrement the size
            i = i - 1  # Go to the next to last
        if (self.__size == 0):
            return True
        return False

    # end clear()

    def _selfSort(self):
        return self.shellSort()
        i = 0
        low = None
        high = None
        while (i < self.__size):
            if (low == None):
                low = self.__sortedList[i].getKey()
            if (high == None):
                high = self.__sortedList[i].getKey()
            if (low > self.__sortedList[i].getKey()):
                low = self.__sortedList[i].getKey()
            elif (high < self.__sortedList[i].getKey()):
                high = self.__sortedList[i].getKey()
            i = i + 1
        #return self.quickSort(low, high)

    # end selfSort()

    def shellSort(self):  # Needs to return true/false
        # Implemented by Anthony Castillo
        # Sorting function Using ShellSort to sort the list
        # Should be putting the smaller strings to the front of the list (i.e., apples, bananas, Apples, Bananas, Grapes, Pumpkins, etc.) Lowercase will come to the front followed by upper case
        if (self.__size == 0
            ):  # The list is empty and could be considered as "sorted"
            return True
        elif (self.__size == 1
              ):  # A list with just one node can be considered as "sorted"
            return True
        gap = self.__size // 3
        #gap = 1 # Using 3n+1 for our gap sizes
        #while (gap < self.__size):
        #gap = gap + 3  # using a gap size of 3n+1 i.e., 1,4,7,10,13,16,19,22...,etc.
        #gap = gap - 3  # To ensure gap size is just below the length of the list
        while (gap >= 1):  # WIP, works but how well?
            #print('Gap Size: ', gap) # For testing purposes
            sublistSize = (self.__size // gap
                           )  # Number of items in our list per gap
            #print('Sublist Size: ', sublistSize) # For testing purposes
            for i in range(
                    0, sublistSize - 1
            ):  # When sublistSize = self.__size we don't need to run i on the last element of the list
                #print('i: ', i) # For testing purposes
                for j in range(
                        1, sublistSize - i
                ):  # Starts at 1 because [i+gap*0] would just be [i] and it doesn't make sense to compare [i] to [i]; sublistSize should decrement as i increases so that [i+gap*j] doesn't go out of bounds.
                    #print('j: ', j) # For testing purposes
                    if (self.__sortedList[i].getKey() >
                            self.__sortedList[i + gap * j].getKey()):
                        #print('Swapping: ', self.__sortedList[i].getKey(), ' with ', self.__sortedList[i+gap*j].getKey()) # For testing purposes
                        self.__sortedList[i], self.__sortedList[
                            i + gap * j] = self.__sortedList[
                                i + gap * j], self.__sortedList[i]
            gap = gap - 3
        if (gap <= 1):
            return True
        return False

    # end selfSort()

    def quickSort(self, low,
                  high):  # Should return true/false for success/failure
        # Sorting function using quicksort to sort the list
        # Takes the lowest and highest values when going through the arrays; the test low/high values would be "Apples" and "Zucchini"
        # Implemented by Sierra

        if (low < high):
            partition_index = self.partition(low, high)
            self.quickSort(self.__sortedList, low, high, partition_index - 1)
            self.quickSort(self.__sortedList, partition_index + 1, high)
            return True
        return False

    # end quicksort()

    def partition(self, low, high):  # Should return
        # Partner function for partition for quicksort
        # Implemented by Sierra
        i = low - 1
        pivot = self.__sortedList[high]
        for j in range(low, high):
            if self.__sortedList[j] <= pivot:
                i = i + 1
                self.__sortedList[i], self.__sortedList[j] = self.__sortedList[
                    j], self.__sortedList[i]
                self.__sortedList[i + 1], self.__sortedList[
                    high] = self.__sortedList[high], self.__sortedList[i + 1]
                return (i + 1)

    # end partition()
