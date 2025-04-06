print("Starting")

try:
  print(x)
except NameError as error:
  print(f"NameError: {error}")
except ZeroDivisionError as error:
  print(f"ZeroDivisionError: {error}")
except Exception as e:
  print(e.with_traceback())
finally:
  print("finally block")

print("End")

print("________________________________________")
print()

#Ternary operator
x = 10
y = ""
if x > 50:
  y = "more than 50"
else:
  y = "less than 50"
  
print(y)
print("With ternary")
y = "more than 50" if x > 50 else "less than 50"
print(y)

print("________________________________________")
print()

#List comprehension
numbers = []
for number in range(1, 11):
  if number % 2 == 1:
    numbers.append(number)
  else:
    numbers.append("even")
print(numbers)

print("List comprehension")

numbers_comprehension = [number if number % 2 == 1 else "even" for number in range(1, 11)]
print(numbers_comprehension)

print("________________________________________")
print()

# lambda functions

def normal_function():
  print("normal function")

normal_function()

x = lambda: print("lambda function")
x()