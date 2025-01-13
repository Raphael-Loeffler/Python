# - Create a function called `calculateFactorial()`
#   that returns the factorial of its input
#
# - Example: calculateFactorial(5) = 1 * 2 * 3 * 4 * 5 = 120
def calculateFactorial(number: int) -> int:
  out = 1
  for i in range(1, number + 1):
    out = out * i
  return out
if __name__ == "__main__":
  print(calculateFactorial(5))