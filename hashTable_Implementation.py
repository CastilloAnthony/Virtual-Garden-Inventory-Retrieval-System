'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  11/09/2022
  CS-3100
  Professor Hatem
'''
from abstractClasses import dictAbstract
class hashTable_Imp(dictAbstract):
    def __init__(self, tableSize = None): # Default Initializer
        # Implemented by Anthony Castillo
        self.__size = 0 # Number of objects in the table
        if (isinstance(tableSize, int)):
            self.__maxSize = tableSize # Maximum possible size of the table
        else:
            self.__maxSize = 100 # Supports up to 100 items by default
        self.__hashTable = [None] * self.__maxSize
    # end __init__()
      
    def __del__(self): # Default deconstructor
        # Implemented by Anthony Castillo
        del self.__size
        del self.__maxSize
        del self.__hashTable
    # end __del__()
      
    def __str__(self): # Returns all of the crop information contained within the list
        # Implemented by Anthony Castillo
        info = ''
        for i in self.__hashTable:
            if (i == None):
                continue
            else:
                info = info + str(i) + '\n'
        return info
        ''' # WIP below
        j = 0 
        sortedInfo = ''
        sortedArray = [None] * self.__maxSize
        while (j < self.__maxSize): # Attempting to sort output, WIP
            if (self.__hashTable[j] == None):
                continue
            else:
                largest = self.__hashTable[j]
                for k in self.__hashTable:
                    if (k == None):
                        continue
                    elif (k == 'Tombstone'):
                        continue
                    elif (largest == sortedArray[k]):
                        continue
                    elif (largest.get_name() > j.get_name()):
                        largest = j
                
            sortedArray[j] = largest
            sortedInfo = sortedInfo + str(j) + '\n'
            j = j + 1
        return sortedInfo
        '''
    # end __str__()
      
    def __len__(self): # Returns the length of the table
        # Implemented by Anthony Castillo
        return self.__size
    # end __len__()
      
    def __contains__(self, key): # Returns true/false if the key is contained in the table
        # Implemented by Sierra
        i = 0
        while (i < self.__maxSize):
          if (self.__hashTable[i] == None):
              i = i + 1
          elif (self.__hashTable[i] == 'Tombstone'):
              i = i + 1
          elif (self.__hashTable[i].get_name().lower() == key.lower()):
              return True
          else: 
              i = i + 1
        return False
    # end __contains__()
      
    def __getitem__(self, key): # Returns the item/crop that has the matching key
        # Implemented by Sierra and Anthony Castillo
        # For integer keys we'll be iterating thru the entire table and only returning the independent items/crops within the table.
        # For string keys, I recommend hashing the string key first and checking that location. If its not at that location then try iterating thru the table starting at that location and keeping in mind that the hash2() function is incrementing in threes. - Anthony
        # Directions:
        # hash the key and 
        # check that key's specific location (if/else statement?)
        # (else -> iterate through the table from that location in hash() and hash2(); hash2() WILL INCREMENT BY THREES)
        #increment by 1 through hash(), then by 3 in hash2(), then 1 in hash2()
        if (self.__size == 0): # If the table is empty then nothing can ever be found
            raise IndexError
        i = 0
        if (isinstance(key, int)): # If key is an integer
            #print('Searching by integer.') # Debugging
            if (key >= self.__size):
                raise IndexError
            elif (key < 0):
                raise IndexError
            else:
                finds = 0
                while (i < self.__maxSize):
                    if (self.__hashTable[i] != None): # Always check for NoneType first
                        if (self.__hashTable[i] != 'Tombstone'): # Then check for the string 'Tombstone'
                            if (finds == key): # Anything else must be crop object
                                #print(self.__hashTable[i]) # Debugging
                                return self.__hashTable[i]
                            else:
                                finds = finds + 1
                    i = i + 1    
                '''  # Depreciated
                    if (self.__hashTable[i] == None): # Depreciated # Always check for NoneType before anything else
                        pass
                    elif (self.__hashTable[i] == 'Tombstone'): # Depreciated # Always check for the string 'Tombstone' before assuming the object is a crop
                        pass
                    elif (finds != key): # Depreciated # key = 0-self.__size #self.__size-key
                        finds = finds + 1
                    if (finds == key): # Depreciated
                        if (self.__hashTable[i] != None):
                            if (self.__hashTable[i] != 'Tombstone'):
                                return self.__hashTable[i]
                        #print(finds, key, i, self.__hashTable[i]) # Debugging
                        
                    i = i + 1
                '''
        elif (isinstance(key, str)): # If key is a string
            tableSpace = self.hash(key)
            if (self.__hashTable[tableSpace] == None): # If the first slot the hash function brings us to is empty then the key cannot possibly be contained within the table
                raise self.__hashTable[tableSpace]
            for i in range(0, self.__maxSize): # Increment by threes
                if (self.__hashTable[(tableSpace + (i*3)) % self.__maxSize] == None): # If we encounter a None object now then that means that the key will never be found
                    raise self.__hashTable[tableSpace]
                elif (self.__hashTable[tableSpace + (i*3) % self.__maxSize] == 'Tombstone'): # Continue iterating when we encounter tombstones
                    continue
                elif (self.__hashTable[(tableSpace + (i*3)) % self.__maxSize].get_name().lower() == key.lower()): # This will be our match
                    return self.__hashTable[(tableSpace + (i*3) % self.__maxSize)]
                else:
                    continue
            for i in range(0, self.__maxSize): # Increment by ones
                if (self.__hashTable[(tableSpace + i) % self.__maxSize] == None):
                    continue
                elif (self.__hashTable[(tableSpace + i) % self.__maxSize] == 'Tombstone'):
                    continue
                elif (self.__hashTable[(tableSpace + i) % self.__maxSize].get_name().lower() == key.lower()):
                    return self.__hashTable[(tableSpace + i) % self.__maxSize]
            raise IndexError
        elif (isinstance(key, slice)): # If key is a slice #consider while loop to combat error on line 293 in gardenClass (i.get_name())
            # Slice meaning a crop object itself, so we only want to return specific crop objects
            for i in range(0, self.__maxSize):
                
                if (self.__hashTable[i] == None):
                    continue
                elif (self.__hashTable[i] == 'Tombstone'):
                    continue
                elif (self.__hashTable[i] == key):
                    return self.__hashTable[i]
            raise IndexError
        else:
            raise TypeError
    # end __getitem__()

    def __setitem__(self, crop): # Adds an item/crop to the table, likely to call the hash() function and/or the hash2()
        # Implemented by Sierra
        # iterate through hash() looking for an empty slot or Tombstone or a matching key; if none are returned then perform the same function through hash2()
        tableSpace = self.hash(crop.get_name())
        if (self.__hashTable[tableSpace] == None):
            self.__hashTable[tableSpace] = crop
            self.__size = self.__size + 1
            return True
        elif (self.__hashTable[tableSpace] == 'Tombstone'):
            self.__hashTable[tableSpace] = crop
            self.__size = self.__size + 1
            return True
        elif (self.__hashTable[tableSpace].get_name() == crop.get_name()):
            self.__hashTable[tableSpace] = crop
            self.__size = self.__size + 1
            return True
        else:
            tableSpace2 = self.hash2(crop.get_name(), tableSpace)
            if (tableSpace2 == None):
                return False
            else:
                self.__hashTable[tableSpace2] = crop
                self.__size = self.__size + 1
                return True
    # end __setitem__()
      
    def append(self, crop): # Adds a crop to the table, likely to call the hash() function, and/or the hash2()
        # Implemented by Anthony Castillo
        # From 15.9: recall that a successful search for the record during insertion should generate an error because two records with the same key are not allowed to be stored in the table
        tableSlot = self.hash(crop.get_name())
        if (self.__hashTable[tableSlot] == None): # If the index is empty
            self.__hashTable[tableSlot] = crop
            self.__size = self.__size + 1
            return True
        elif (self.__hashTable[tableSlot] == 'Tombstone'): # If the index is a tombstone
            self.__hashTable[tableSlot] = crop
            self.__size = self.__size + 1
            return True
        elif (self.__hashTable[tableSlot].get_name() == crop.get_name()): # If the index has a crop with a matching name then we'll be replacing the old entry with the new one
            self.__hashTable[tableSlot] = crop
            self.__size = self.__size + 1
            return True
        else:
            tableSlot2 = self.hash2(crop.get_name(), tableSlot)
            if (tableSlot2 == None):
                return False
            else: 
                self.__hashTable[tableSlot2] = crop
                self.__size = self.__size + 1
                return True
    # end append()

    def remove(self, key): # Removes the specified crop with the matching key from the table
        # Implemented by Anthony Castillo
        # Should replace the value with a 'Tombstone' of some description
        i, j = 0, 0 # 'I' keeps track of the max table size; while 'J' keeps track of the number of objects/crops in the table
        while (i < self.__maxSize and j < self.__size):
            if (self.__hashTable[i] == None):
                i = i + 1
            elif (self.__hashTable[i] == 'Tombstone'):
                i = i + 1
            elif (self.__hashTable[i].get_name().lower() == key.lower()):
                #del self.__hashTable[i]
                self.__hashTable[i] == 'Tombstone' # Deletes, but sets it to a tombstone
                self.__size = self.__size - 1
                return True
            elif (isinstance(self.__hashTable[i].get_name(), str)):
                j = j + 1 # One object/crop found
                i = i + 1
            else:
                i = i + 1
            #print('i: ', i, '\t', 'j: ', j) # Debugging
        return False
    # end remove()

    def clear(self): # Removes all elements from the table
        # Implemented by Sierra
        i = 0
        while (i < self.__maxSize):
            #print(i) # Debugging
            if (self.__hashTable[i]  == None):
              i = i + 1
              continue
            elif (self.__hashTable[i] == 'Tombstone'):
              self.__hashTable[i] = None
              i = i + 1
            elif (isinstance(self.__hashTable[i].get_name(),str)):
              self.__hashTable[i] = None
              i = i + 1 
              self.__size = self.__size - 1
            else:
              i = i + 1
        if (self.__size == 0):
            return True
        else:
            return False
    # end clear()

    def hash(self, key): # Returns the hashed value of the string key
        # Implemented by Anthony Castillo
        hashedString = 0
        for c in key.lower():
            hashedString = hashedString + ord(c)
        return hashedString % self.__maxSize
    # end hash()
        
    def hash2(self, key, hashedString): # Returns an unused hash index or the hash index of a matching key
        # Implemented by Anthony Castillo
        # Searches (Incrementally) thru the hashTable to find an empty slot for the hashedString
        # Causes clustering but uses all slots; we should use a different implementation
        '''
        for i in range(hashedString, self.__maxSize): # Depreciated, causes clustering, using the below section
            print(i)
            if (self.__hashTable[i] == None):
                print('Hash2() returning i=', i) # Temporary, for debugging purposes
                return i#hashedString+i#, True
            elif (self.__hashTable[i].get_name() == key): # The key is already inside of the table
                print('Hash2() returning i=', i) # Temporary, for debugging purposes
                return i#hashedString+i#, False
        for j in range(0, hashedString): # Depreciated, using the below section
            if (self.__hashTable[j] == None):
                print('Hash2() returning j=', j) # Temporary, for debugging purposes
                return j#, True
            elif (self.__hashTable[j].get_name() == key):
                print('Hash2() returning j=', j) # Temporary, for debugging purposes
                return j#, False
        '''
        for k in range(0, self.__maxSize):
            #print('k: ', (hashedString+(k*3))%self.__maxSize) # Debugging
            if (self.__hashTable[(hashedString + (k*3)) % self.__maxSize] == None): # Checks for an empty slot
                return ((hashedString + (k*3)) % self.__maxSize)
            elif (self.__hashTable[(hashedString + (k*3)) % self.__maxSize] == 'Tombstone'): # Checks for a tombstone
                return ((hashedString + (k*3)) % self.__maxSize)
            elif (self.__hashTable[(hashedString + (k*3)) % self.__maxSize].get_name().lower() == key.lower()): # Checks for a matching key
                return ((hashedString + (k*3)) % self.__maxSize)
            else: # Otherwise continue
                continue
        for l in range(hashedString, self.__maxSize): # If the above doesn't find an empty slot, this will. Otherwise, None will be returned. Can cause clustering
            #print('l: ', l) # Debugging
            if (self.__hashTable[l] == None):
                return l
            elif (self.__hashTable[l] == 'Tombstone'):
                return l
            elif (self.__hashTable[l].get_name().lower() == key.lower()):
                return l
        for m in range(0, hashedString): # Partner loop for the above loop
            #print('m: ', m) # Debugging
            if (self.__hashTable[m] == None):
                return m
            elif (self.__hashTable[m] == 'Tombstone'):
                return m
            elif (self.__hashTable[m].get_name().lower() == key.lower()):
                return m
        return None
    # end hash2()

    def setMaxSize(self, max): # Sets the max size of hashTable
        self.__maxSize = int(max)
        if (self.__maxSize == max): # Not necessary
            return True # But gives us some feedback
        else:
            return False
    # end setMaxSize()