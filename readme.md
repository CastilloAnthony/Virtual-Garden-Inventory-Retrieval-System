'''
  Virtual Garden Inventory System
  Anthony Castillo
  Amanjoit Kaur
  Sierra Pangilinan
  09/06/2022
  CS-3100
  Professor Hatem
'''

This is the Virtual Garden Inventory System. It can read .csv files formated with nine comma delimited columns and add them to a list. If no .csv file is specified then the system will try to read from a file called gardenDatabase.csv. This system can add new crops, remove old crops, or modify crops in the list. (Note: For the modify cropy function, you can not modify the name of a crop, you are only allowed to modify the elements of that crop. If you need to modify the name of a crop then you need to create a whole new crop to take its place.) Additionally, the system can search through the list of crops and identify crops that have the requested name or it can search through the list and identify multiple crops with matching information in their specified element categories (i.e., growing season, harvest season, diseases, etc.).