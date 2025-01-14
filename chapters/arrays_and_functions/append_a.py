# - Create a variable named `typo` and assign the value `Chinchill` to it
# - Write a function called `append_a()` that gets a string as an input,
#   appends an 'a' character to its end and returns with a string
# - Print the result of `append_a(typo)`
def append_a(string: str) -> str:
  return string + "a"
if __name__ == "__main__":
  typo = "Chinchill"
  print(append_a(typo))