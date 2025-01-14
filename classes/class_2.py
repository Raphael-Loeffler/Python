from pathlib import Path
from string import ascii_lowercase, ascii_uppercase
"""
import math
import sys
import os
import time
import string

PIP
"""
empty_list_1 = [] # <- better
empty_list_2 = list()

empty_tuple_1 = () # <- better
empty_tuple_2 = tuple()
empty_tuple_3 = tuple(empty_list_1)

empty_set_1 = {}
empty_set_2 = set()
set_example = {1, 2, 3, 4, 4, 5, 5, 6, 6}
print(f"{set_example=}")

print(f"{empty_list_1}")
print(f"{empty_list_2=}")

print(f"{type(empty_list_1)=}")
print(f"{type(empty_list_2)=}")

def number_square(number):
  """_summary_

  Args:
      number (_type_): _description_

  Returns:
      _type_: _description_
  """
  return number ** 2
#qrint(help(number_square))
#print(number_square.__doc__)
# always put dogstrings in functions
print("_______________________________")
print()

class Creature:
  """
  name -> public
  _name -> protected
  __name -> private
  """
  def __init__(self, height, weight, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.height = height
    self.weight = weight
  
  def breathe(self):
    print("I can breathe")

class Employee:
  def __init__(self, salary, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self.salary = salary
  
  def working(self) -> None:
    print("I am working")

class Person(Creature, Employee):
  def __init__(self, name, weight, height, salary) -> None:
    super().__init__(height=height, weight=weight, salary=salary)
    self.name = name
  def walk(self) -> None:
    print("I walk")

if __name__ == "__main__":
  michalis = Person("Michalis", weight=83, height=185, salary=1_000)
  #michalis.walk()
  print(f"{michalis.name}")
  print(f"{michalis.weight}")
  print(f"{michalis.height}")
  michalis.breathe()
  print(f"{michalis.salary}")
  
  print("_______________________________")
  print()
  
  PATH_ROOT_DIR = Path(__file__).parent
  PATH_FILE = PATH_ROOT_DIR / "text.txt"
  
  with open(PATH_FILE, "r") as file:
    lines = file.readlines()
    """
    print(lines)
    for line in lines:
      print(line)
    file.write("Prague") """
    for index, line in enumerate(lines):
      print(f"{index + 1}. {line}")
  
  print("_______________________________")
  print()
  
  print(type(3))
  #word = input("Give me a word: ")
  #print(f"{word=}")
  print(len("frtszaz"))
  numbers = [1, 2, 3, 4, 1, 2]
  print(f"{max(numbers)=}")
  print(f"{min(numbers)=}")
  print(f"{sum(numbers)=}")
  sorted_numbers = sorted(numbers)
  print(sorted_numbers)
  names = ["aa", "AA", "bbbb", "B"]
  sorted_names = sorted(names)
  print(sorted_names)
  #zip, filter, map, eval -> useful functions
  exec("x = 5")
  print(f"{x=}")
  print(ascii_lowercase)
  print(ascii_uppercase)