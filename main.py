'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  09/06/2022
  CS-3100
  Professor Hatem
'''

from interfaceClass import Interface
from unsortedLinkedList_Implementation import UnsortedDictAbstract_Imp
from sortedArray_Implementation import SortedDictAbstract_Imp
from hashTable_Implementation import hashTable_Imp
from cropClass import Crop
from gardenClass import Garden  # Temporary
import os  # Solely used for clearing the screen


def main():
    newInterface = Interface()
    newInterface.virtualGardenInterface()
# end main()


def clearScreen():
    input('Press any key to continue...')
    if (os.name == 'nt'):  # Clearing the screen
        os.system('cls')  # For windows
    else:
        os.system('clear')  # For Linux


# end clearScreen()


def testingGardenDicts():
    print('Testing all Garden dictionaries...')
    newGarden0 = Garden(0)  # Unsorted Linked List
    newGarden1 = Garden(1)  # Sorted Linked List
    newGarden2 = Garden(2, 1000)  # Hash Table with a size of 1000
    newGarden3 = Garden(3)  # Pythonic Array
    newGarden0.loadDatabase()  # Default csv will be loaded
    newGarden1.loadDatabase()  # Default csv will be loaded
    newGarden2.loadDatabase()  # Default csv will be loaded
    newGarden3.loadDatabase()  # Default csv will be loaded

    testCrop1 = Crop()

    testCrop1.set_name(
        'Blueberry1'
    )  # Cannot accept a digit in its name... This might need to be changed.
    testCrop1.set_cropType('Fruit')
    testCrop1.set_growingSeason('Summer')
    testCrop1.set_harvestSeason('Winter')
    testCrop1.set_averageGrowingTime('180 days')
    testCrop1.set_averageYield('10 quarts')
    testCrop1.set_diseases('Fruit rot')
    testCrop1.set_soilWaterMoisture('2 in')
    testCrop1.set_nutritionalValue('Vitamin C')

    print('***********************************************')
    print('Unsorted Linked List - Length:', len(newGarden0))
    print('***********************************************')
    print(
        'Insert new function: ',
        newGarden0.insertNew(testCrop1.get_name(), testCrop1.get_cropType(),
                             testCrop1.get_growingSeason(),
                             testCrop1.get_harvestSeason(),
                             testCrop1.get_averageGrowingTime(),
                             testCrop1.get_averageYield(),
                             testCrop1.get_diseases(),
                             testCrop1.get_nutritionalValue(),
                             testCrop1.get_soilWaterMoisture()))
    print('Search by name function: ')
    print(newGarden0.searchForCrop(testCrop1.get_name()))
    print('Search by elements function: ')
    matches, finds = newGarden0.searchByElements('harvestSeason', 'winter')
    for i in matches:
        print(i)
    print('Modify crop function: ',
          newGarden0.modifyCrop('Blueberry', 'cropType', 'Vegetable'))
    print('Remove crop Function: ',
          newGarden0.removeCrop(testCrop1.get_name()), '\n')
    print('Print function: ')
    print(str(newGarden0), '\nUnsorted Linked List Test Complete')
    input('Press any key to continue...')

    print('***********************************************')
    print('Sorted Linked List - Length:', len(newGarden1))
    print('***********************************************')
    print(
        'Insert new function: ',
        newGarden1.insertNew(testCrop1.get_name(), testCrop1.get_cropType(),
                             testCrop1.get_growingSeason(),
                             testCrop1.get_harvestSeason(),
                             testCrop1.get_averageGrowingTime(),
                             testCrop1.get_averageYield(),
                             testCrop1.get_diseases(),
                             testCrop1.get_nutritionalValue(),
                             testCrop1.get_soilWaterMoisture()))
    print('Search by name function: ')
    print(newGarden1.searchForCrop(testCrop1.get_name()))
    print('Search by elements function: ')
    matches, finds = newGarden1.searchByElements('harvestSeason', 'winter')
    for i in matches:
        print(i)
    print('Modify crop function: ',
          newGarden1.modifyCrop('Blueberry', 'cropType', 'Vegetable'))
    print('Remove crop Function: ',
          newGarden1.removeCrop(testCrop1.get_name()), '\n')
    newGarden1.sortList()
    print('Print function: ')
    print(str(newGarden1), '\nSorted Array Test Complete')
    input('Press any key to continue...')

    print('***********************************************')
    print('Hash Table - Length:', len(newGarden2))
    print('***********************************************')
    print(
        'Insert new function: ',
        newGarden2.insertNew(testCrop1.get_name(), testCrop1.get_cropType(),
                             testCrop1.get_growingSeason(),
                             testCrop1.get_harvestSeason(),
                             testCrop1.get_averageGrowingTime(),
                             testCrop1.get_averageYield(),
                             testCrop1.get_diseases(),
                             testCrop1.get_nutritionalValue(),
                             testCrop1.get_soilWaterMoisture()))
    print('Search by name function: ')
    print(newGarden2.searchForCrop(testCrop1.get_name()))
    print('Search by elements function: ')
    matches, finds = newGarden2.searchByElements('harvestSeason', 'winter')
    for i in matches:
        print(i)
    print('Modify crop function: ',
          newGarden2.modifyCrop('Blueberry', 'cropType', 'Vegetable'))
    print('Remove crop Function: ',
          newGarden2.removeCrop(testCrop1.get_name()), '\n')
    print('Print function: ')
    print(str(newGarden2), '\nHash Table Test Complete')
    input('Press any key to continue...')

    print('***********************************************')
    print('Pythonic Array - Length:', len(newGarden3))
    print('***********************************************')
    print(
        'Insert new function: ',
        newGarden3.insertNew(testCrop1.get_name(), testCrop1.get_cropType(),
                             testCrop1.get_growingSeason(),
                             testCrop1.get_harvestSeason(),
                             testCrop1.get_averageGrowingTime(),
                             testCrop1.get_averageYield(),
                             testCrop1.get_diseases(),
                             testCrop1.get_nutritionalValue(),
                             testCrop1.get_soilWaterMoisture()))
    print('Search by name function: ')
    print(newGarden3.searchForCrop(testCrop1.get_name()))
    print('Search by elements function: ')
    matches, finds = newGarden3.searchByElements('harvestSeason', 'winter')
    for i in matches:
        print(i)
    print('Modify crop function: ',
          newGarden3.modifyCrop('Blueberry', 'cropType', 'Vegetable'))
    print('Remove crop Function: ',
          newGarden3.removeCrop(testCrop1.get_name()), '\n')
    print('Print function: ')
    print(str(newGarden3), '\nPythonic Array Test Complete')

    print('\nAll Garden Dictionary tests are complete!')


# end testingGardenDicts()


def testingHashTable():  # Depreciated
    testCrop1 = Crop()
    testCrop2 = Crop()
    testCrop3 = Crop()
    testCrop4 = Crop()

    testCrop1.set_name('Oranges')
    testCrop1.set_cropType('Fruit')
    testCrop1.set_growingSeason('Summer')
    testCrop1.set_harvestSeason('Winter')
    testCrop1.set_averageGrowingTime('180 days')
    testCrop1.set_averageYield('10 oranges')
    testCrop1.set_diseases('Fruit rot')
    testCrop1.set_soilWaterMoisture('2 in')
    testCrop1.set_nutritionalValue('Vitamin C')

    testCrop2.set_name('Apples')
    testCrop2.set_cropType('Fruit')
    testCrop2.set_growingSeason('Summer')
    testCrop2.set_harvestSeason('Winter')
    testCrop2.set_averageGrowingTime('180 days')
    testCrop2.set_averageYield('10 apples')
    testCrop2.set_diseases('Fruit rot')
    testCrop2.set_soilWaterMoisture('2 in')
    testCrop2.set_nutritionalValue('Vitamin C')

    testCrop3.set_name('Pears')
    testCrop3.set_cropType('Fruit')
    testCrop3.set_growingSeason('Summer')
    testCrop3.set_harvestSeason('Winter')
    testCrop3.set_averageGrowingTime('180 days')
    testCrop3.set_averageYield('10 pears')
    testCrop3.set_diseases('Fruit rot')
    testCrop3.set_soilWaterMoisture('2 in')
    testCrop3.set_nutritionalValue('Vitamin C')

    testCrop4.set_name('Dragonfruit')
    testCrop4.set_cropType('Fruit')
    testCrop4.set_growingSeason('Summer')
    testCrop4.set_harvestSeason('Winter')
    testCrop4.set_averageGrowingTime('180 days')
    testCrop4.set_averageYield('10 lbs')
    testCrop4.set_diseases('Fruit rot')
    testCrop4.set_soilWaterMoisture('2 in')
    testCrop4.set_nutritionalValue('Vitamin C')

    newHashTable = hashTable_Imp()
    newHashTable.append(testCrop1)
    newHashTable.append(testCrop2)
    newHashTable.append(testCrop3)
    newHashTable.append(testCrop4)

    print('***********************************************')
    print('Testing Hash Table')
    print('***********************************************')
    print('Length of Hash Table: ', len(newHashTable), '\n')
    print(str(newHashTable))

    newHashTable.remove('Oranges')
    newHashTable.clear()

    testArray = []
    testString1 = 'Blueberry'
    testString2 = 'Pineapple'
    testString3 = 'Strawberry'
    testString4 = 'Corn'
    testArray.append(testString1)
    testArray.append(testString2)
    testArray.append(testString3)
    testArray.append(testString4)

    for i in testArray:
        if i in newHashTable:
            print(i, ' is in the hash table.')
        else:
            print(i, ' is not in the hash table.')
        stringCode = 0
        for c in i:
            stringCode = stringCode + ord(c)
        print('The sum of the unicode of the string ', i, ' is ', stringCode)


# end testingHashTable()


def testingSortingArray():  # For testing purposes # Depreciated
    testCrop1 = Crop()
    testCrop2 = Crop()
    testCrop3 = Crop()
    testCrop4 = Crop()
    testCrop5 = Crop()
    testCrop6 = Crop()
    testCrop7 = Crop()
    testCrop8 = Crop()
    testCrop9 = Crop()
    testCrop10 = Crop()
    testCrop11 = Crop()
    testCrop12 = Crop()
    testCrop13 = Crop()

    testCrop1.set_name('Oranges')
    testCrop1.set_cropType('Fruit')
    testCrop1.set_growingSeason('Summer')
    testCrop1.set_harvestSeason('Winter')
    testCrop1.set_averageGrowingTime('180 days')
    testCrop1.set_averageYield('10 oranges')
    testCrop1.set_diseases('Fruit rot')
    testCrop1.set_soilWaterMoisture('2 in')
    testCrop1.set_nutritionalValue('Vitamin C')

    testCrop2.set_name('Apples')
    testCrop2.set_cropType('Fruit')
    testCrop2.set_growingSeason('Summer')
    testCrop2.set_harvestSeason('Winter')
    testCrop2.set_averageGrowingTime('180 days')
    testCrop2.set_averageYield('10 apples')
    testCrop2.set_diseases('Fruit rot')
    testCrop2.set_soilWaterMoisture('2 in')
    testCrop2.set_nutritionalValue('Vitamin C')

    testCrop3.set_name('Pears')
    testCrop3.set_cropType('Fruit')
    testCrop3.set_growingSeason('Summer')
    testCrop3.set_harvestSeason('Winter')
    testCrop3.set_averageGrowingTime('180 days')
    testCrop3.set_averageYield('10 pears')
    testCrop3.set_diseases('Fruit rot')
    testCrop3.set_soilWaterMoisture('2 in')
    testCrop3.set_nutritionalValue('Vitamin C')

    testCrop4.set_name('Dragonfruit')
    testCrop4.set_cropType('Fruit')
    testCrop4.set_growingSeason('Summer')
    testCrop4.set_harvestSeason('Winter')
    testCrop4.set_averageGrowingTime('180 days')
    testCrop4.set_averageYield('10 lbs')
    testCrop4.set_diseases('Fruit rot')
    testCrop4.set_soilWaterMoisture('2 in')
    testCrop4.set_nutritionalValue('Vitamin C')

    testCrop5.set_name('Blueberry')
    testCrop5.set_cropType('Fruit')
    testCrop5.set_growingSeason('Summer')
    testCrop5.set_harvestSeason('Winter')
    testCrop5.set_averageGrowingTime('180 days')
    testCrop5.set_averageYield('10 lbs')
    testCrop5.set_diseases('Fruit rot')
    testCrop5.set_soilWaterMoisture('2 in')
    testCrop5.set_nutritionalValue('Vitamin C')

    testCrop6.set_name('Grapes')
    testCrop6.set_cropType('Fruit')
    testCrop6.set_growingSeason('Summer')
    testCrop6.set_harvestSeason('Winter')
    testCrop6.set_averageGrowingTime('180 days')
    testCrop6.set_averageYield('10 grapes')
    testCrop6.set_diseases('Fruit rot')
    testCrop6.set_soilWaterMoisture('2 in')
    testCrop6.set_nutritionalValue('Vitamin C')

    testCrop7.set_name('Strawberry')
    testCrop7.set_cropType('Fruit')
    testCrop7.set_growingSeason('Summer')
    testCrop7.set_harvestSeason('Winter')
    testCrop7.set_averageGrowingTime('180 days')
    testCrop7.set_averageYield('10 lbs')
    testCrop7.set_diseases('Fruit rot')
    testCrop7.set_soilWaterMoisture('2 in')
    testCrop7.set_nutritionalValue('Vitamin C')

    testCrop8.set_name('Blackberry')
    testCrop8.set_cropType('Fruit')
    testCrop8.set_growingSeason('Summer')
    testCrop8.set_harvestSeason('Winter')
    testCrop8.set_averageGrowingTime('180 days')
    testCrop8.set_averageYield('10 lbs')
    testCrop8.set_diseases('Fruit rot')
    testCrop8.set_soilWaterMoisture('2 in')
    testCrop8.set_nutritionalValue('Vitamin C')

    testCrop9.set_name('Lemon')
    testCrop9.set_cropType('Fruit')
    testCrop9.set_growingSeason('Summer')
    testCrop9.set_harvestSeason('Winter')
    testCrop9.set_averageGrowingTime('180 days')
    testCrop9.set_averageYield('10 lemons')
    testCrop9.set_diseases('Fruit rot')
    testCrop9.set_soilWaterMoisture('2 in')
    testCrop9.set_nutritionalValue('Vitamin C')

    testCrop10.set_name('Peach')
    testCrop10.set_cropType('Fruit')
    testCrop10.set_growingSeason('Summer')
    testCrop10.set_harvestSeason('Winter')
    testCrop10.set_averageGrowingTime('180 days')
    testCrop10.set_averageYield('10 peaches')
    testCrop10.set_diseases('Fruit rot')
    testCrop10.set_soilWaterMoisture('2 in')
    testCrop10.set_nutritionalValue('Vitamin C')

    testCrop11.set_name('Raspberry')
    testCrop11.set_cropType('Fruit')
    testCrop11.set_growingSeason('Summer')
    testCrop11.set_harvestSeason('Winter')
    testCrop11.set_averageGrowingTime('180 days')
    testCrop11.set_averageYield('10 lbs')
    testCrop11.set_diseases('Fruit rot')
    testCrop11.set_soilWaterMoisture('2 in')
    testCrop11.set_nutritionalValue('Vitamin C')

    testCrop12.set_name('Grapefruit')
    testCrop12.set_cropType('Fruit')
    testCrop12.set_growingSeason('Summer')
    testCrop12.set_harvestSeason('Winter')
    testCrop12.set_averageGrowingTime('180 days')
    testCrop12.set_averageYield('10 grapefruits')
    testCrop12.set_diseases('Fruit rot')
    testCrop12.set_soilWaterMoisture('2 in')
    testCrop12.set_nutritionalValue('Vitamin C')

    testCrop13.set_name('Durian')
    testCrop13.set_cropType('Fruit')
    testCrop13.set_growingSeason('Summer')
    testCrop13.set_harvestSeason('Winter')
    testCrop13.set_averageGrowingTime('180 days')
    testCrop13.set_averageYield('10 lbs')
    testCrop13.set_diseases('Fruit rot')
    testCrop13.set_soilWaterMoisture('2 in')
    testCrop13.set_nutritionalValue('Vitamin C')

    newArray = SortedDictAbstract_Imp()
    newArray.append(testCrop1)
    newArray.append(testCrop2)
    newArray.append(testCrop3)
    newArray.append(testCrop4)
    newArray.append(testCrop5)
    newArray.append(testCrop6)
    newArray.append(testCrop7)
    newArray.append(testCrop8)
    newArray.append(testCrop9)
    newArray.append(testCrop10)
    newArray.append(testCrop11)
    newArray.append(testCrop12)
    newArray.append(testCrop13)

    print('***********************************************')
    print('Testing Sorted Array')
    print('***********************************************')
    print('Length of Array: ', len(newArray), '\n')
    print('Before Sorting: \n')
    print(str(newArray))
    newArray.selfSort()
    print('-----------------------------------------------')
    print('After Sorting: \n')
    print(str(newArray))

    newArray.remove('Orange')
    newArray.clear()

    testArray = []
    testString1 = 'Blueberry'
    testString2 = 'Pineapple'
    testString3 = 'Strawberry'
    testString4 = 'Corn'
    testArray.append(testString1)
    testArray.append(testString2)
    testArray.append(testString3)
    testArray.append(testString4)

    for i in testArray:
        if (i in newArray):
            print(i, ' is in the sorted array.')
        else:
            print(i, ' was not found in the sorted array.')
        stringCode = 0
        for c in i:
            stringCode = stringCode + ord(c)
        print('The sum of the unicode of the string ', i, ' is ', stringCode)
    '''
    newArray2 = []
    newArray2.append('alpha')
    newArray2.append('beta')
    newArray2.append('charlie')
    newArray2.append('delta')
    print('Initial Array')
    for i in newArray2:
        print(i)
    
    del newArray2[2]
    newArray2.insert(2, 'echo')
    print('Modified Array')
    for i in newArray2:
        print(i)
    
    greatestString = ''
    leastString = ''
    i = 0
    while i < len(newArray2):
        if (i == 0):
            greatestString = newArray2[i]
            leastString = newArray2[i]
        if (greatestString < newArray2[i]):
            greatestString = newArray2[i]
        if (leastString > newArray2[i]):
            leastString = newArray2[i]
        i = i + 1
    print('The length of the array is: ', len(newArray2), 'The greatest string is: ', str(greatestString), ' The least string is: ', str(leastString))
    '''


# end of testingSortingArray()


def testingUnsortedLinkedList():  # For testing purposes # Depreciated
    testCrop1 = Crop()
    testCrop2 = Crop()
    testCrop3 = Crop()
    testCrop4 = Crop()

    testCrop1.set_name('Oranges')
    testCrop1.set_cropType('Fruit')
    testCrop1.set_growingSeason('Summer')
    testCrop1.set_harvestSeason('Winter')
    testCrop1.set_averageGrowingTime('180 days')
    testCrop1.set_averageYield('10 oranges')
    testCrop1.set_diseases('Fruit rot')
    testCrop1.set_soilWaterMoisture('2 in')
    testCrop1.set_nutritionalValue('Vitamin C')

    testCrop2.set_name('Apples')
    testCrop2.set_cropType('Fruit')
    testCrop2.set_growingSeason('Summer')
    testCrop2.set_harvestSeason('Winter')
    testCrop2.set_averageGrowingTime('180 days')
    testCrop2.set_averageYield('10 apples')
    testCrop2.set_diseases('Fruit rot')
    testCrop2.set_soilWaterMoisture('2 in')
    testCrop2.set_nutritionalValue('Vitamin C')

    testCrop3.set_name('Pears')
    testCrop3.set_cropType('Fruit')
    testCrop3.set_growingSeason('Summer')
    testCrop3.set_harvestSeason('Winter')
    testCrop3.set_averageGrowingTime('180 days')
    testCrop3.set_averageYield('10 pears')
    testCrop3.set_diseases('Fruit rot')
    testCrop3.set_soilWaterMoisture('2 in')
    testCrop3.set_nutritionalValue('Vitamin C')

    testCrop4.set_name('Dragonfruit')
    testCrop4.set_cropType('Fruit')
    testCrop4.set_growingSeason('Summer')
    testCrop4.set_harvestSeason('Winter')
    testCrop4.set_averageGrowingTime('180 days')
    testCrop4.set_averageYield('10 lbs')
    testCrop4.set_diseases('Fruit rot')
    testCrop4.set_soilWaterMoisture('2 in')
    testCrop4.set_nutritionalValue('Vitamin C')

    newArray = UnsortedDictAbstract_Imp()
    newArray.append(testCrop1)
    newArray.append(testCrop2)
    newArray.append(testCrop3)
    newArray.append(testCrop4)

    print('***********************************************')
    print('Testing Unsorted Linked List')
    print('***********************************************')
    print('Length of Unsorted Linked List: ', len(newArray), '\n')
    print(str(newArray))

    newArray.remove('Orange')
    newArray.clear()

    testArray = []
    testString1 = 'Blueberry'
    testString2 = 'Pineapple'
    testString3 = 'Strawberry'
    testString4 = 'Corn'
    testArray.append(testString1)
    testArray.append(testString2)
    testArray.append(testString3)
    testArray.append(testString4)

    for i in testArray:
        if i in newArray:
            print(i, ' is in the unsorted linked list.')
        else:
            print(i, ' is not in the unsorted linked list.')
        stringCode = 0
        for c in i:
            stringCode = stringCode + ord(c)
        print('The sum of the unicode of the string ', i, ' is ', stringCode)


# testingUnsortedLinkedList()

# Comment out the testing functions before fully submitting
'''
testingUnsortedLinkedList()
testingHashTable()
testingSortingArray()
clearScreen()
'''
#testingGardenDicts()
#clearScreen()

main()
#testingGardenDicts()
