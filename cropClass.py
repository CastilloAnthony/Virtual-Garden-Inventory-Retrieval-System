'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  09/18/2022
  CS-3100
  Professor Hatem
'''


# This will be the base class for every crop added into our data structure.
class Crop:

    def __init__(self):
        # The Classes' variables.
        # Implemented by Anthony Castillo
        self.__name = ""
        self.__cropType = ""
        self.__growingSeason = ""
        self.__harvestSeason = ""
        self.__averageGrowingTime = ""
        self.__averageYield = ""
        self.__diseases = ""
        self.__nutritionalValue = ""
        self.__soilWaterMoisture = ""
        self.__monthsSeasons = {
            'spring', 'summer', 'fall', 'winter', 'autumn', 'january',
            'february', 'march', 'april', 'may', 'june', 'july', 'august',
            'september', 'october', 'november', 'december', 'frost', 'year'
        }  # year-round # Is not needed in here because the 'year' parameter covers it.

    # end __init__()

    def __del__(self): # Default deconstructor deletes all the variables before going out of scope.
        # Implemented by Anthony Castillo
        del self.__name
        del self.__cropType
        del self.__growingSeason
        del self.__harvestSeason
        del self.__averageGrowingTime
        del self.__averageYield
        del self.__diseases
        del self.__nutritionalValue
        del self.__soilWaterMoisture
        del self.__monthsSeasons
      
    def __str__(self):
        # Returns all of the information contained within this crop in a (human readable string) formatted manner.
        # Implemented by Anthony Castillo
        information = 'Crop Name: \t\t\t\t' + self.get_name(
        ) + '\n' + 'Crop Type: \t\t\t\t' + self.get_cropType(
        ) + '\n' + 'Growing Season: \t\t' + self.get_growingSeason(
        ) + '\n' + 'Harvest Season: \t\t' + self.get_harvestSeason(
        ) + '\n' + 'Average Growing Time: \t' + self.get_averageGrowingTime(
        ) + '\n' + 'Average Yield: \t\t\t' + self.get_averageYield(
        ) + '\n' + 'Diseases: \t\t\t\t' + self.get_diseases(
        ) + '\n' + 'Nutritional Values: \t' + self.get_nutritionalValue(
        ) + '\n' + 'Soil Water Moisture: \t' + self.get_soilWaterMoisture(
        ) + '\n'  # \t is a tab, \n is a newline
        return information

    # end __str__()

    def pullDataCSV(self):
        # Returns all of the information contained within this crop in a csv (list) friendly manner.
        # Implemented by Anthony Castillo
        information = []
        information.append(self.get_name())
        information.append(self.get_cropType())
        information.append(self.get_growingSeason())
        information.append(self.get_harvestSeason())
        information.append(self.get_averageGrowingTime())
        information.append(self.get_averageYield())
        information.append(self.get_diseases())
        information.append(self.get_nutritionalValue())
        information.append(self.get_soilWaterMoisture())
        return information

    # end pullDataCSV()

    # Below here we will define all other functions that our class will use and need like the functions to actually set the values for the class and retrieve those values.

    # Amanjoit will do the name; cropType; growingSeason
    # Implemted by Amanjoit Kaur
    # For the growingSeason, since some plants are grown towards the mid of the month, for those plants when searched you will see that they are grown in Mid-Spring or Mid-Summer or Mid-Fall.
    def get_name(self):
        return self.__name
        # Implemented by Amanjoit Kaur

    # end get_name()

    def set_name(self, name):  # Returns True on success or false on a failure.
        # Implemented by Amanjoit Kaur
        # Minor modifications by Anthony Castillo
        #self.__name = name
        if (name.isdigit() != True):  #isinstance(name, str)):
            self.__name = name
            return True
        return False
    # end set_name()

    def get_cropType(self):
        # Implemented by Amanjoit Kaur
        return self.__cropType

    # end get_cropType()

    def set_cropType(
            self, cropType):  # Returns True on success or false on a failure.
        # Implemented by Amanjoit Kaur
        # Minor modifications by Anthony Castillo
        cropTypeDictionary = {
            'plant', 'bush', 'tree', 'fruit', 'vegetable', 'nut', 'squash'
        }
        for i in cropTypeDictionary:
            if (i in cropType.lower()):
                self.__cropType = cropType
                return True
        return False

    # end set_cropType()

    def get_growingSeason(self):
        # Implemented by Amanjoit Kaur
        return self.__growingSeason

    # end get_growingSeason()

    def set_growingSeason(
            self,
            growingSeason):  # Returns True on success or false on a failure.
        # Implemented by Amanjoit Kaur
        # Minor modifications by Anthony Castillo
        for i in self.__monthsSeasons:
            if (i in growingSeason.lower()):
                self.__growingSeason = growingSeason
                return True
        return False

    # end set_growingSeason()

    # Anthony will do the harvestSeason; averageGrowingTime; averageYield

    def set_harvestSeason(
            self,
            harvestSeason):  # Returns True on success or false on a failure.
        # Implemented by Anthony Castillo
        '''
        # modify by Amanjoit - for set_harvestSeason in garden class for new crop, commented out extraHarvestParameters because it's not complete, string should be parsed. remediated to only accept monthsSeasons
        # What? - Anthony
        '''
        # Should be in the format of "Summer" or "August to September" or "Late Summer to Early Fall"
        extraHarvestParameters = {'months old', 'days from planting'}
        for i in self.__monthsSeasons:
            if (i in harvestSeason.lower()):
                self.__harvestSeason = harvestSeason
                return True
        for i in extraHarvestParameters:
            if (i in harvestSeason.lower()):
                self.__harvestSeason = harvestSeason
                return True
        return False

    # end set_harvestSeason()

    def get_harvestSeason(self):
        # Implemented by Anthony Castillo
        return self.__harvestSeason

    # end get_harvestSeason()

    def set_averageGrowingTime(
            self, averageGrowingTime
    ):  # Returns True on success or false on a failure.
        # Implemented by Anthony Castillo
        # Should be in the format of "60 to 100 Days" or "2-3 Years"
        daysYears = {'day', 'month', 'year'}
        for i in daysYears:
            if (i in averageGrowingTime.lower()):
                self.__averageGrowingTime = averageGrowingTime
                return True
        return False

    # end set_averageGrowingTime()

    def get_averageGrowingTime(self):
        # Implemented by Anthony Castillo
        return self.__averageGrowingTime

    # end get_averageGrowingTime()

    def set_averageYield(
            self,
            averageYield):  # Returns True on success or false on a failure.
        # Implemented by Anthony Castillo
        # Should be in the format of lbs, quarts, pounds

        yields = {'lbs', 'quart', 'pound'}  # , 'bells', 'chilies'

        if (self.get_name().lower()
                in averageYield.lower()):  # apples, oranges, grapes, etc.
            self.__averageYield = averageYield
            return True

        if (self.get_cropType().lower()
                in averageYield.lower()):  # tree, plant, bush, etc.
            self.__averageYield = averageYield
            return True

        for i in yields:
            if (i in averageYield.lower()):
                self.__averageYield = averageYield
                return True
        return False

    # end set_averageYield()

    def get_averageYield(self):
        # Implemented by Anthony Castillo
        return self.__averageYield

    # end get_averageYield()

    # Sierra will do the diseases; nutrition; waterSoilMoisture
    def get_diseases(self):
        # Implemented by Sierra
        return self.__diseases

    # end get_diseases()

    def set_diseases(
            self, diseases):  # Returns True on success or false on a failure.
        #Implemented by Sierra
        # Modified by Anthony Castillo
        if (diseases.isdigit() !=
                True):  # Checks to see if the user input only numbers
            self.__diseases = diseases
            return True
        return False

    # end set_diseases()

    def get_nutritionalValue(self):
        #Implemented by Sierra
        return self.__nutritionalValue

    # end get_nutritionalValue()

    def set_nutritionalValue(
            self, nutritionalValue
    ):  # Returns True on success or false on a failure.
        # Implemented by Sierra
        # Minor modifications by Anthony Castillo
        nutritionalValueDictionary = {
            'vitamin', 'iron', 'calcium', 'folate', 'magnesium'
        }
        for i in nutritionalValueDictionary:
            if (i.lower() in nutritionalValue.lower()):
                self.__nutritionalValue = nutritionalValue
                return True
        return False

    # end set_nutritionalValue()

    def get_soilWaterMoisture(self):
        #Implemented by Sierra
        return self.__soilWaterMoisture

    # end get_soilWaterMoisture()

    def set_soilWaterMoisture(
            self, soilWaterMoisture
    ):  # Returns True on success or false on a failure.
        #Implemented by Sierra
        # Modified by Anthony Castillo
        if (soilWaterMoisture.isdigit() != True):
            self.__soilWaterMoisture = soilWaterMoisture
            return True
        return False

    # end set_soilWaterMoisture()
# end Crop class
