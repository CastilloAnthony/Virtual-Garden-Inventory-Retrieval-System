'''
  Virtual Garden Inventory System
  Anthony Castillo
  Sierra Pangilinan
  Amanjoit Kaur
  10/12/2022
  CS-3100
  Professor Hatem
'''
# Dictionary Linked List Implemented by Amanjoit Kaur- 10/14/2022

from abc import ABC, abstractmethod
# ABC is an object and it lets python know that we are inhereting an abstract class. 
class DictAbstract(ABC):
    
  # This tells you the size of the dictionary. 
  @abstractmethod
  def size(self):
    pass
  # This is where you will be allowed to update any elements in the dictionary. 
  def update_element(self):
    pass
  # This can be written if you want it to be used for returnable boolean. Yes or no if its empty.
  @abstractmethod
  def is_empty(self):
    pass
  # Here you will be able to find the element in the dictionary. 
  @abstractmethod
  def find_element(self):
    pass
    # Here you will be able to add the element in the dictionary. 
  @abstractmethod
  def add_element(self):
    pass
     # Here you will be able to remove the element in the dictionary. 
  @abstractmethod
  def remove(self):
    pass
# Here you are bale to return the length of the list.
  @abstractmethod
  def __len__(self): 
    pass 
# Here you are able to return all the content in the list. 
  @abstractmethod
  def __str__(self):
    pass
# Here you can define how the calss behaves when at the right side of the "in" operator (or "not in").
  @abstractmethod
  def __contains__(self, key): 
    pass
# Here you are able to return the value paired with the specific key that was given to the function. 
  @abstractmethod
  def __getitem__(self, key):
    pass
# Here you are adding a new crop to the end of the dictionary. 
  @abstractmethod
  def append(self):
    pass