'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  10/12/2022
  CS-3100
  Professor Hatem
'''

from abc import abstractmethod
from abc import ABC

class LinkedList_Node(ABC):
  # Implemented by all group members unanimously during Wednesday lab
    @abstractmethod
    def __init__(self): # Initializes up the variables dataKey, dataValue, nextNode
        pass

    @abstractmethod
    def __del__(self): # Called when the node goes out of scope
        pass
      
    @abstractmethod
    def getKey(self): # Returns the dataKey
        pass

    @abstractmethod
    def getValue(self): # Returns the dataValue
        pass

    @abstractmethod
    def getNext(self): # Returns the nextNode
        pass

    @abstractmethod
    def setKey(self, key): # Sets the dataKey
        pass

    @abstractmethod
    def setValue(self, value): # Sets the dataValue
        pass

    @abstractmethod
    def setNext(self, node): # Sets the nextNode
        pass

    @abstractmethod
    def clear(self): # Clears the data set in the data fields
        pass

class GardenAbstract(ABC):

    @abstractmethod
    def loadDatabase(
        self, location
    ):  # Given a location, the function will import all the data from the file. Returns either an empty list or a list of the lines that could not be imported.
        pass

    @abstractmethod
    def saveToFile(
        self, location
    ):  # Attempts to save the dictionary to the given location, returns true/false on success/failure
        pass

    @abstractmethod
    def insertNew(
        self, name, cropType, growingSeason, harvestSeason, averageGrowingTime,
        averageYield, diseases, nutritionalValue, soilWaterMoisture
    ):  # allows user to add a new crop; returns true/false for success/failure
        pass

    @abstractmethod
    def modifyCrop(
        self, name, element, replacement
    ):  # allows the user to modify crop information already present in the dictionary; returns true/false for success/failure
        pass

    @abstractmethod
    def removeCrop(
        self, name
    ):  # Removes the specified crop from the dictionary; returns success/failire
        pass

    @abstractmethod
    def searchForCrop(self, name):
        # Function that searches our data structure for the specified crop and then returns that crop's information; returns string of desired crop for success
        pass

    @abstractmethod
    def searchByElements(
        self, element, information
    ):  # allows the user to search for a group of crops based on a specific element or piece of information
        pass

class dictAbstract(ABC):
    @abstractmethod
    def __init__(self): # The default Initializer
        pass
      
    @abstractmethod
    def __del__(self): # The default Deconstructor
        pass
      
    @abstractmethod
    def __len__(self): # Returns the length of the list
        pass

    @abstractmethod
    def __str__(self): # Returns all of the content of the tree. Might not be needed...
        pass

    @abstractmethod
    def __contains__(self, key): # Defines how the class behaves when at the right side of the "in" operator (or "not in")
        # i.e., if (key in dic): { do this }
        pass

    @abstractmethod
    def __getitem__(self, key): # Returns the value paired with the specific key that was given to the function. 
        # value = self[key]
        pass

    @abstractmethod
    def __setitem__(self, crop): # Adds a new crop to the end of the dictionary for the list['key'] = object format
        pass
      
    @abstractmethod
    def append(self): # Adds a new crop to the end of the dictionary
        pass

    @abstractmethod
    def remove(self, index): # Removes a specific crop at the given index from the dictionary
        pass

    @abstractmethod
    def clear(self):
        pass
    # What else does a dictionary need to be able to do?

class ArrayNodeAbstract(ABC):
    def __init__(self): # The default initalizer
        # i.e., self.__head = Class()
        pass

    def __del__(self): # The default deconstructor, needs to del the node's variables
        # i.e., del self.__head
        pass
      
    def setKey(self, key): # Needs to set the node's key
        pass

    def setData(self, data): # Needs to set the node's data
        pass

    def getKey(self): # Returns the key
        pass

    def getData(self): # Returns the data/crop
        pass

    def clear(self): # Needs clear all of the data in 
        pass