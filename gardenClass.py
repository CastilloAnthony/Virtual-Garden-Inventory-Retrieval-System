'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  09/18/2022
  CS-3100
  Professor Hatem
'''
# commenting to join the GitHub
# This file will host all of our actual functions so that our main.py is not cluttered
import csv  # for csv file reading
from cropClass import Crop
from abstractClasses import GardenAbstract
from unsortedLinkedList_Implementation import UnsortedDictAbstract_Imp
from sortedArray_Implementation import SortedDictAbstract_Imp
from hashTable_Implementation import hashTable_Imp

class Garden(GardenAbstract):
    '''
    def __init__(self): # Depreciated
        # Implemented by Anthony Castillo
        # Modified by Sierra
        # Modified by Anthony Castillo
        
        # self.__gardenDatabase = [] # Old; Inital Array
        #self.__gardenDatabase = UnsortedDictAbstract_Imp() # Unsorted Linked List
        self.__gardenDatabase = SortedDictAbstract_Imp() # Sorted Array
        #self.__gardenDatabase = hashTable_Imp() # Hash Table
    # end __init__()
    '''
  
    def __init__(self, dataStructure = None, tableSize = None):
        # Implemented by Anthony Castillo
        # An alternative initialization method used to allow the user/program to choose which data structure to use, will default to the pythonic array.
        if (dataStructure == 0):
            self.__gardenDatabase = UnsortedDictAbstract_Imp()
            #print("Database set to UnsortedDictAbstract_Imp") # Debugging
        elif (dataStructure == 1):
            self.__gardenDatabase = SortedDictAbstract_Imp()
            #print("Database set to SortedDictAbstract_Imp") # Debugging
        elif (dataStructure == 2):
            self.__gardenDatabase = hashTable_Imp(tableSize)
            #print("Database set to hashTable_Imp") # Debugging
        else:
            self.__gardenDatabase = []
            #print("Database set to Pythonic Array") # Debugging
        self.__dataStructureType = self.setType()
    # end __init__()
      
    def __len__(self):
        # Returns the length of the current gardenDatabase list.
        # Implemented by Anthony Castillo
        return len(self.__gardenDatabase)
    # end len()

    def __str__(self):
        # Returns a long string of formatted data from the database.
        # Implemented by Anthony Castillo
        if (self.__dataStructureType == '3'): # If the database is using a pythonic array we'll use this method of displaying the list
            listInfo = ''  # Initializing an empty string
            i = 0
            while (i < len(self.__gardenDatabase)):
                #if (str(i) == 'None'): # Debugging
                    #print('A None was detected: ', i) # Debugging
                listInfo = listInfo + str(self.__gardenDatabase[i]
                ) + '\n'  # Adding the information from every crop into this string.
                i = i + 1      
            return listInfo  # Returning the long string of data.
        else:
            return str(self.__gardenDatabase) # This is a newer implementation that relies solely on the data structure to return all of the data contained within it
    # end __str__()

    def loadDatabase(self, location = ''):  # reload/load
        # Loads the database from the file
        # Implemented by Anthony Castillo
        if ('.csv' not in location):
            location = 'gardenDatabase.csv'
        linesWithFailures = []
        with open(location, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(
                csvreader
            )  # Skipping the first line since its just the labels # Throws an error if the file is empty
            lineNumber = 2  # Starting at line 2 since line 1 is the labels
            self.__gardenDatabase.clear()  # Clearing the current list
            for line in csvreader:
                if (line != ''):  # We don't want any lines that are empty
                    tempCrop = Crop(
                    )  # Crop class that will store all the new information from the line
                    successes = [
                    ]  # A list of true/false to check if all of the data gets imported correctly
                    successes.append(
                        tempCrop.set_soilWaterMoisture(line.pop())
                    )  # These set functions will return True on success, or False on failure
                    successes.append(tempCrop.set_nutritionalValue(line.pop()))
                    successes.append(tempCrop.set_diseases(line.pop()))
                    successes.append(tempCrop.set_averageYield(line.pop()))
                    successes.append(
                        tempCrop.set_averageGrowingTime(line.pop()))
                    successes.append(tempCrop.set_harvestSeason(line.pop()))
                    successes.append(tempCrop.set_growingSeason(line.pop()))
                    successes.append(tempCrop.set_cropType(line.pop()))
                    successes.append(tempCrop.set_name(line.pop()))
                    if (
                            False in successes
                    ):  # If any of them are False then we won't add the crop to the database list
                        linesWithFailures.append(
                            lineNumber
                        )  # Instead we will append the the line number of the line with discrepancies to this list of failed crops
                    else:  # Otherwise, we'll add it to the database list
                        self.__gardenDatabase.append(
                            tempCrop
                        )  # Appending this crop to the end of the gardenDatabase list
                lineNumber = lineNumber + 1
            csvfile.close(
            )  # Closing the file once we're done reading in the data.
        return linesWithFailures  # Return either an empty list or a list of numbers representeing the line number of the database with discrepancies
    # end loadDatabase()

    def saveToFile(self, location):
        # Attempts to save the current database list to the given filename
        # Initally Implemented by Anthony Castillo
        # Modified by Amanjoit Kaur
        if (len(self.__gardenDatabase) == 0):  # Empty list
            return False  # We don't want to save an empty list
        if ('.csv' not in location):
            location = 'gardenDatabase.csv'
        fieldNames = [
            'Crop Name', 'Type of Crop', 'Growing Season', 'Harvesting Season',
            'Avg. Growing Time', 'Avg. Yield', 'Diseases',
            'Nutritional Benefits', 'Water Soil Moisture'
        ]
        with open(location, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(
                fieldNames)  # Write the labels into the first row
            for i in self.__gardenDatabase:
                csvwriter.writerow(i.pullDataCSV())
            return True  # We have successfully saved to the file
        return False
    # end saveToFile()

    def insertNew(self, name, cropType, growingSeason, harvestSeason,
                  averageGrowingTime, averageYield, diseases, nutritionalValue,
                  soilWaterMoisture):
        # Takes in user parameters and attempts to add the new crop to the list.
        # Implemented by Amanjoit
        # Needs to return True/False for success/failure
        # Add these variables to the parameters list of this function. The interface will be handling the questions. This function should still verify that the new crop isn't missing data before adding it to the list.
        # All of the set_element() functions will now return True or False depending upon error checking success.
        # Verify that all elements have been added to the new crop correctly, then we'll add the new crop to the list
        newCrop = Crop(
        )  # make this newCrop = Crop() # since Crop() is the name of the actual crop class
        # debg, log successes
        # array.append(true/false)
        successes = []  # A simple list of true or falses values
        successes.append(newCrop.set_name(name))  # Setting name
        successes.append(newCrop.set_cropType(cropType))  # Setting cropType
        successes.append(
            newCrop.set_growingSeason(growingSeason))  # Setting growingSeason
        successes.append(
            newCrop.set_harvestSeason(harvestSeason))  # Setting harvestSeason
        successes.append(newCrop.set_averageGrowingTime(
            averageGrowingTime))  #Setting averageGrowingTime
        successes.append(
            newCrop.set_averageYield(averageYield))  # Setting averageYield
        successes.append(newCrop.set_diseases(diseases))  # Setting diseases
        successes.append(newCrop.set_nutritionalValue(
            nutritionalValue))  # Setting nutritional
        successes.append(newCrop.set_soilWaterMoisture(
            soilWaterMoisture))  # Setting soilWaterMoisture

        #print("Success array: ", successes) # Debugging
        if (False in successes
            ):  # This will be if one of the set functions returns false
            return False
        else:  # This will be if all of the set functions return true
            self.__gardenDatabase.append(
                newCrop
            )  # Officially appends the new crop to the back of our data structure
            return True  # This will also initiate an autosave
    # end insertNew()

    def modifyCrop(self, name, element, replacement):
        # Modifies an element (excluding the name) in our data structure then saves those changes to the file
        # The arguments will tell the function which crop and which element is going to be modified
        # Implememnted by Sierra
        # Modified by Anthony
        # call the crop index
        # search for the specific crop
        # input pre-entered info
        if ('cropType'
                in element):  # If the user wants to change the crop type
            for index in self.__gardenDatabase:  # Iterate thru the list and make comparisons to each
                if (
                        name.lower() in index.get_name().lower()
                ):  # Look for the name of the crop the user wants to change
                    index.set_cropType(replacement)  # Make the change
                    return True  # Return with True for success
        elif ('growingSeason' in element):
            for index in self.__gardenDatabase:
                if (name.lower() in index.get_name().lower()):
                    index.set_growingSeason(replacement)
                    return True
        elif ('harvestSeason' in element):
            for index in self.__gardenDatabase:
                if (name.lower() in index.get_name().lower()):
                    index.set_harvestSeason(replacement)
                    return True
        elif ('averageGrowingTime' in element):
            for index in self.__gardenDatabase:
                if (name.lower() in index.get_name().lower()):
                    index.set_averageGrowingTime(replacement)
                    return True
        elif ('averageYield' in element):
            for index in self.__gardenDatabase:
                if (name.lower() in index.get_name().lower()):
                    index.set_averageYield(replacement)
                    return True
        elif ('diseases' in element):
            for index in self.__gardenDatabase:
                if (name.lower() in index.get_name().lower()):
                    index.set_diseases(replacement)
                    return True
        elif ('nutritionalValue' in element):
            for index in self.__gardenDatabase:
                if (name.lower() in index.get_name().lower()):
                    index.set_nutritionialValue(replacement)
                    return True
        elif ('soilWaterMoisture' in element):
            for index in self.__gardenDatabase:
                if (name.lower() in index.get_name().lower()):
                    index.set_soilWaterMoisture(replacement)
                    return True
        else:
            return False  # The user input the wrong type of element
    # end modifyCrop()

    def removeCrop(self, name):
        # Removes the specified crop from our data structure
        # Implemented by Sierra
        # Needs tor return True/False for success/failure
        # Minor modification by Anthony Castillo
        if (self.__dataStructureType == '3'): # Checks the data structure type
            for index in self.__gardenDatabase:  # Iterates thru the database
                #print(index) # Debugging
                if (
                        name.lower() in index.get_name().lower()
                ):  # Compares the user's name input to the name of the current crop
                    self.__gardenDatabase.remove(
                        index)  # Removes that crop if it matches
                    return True  # Returns true upon successful removal
            return False
        else:
            if (self.__gardenDatabase.remove(name)): # For custom Data Strucutres using built-in remove functions
                return True
            else:
                return False
    # end removeCrop()

    def searchForCrop(self, name):
        # Function that searches our data structure for the specified crop and then returns that crop's information
        # Implemented by Sierra
        # Modified by Anthony Castillo
        if (self.__dataStructureType == '1' or self.__dataStructureType == '2'):
            return self.__gardenDatabase[name]
        else:
            for crop in self.__gardenDatabase:
                if (name.lower() in crop.get_name().lower()):
                    #self.showCrop(crop)  #return crop if found in database
                    #replace with self.gardenDatabase[crop].showCrop
                    return str(
                        crop
                    )  # check the cropClass.py file (line 32) to understand this function "__str__()"
    # end searchForCrop()

    def searchByElements(self, element, information):
        # Implemented by Anthony Castillo
        # Function that searches our data structure for all crops that contain the requested information in the specified element
        # (i.e. element = 'growingSeason', information = 'August')
        # This funciton should return the crop information of each crop that matches the requested information that it finds.
        # These four dictionaries are used to search for growing season and harvest season
        spring = {'spring', 'march', 'april', 'may'}
        summer = {'summer', 'june', 'july', 'august'}
        fall = {'fall', 'september', 'october', 'november',
                'autumn'}  # autumn is an alias for fall
        winter = {'winter', 'december', 'january', 'february'}
        yearly = {'year', 'yearly', 'annual',
                  'annually'}  # For year round crops
        totalFinds = 0
        matches = []  # A list of strings, nothing more
        if (
                'name' in element
        ):  # Using predefined identifiers for figuring out which element the user wants to search thru
            for i in self.__gardenDatabase:  # Iterating thru the garden list
                if (
                        information.lower() in i.get_name().lower()
                ):  # Comparing the information with the garden's list of information
                    matches.append(str(i))
                    totalFinds = totalFinds + 1  # Incrementing the total find count up by one
        elif ('cropType' in element):
            for i in self.__gardenDatabase:
                if (information.lower() in i.get_cropType().lower()):
                    matches.append(str(i))
                    totalFinds = totalFinds + 1
        elif ('growingSeason' in element
              ):  # We'll use predefined dictionaries to search between seasons
            for i in self.__gardenDatabase:
                if (information.lower()
                        in spring):  # If the user requests a month in spring
                    for k in spring:
                        if (k in i.get_growingSeason().lower()
                            ):  # If one month of the season matches
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
                elif (information.lower() in summer):  # Summer Crops
                    for k in summer:
                        if (k in i.get_growingSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
                elif (information.lower() in fall):  # Fall Crops
                    for k in fall:
                        if (k in i.get_growingSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
                elif (information.lower() in winter):  # Winter Crops
                    for k in winter:
                        if (k in i.get_growingSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
                elif (information.lower() in yearly):  # For year round crops
                    for k in yearly:
                        if (k in i.get_growingSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
        elif ('harvestSeason' in element):  # Same as growing Season
            for i in self.__gardenDatabase:
                if (information.lower() in spring):  # Spring Crops
                    for k in spring:
                        if (k in i.get_harvestSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
                elif (information.lower() in summer):  # Summer Crops
                    for k in summer:
                        if (k in i.get_harvestSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
                elif (information.lower() in fall):  # Fall Crops
                    for k in fall:
                        if (k in i.get_harvestSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
                elif (information.lower() in winter):  # Winter Crops
                    for k in winter:
                        if (k in i.get_harvestSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
                elif (information.lower() in yearly):  # For year round crops
                    for k in yearly:
                        if (k in i.get_harvestSeason().lower()):
                            matches.append(str(i))
                            totalFinds = totalFinds + 1
                            break
        elif ('growingTime' in element):
            for i in self.__gardenDatabase:
                if (information.lower() in i.get_averageGrowingTime().lower()):
                    matches.append(str(i))
                    totalFinds = totalFinds + 1
        elif ('yield' in element):
            for i in self.__gardenDatabase:
                if (information.lower() in i.get_averageYield().lower()):
                    matches.append(str(i))
                    totalFinds = totalFinds + 1
        elif ('disease' in element):
            for i in self.__gardenDatabase:
                if (information.lower() in i.get_diseases().lower()):
                    matches.append(str(i))
                    totalFinds = totalFinds + 1
        elif ('nutritional' in element):
            for i in self.__gardenDatabase:
                if (information.lower() in i.get_nutritionalValue().lower()):
                    matches.append(str(i))
                    totalFinds = totalFinds + 1
        elif ('water' in element or 'moisture' in element):
            for i in self.__gardenDatabase:
                if (information.lower() in i.get_soilWaterMoisture().lower()):
                    matches.append(str(i))
                    totalFinds = totalFinds + 1
        else:
            return matches, -1  # An invalid element type was entered, returns an empty list and an error code
        return matches, totalFinds  # Returns the matches and the number of matches

    # end searchByElements()
    '''
    def sortList(self): # Returns true/false on success/failure
        # Implemented by Anthony Castillo
        # Calls the sort function
        #if (isinstance(self.__gardenDatabase, SortedDictAbstract_Imp)): # It only attempts to sort if the list is in the right format
        if (self.__dataStructureType == '1'): # If is a Sorted Array
            self.__gardenDatabase.selfSort()
            return True
        #elif (Other data structure with sorting algorithim):
        else:
            return False
    '''

    def setType(self): # Returns an integer representing the type of data structure being used.
        # Implemented by Anthony Castillo
        if (isinstance(self.__gardenDatabase, UnsortedDictAbstract_Imp)):
            return '0'
        elif (isinstance(self.__gardenDatabase, SortedDictAbstract_Imp)):
            return '1'
        elif (isinstance(self.__gardenDatabase, hashTable_Imp)):
            return '2'
        else: # Pythonic Array
            return '3'
    # end setType()
          
    def getDataStructureType(self): # Returns the integer representing the type of data structure being used.
        # Implemented by Anthony Castillo
        return self.__dataStructureType
    # end getDataStructureType()
