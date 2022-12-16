'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  09/26/2022
  CS-3100
  Professor Hatem
'''
# This will be the base class for our user(s) to interface with our garden object
from gardenClass import Garden

class Interface:
    @staticmethod
    def printMainMenu():
        print(
            '\n',
            '***************************************************',
            '\n',
            'Virtual Garden Inventory System Main Menu',
            '\n',
            '***************************************************',
            '\n',
            '[0] Exit Program',
            '\n',
            '[1] Help',
            '\n',
            '[2] Load Database',
            '\n',
            '[3] Save Database to file',
            '\n',
            '[4] Show List',
            '\n',
            '[5] Insert New Crop',
            '\n',
            '[6] Remove Crop',
            '\n',
            '[7] Modify Crop Information',
            '\n',
            '[8] Search for Crop',
            '\n',
            '[9] Search for Crops by Information',
            '\n',
        )
    # end printMainMenu()
          
    @staticmethod
    def virtualGardenInterface():
        # The Main Interface function for interacting with the Garden class
        # Implemented by Anthony Castillo
        # Modified Amanjoit Added \n and examples for input for the user 
        #garden = Garden()

        print('\n',
            '***************************************************',
            '\n',
            'Welcome to the Virtual Garden Inventory System',
            '\n',
            '***************************************************',
            '\n',
            'Which Data Structure would you like to use?',
              '\n',
              '[0] Unsorted Linked List',
              '\n',
              '[1] Sorted Array',
              '\n',
              '[2] Hash Table',
              '\n',
              '[3] Pythonic Array (Default)',
              '\n'
             ) # Choosing the data strcuture
        userPrecheck = input('Option: ')
        userInput, size = '', 100
        if (userPrecheck.isdigit()):  # Checks the user's input for a digit only string
            userInput = int(userPrecheck)  # Converts that input to an integer
            if (userInput == 2):
                userPrecheck2 = input('How large would you like the table to be? (default: 100) ')
                if (userPrecheck2.isdigit()):
                    size = int(userPrecheck2)
                else:
                    print('Invalid value entered, defaulting to 100')
        else:
            print('Invalid option selected, defaulting to the Pythonic Array')  # The user did not input a digit
            userInput = ''
        garden = Garden(userInput, size) # Initializing the Garden Database
        gardenType = garden.getDataStructureType()
        if (gardenType == '0'):
            print('Initialized Garden as an Unsorted Linked List.')
        elif (gardenType == '1'):
            print('Initialized Garden as a Sorted Array')
        elif (gardenType == '2'):
            print('Initialized Garden as a Hash Table')
        else:
            print('Initialized Garden as a Pytonic Array')
        option = 1
        autosave = False  # This tells the autosave feature when it is enabled or not
        location = ''  # This holds the location for the current .csv file. Needed by the autosave feature
        yes = {
            'yes', 'y', 'true', 'ya', 'yeah', 'yah', 'enable', 'affirmative'
        }  # A collection of aliases for yes.
        while (option != 0):
            Interface.printMainMenu()
            successfulOperation = False  # Insert New, Modify Crop, Remove Crop will set this to true; This will tell the autosave feature when it needs to perform a save; This needs to go back to false at the start of every loop.
            if (len(garden) == 0):
                print('The database is currently empty. \n')
            userPrecheck = input('Option: ')
            if (userPrecheck.isdigit()
                ):  # Checks the user's input for a digit only string
                userInput = int(
                    userPrecheck)  # Converts that input to an integer
            else:
                print('Invalid option selected.'
                      )  # The user did not input a digit
                continue
            if (userInput == 0):  # Quit Program
                print("Exiting Program.")
                option = 0  # Disables the while loop
                quit()  # Exits the program
            elif (userInput == 1):  # Helper Function
                Interface.programInformation()
            elif (
                    userInput == 2
            ):  # Load a Database from Filename; Also can enable the autosave feature
                location = input(
                    'What is the file name of the file you would like to load? (default: gardenDatabase.csv) '
                )
                if ('.csv' in location
                    ):  # If a .csv file is choosen then we'll load that.
                    print('Attempting to load the data in the file ', location)
                else:
                    location = 'gardenDatabase.csv'
                answer = input(
                    'Would you like to enable autosave? (default: Disabled) '
                )  # If the user wants to enable autosave they must answer some form of yes
                if (answer.lower() in yes):
                    autosave = True  # This must be true for the autosave to be used.
                    print(
                        'Autosave has been Enabled for the file: ', location,
                        '\nNote: You can change the target save location by running option 2 again and changing the target loading file, or by running option 3 and changing the target save file.',
                        '\n')
                else:
                    autosave = False
                    print('Warning: autosave is not enabled!',
                          '\nMake sure to save your work with option 3.', '\n')
                print('Attempting to load the data from the file', location)
                failures = garden.loadDatabase(
                    location
                )  # Will returns a list of numbers representing the lines for which importing failed.
                if (len(failures) == 1):  # A singular failure
                    print(
                        'Successfully loaded ', len(garden),
                        ' crops into the garden with 1 import failure on line:',
                        str(failures.pop()), 'of the file', location)
                elif (len(failures) != 0):  # Multiple failures
                    failuresString = ''  # An empty string
                    for i in failures:
                        if (i != failures[-1]):  # If i is not the last element
                            failuresString = failuresString + str(
                                i) + ','  # Add a comma to the end
                        else:
                            failuresString = failuresString + str(
                                i
                            )  # If it is the last element, then we won't add a comma
                    print('Successfully loaded ',
                          len(garden), ' crops into the garden with ',
                          len(failures), ' import failures on lines:',
                          failuresString, 'of the file', location)
                else:  # No failures
                    print('Successfully loaded ', len(garden),
                          ' crops into the garden.', '\n')
                ''' # Depreicated
                if (gardenType == '1' and len(garden) > 0): # If the database is a sorted array
                    print('Attempting to sort the imported list...')
                    if (garden.sortList()): # Calls the sort function 
                        print('The list has been sorted successuflly.')
                    else:
                        print('The list could not be sorted.')
                '''
            elif (userInput == 3):  # Save to file
                if (len(garden) == 0):
                    print(
                        'The garden list is empty. There is nothing to save.')
                else:
                    location = input(
                        'Where do you want to save the file to? (default: gardenDatabase.csv) '
                    )
                    if ('.csv' in location
                        ):  # If a .csv file is choosen then we'll load that.
                        print('Attempting to load the data in the file ',
                              location)
                    elif (location == ''):
                        location = 'gardenDatabase.csv'
                    else:  # Otherwise we'll load the default file.
                        print('Invalid input, using the default file location.')
                        location = 'gardenDatabase.csv'
                    #success = garden.saveToFile(location)
                    if (
                            garden.saveToFile(location)
                    ):  # Will return true upon success, or false upon failure
                        print('Successfuly saved to ', location)
                    else:
                        print('Could not save to ', location)
            elif (userInput == 4):  # Show List
                print(str(garden))
                print('There are ', len(garden), ' crops in this garden.')
            elif (userInput == 5):  # Insert New Crop
            # Modify - Amanjoit, Added \n and examples for input for the user 
                name = input('What do you want to name the crop? ')
                cropType = input(
                    'What type of crop is this? E.g., plant, bush, tree, fruit, vegetable, nut, squash\n'
                )
                growingSeason = input(
                    'What seasons or months does this crop grow in? E.g., spring, summer, fall, winter, autumn, january, february, march, april, may, june, july, august, september, october, november, december, frost, year-round\n'
                )
                harvestSeason = input(
                    'What seasons or months does this crop harvest in? E.g., spring, summer, fall, winter, autumn, january, february, march, april, may, june, july, august, september, october, november, december, frost, year-round\n'
                )
                averageGrowingTime = input(
                    'What is the average growing time for this crop?\n')
                averageYield = input(
                    "What is the average yield per harvest of this crop? E.g, must contains the crop's name, crop type, or weights(lbs, quart, pound)\n"
                )
                diseases = input(
                    'What are the potential disease for this crop?\n')
                nutritionalValue = input(
                    "What potential nutritional value does this crop contain? E.g., vitamin, iron, calcium, folate, magnesium\n"
                )
                soilWaterMoisture = input(
                    'What is the expected watering requirements for this crop?\n'
                )
                # Uncomment this section once the insert new function is working
                if (garden.insertNew(name, cropType, growingSeason,
                                     harvestSeason, averageGrowingTime,
                                     averageYield, diseases, nutritionalValue,
                                     soilWaterMoisture)):
                    successfulOperation = True
                    print('Successfuly added the new crop ', name,
                          ' to the list\n')
                    ''' # Depreciated
                    if (gardenType == '1'): # If the garden is using a sorted array
                        print('Attempting to sort the list...')
                        if (garden.sortList()): # Calls the sort function
                            print('The list has been sorted successuflly.')
                        else:
                            print('The list could not be sorted.')
                    '''
                else:
                    print('Could not add the crop ', name, ' to the list.')
            elif (userInput == 6):  # Remove Crop
                name = input('What is the name of the crop that you want to remove? ')
                success = garden.removeCrop(name)
                if (success):
                    successfulOperation = True
                    print('Successfuly removed ', name, ' from the list.')
                else:
                    print('Could not remove ', name,
                          ' from the list. (Perhaps it is not in the list?)')
            elif (userInput == 7):  # Modifiy Corp Information
                modifyKeywords = 'cropType, growingSeason, harvestSeason, averageGrowingTime, averageYield, diseases, nutritionalValue, soilWaterMoisture'
                name = input('Which crop are you looking to change? ')
                print('Using one of the following element keywords: ', modifyKeywords)
                element = input('Which element are you looking to change? ')
                replacement = input(
                    'What do you want to change that element to? ')
                success = garden.modifyCrop(name, element, replacement)
                if (success):
                    successfulOperation = True
                    print('Successfully changed ', element, ' in the crop ',
                          name, ' to ', replacement, '.\n')
                    print(garden.searchForCrop(name))
                    ''' # We don't really need to sort the array if we're not modifying the names
                    if (gardenType == '1'):  # If the garden is a sorted array
                        print('Attempting to sort the list...')
                        if (garden.sortList()): # Calls the sort function
                            print('The list has been sorted successuflly.')
                        else:
                            print('The list could not be sorted.')
                    '''
                else:
                    if (element == 'name'):
                        print('If you wish to change the name of the crop it is recommended to create a whole new crop and to delete the old one.')
                    else:
                        print('Could not change the ', element, ' in the crop ',
                          name, ' to ', replacement, '. Please try again.')
            elif (userInput == 8):  # Search for Crop
                crop = None
                name = input('What is the name of the crop that you want to search for? ')
                crop = garden.searchForCrop(name)
                if (crop == None):
                    print('Could not find a crop with the name ', name,
                          ' in the database.')
                else:
                    print(crop)
            elif (userInput == 9):  # Search for Crops by Information
                searchByInfoKeywords = 'name, cropType, growingSeason, harvestSeason, growingTime, yield, disease, nutritional, water, moisture'
                print('Using one of the following element keywords: ', searchByInfoKeywords)
                element = input('Which element do you want to search by? ')
                information = input(
                    'What information are you looking to find? ')
                matches, totalFinds = garden.searchByElements(
                    element, information)
                if (totalFinds == -1):
                    print('The element ', element, ' is invalid.')
                elif (totalFinds == 0):
                    print('No matches found for ', information,
                          ' in the element ', element, '.')
                else:
                    print('Dispalying ', totalFinds, ' matches.', '\n')
                    for i in matches:
                        print(i)
                    print('Found ', totalFinds, ' matches.')
            else:
                print('Invalid option selected.')
            if (autosave):  # If autosave is enabled (True)
                if (successfulOperation):
                    print(
                        'Autosaving to ', location, '...'
                    )  # Note: Only the load database feature can enable autosave, but the save to database function can change the autosave location
                    if (
                            garden.saveToFile(location)
                    ):  # We will save to the file that was either last loaded or last saved to
                        print('Save successful!')
                    else:
                        print('An error occured while trying to save to ',
                              location)
        return
    # end virtualGardenInterface()

    def programInformation():
        # Program Information and syntaxing help for the program
        # Implemented by Sierra
        print(
            '\n',
            'Listed below are directions and guidlines to help you make the most of your Virtual Garden'
        )
        #Option 2: Load Database
        print(
            '\n', '***', '\n',
            'Option 2 allows you to pull up all of the information it has for the entire garden. It will load all of the crop information that is stored within the database for use within the other Options. Simply press enter when prompted with "What is the file name of the file you would like to load?" to load the pre-loaded defalt garden database. Upon loading the database, please choose Option 4 if you would like to view the crop database. Loading the database also enables the autosave feature, so any work completed will automatically be saved to the file location that was initially chosen. To save to another file, you will need to reload the database.'
        )
        #Option 3: Save Database to File
        print(
            '\n', '***', '\n',
            'Option 3 allows you to save the crop database to a desired file. Choose...WIP'
        )
        #Option 4: Show List
        print(
            '\n', '***', '\n',
            'Option 4 allows you to show a list of all the crops featured in the database. It will feature the crop name, crop type, growing season, harvest season, average growing time, average yield, common diseases, nutritional value, and soil moisture content.You must use the Load Database feature in Option 3 before activating '
        )
        #Option 5: Insert New Crop
        print(
            '\n', '***', '\n',
            'Option 5 allows you to add a new crop to the database. You can enter all the crop information including, growing/harvest time, soil moisture content, etc.'
        )
        #Option 6: Remove Crop
        print(
            '\n', '***', '\n',
            'Option 6 allows you to remove a crop that you do not want present in the database any longer. It will remove all the crop-specific information as well. Please note that once a crop is deleted, that information is no longer accessible and will need to be manually re-entered.'
        )
        #Option 7: Modify Crop
        print(
            '\n', '***', '\n',
            'Option 7 allows you to modify specific information about a crop. You will be able to edit any element of the crop EXCEPT for the crop name. If you wish to change the name of the crop, you will need to simply remove the crop from the database using the Remove Crop function (Option 6) and enter the information with the new name manually.'
        )
        #Option 8: Search For Crop
        print(
            '\n', '***', '\n',
            'Option 8 allows you to search for a crop based on the crop name. You must type in the exact name of the crop in singluar form (i.e. "Pumpkins" is not accepted, but "Pumpkin" is). You do have the option to use lower or uppercase crop names (i.e. "Pumpkin" or "pumpkin").'
        )
        #Option 9: Search For Crop By Information
        print(
            '\n',
            '***',
            '\n',
            'Option 9 allows you to search for a grouping of crops by a category/element.',
            '\n',
            '\t',
            'When searching for a crop type, you will be allowed to narrow the search results based on the type of crop the produce stems from. The only acceptable terms are "plant", "bush", "tree", "fruit", "vegetable", "nut", or "squash".',
            '\n',
            '\t',
            'When searching for a growing seasons, you will be allowed to narrow down the search results based on the desired growth season. Acceptable terms include by season (spring, fall, summer, winter) or contain the month (January-December)',
            '\n',
            '\t',
            'When searching for harvesting seasons, acceptable terms include seasons (spring, summer, fall, winter) or months (January-December)',
            '\n',
            '\t',
            'When searching for average growing time, you will be able to search for a desired time frame and view a list of all crops associated with the given growth time.',  #narrow down results by timespan- 3 months, etc.??
            '\n',
            '\t',
            'When searching for average yield, you will be able to search for a specific crop yield and be provide',  # change all crops to yield by lbs
            '\n',
            '\t',
            'When searching for common diseases, you will be able to search for a specific disease and view a list of all the crops associated with that listed disease.',
            '\n',
            '\t',
            'When searching for nutritional benefits, you will be able to search for a specific nutrient such as "Vitamins" or "Potassium" and view a listi of crops which contain the given nutrient.',
            '\n',
            '\t',
            'When searching for soil moisture content, you will be able to narrow down the search results based on the desired soil/soil moisture level. The acceptable terms contain "well-draining loamy soil" or "fertile moist soil" for specificity.'
        )

        #Prints directions for each function; includes any parameters or specific keywords that must be used
        return

    # end programInformation()


if __name__ == "__main__":
    Interface.virtualGardenInterface()
