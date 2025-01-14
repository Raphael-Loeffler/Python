#Create a function named build() following your current language's style guide.
#It should take a string, create a palindrome from it and then return it.
def build(word: str) -> str:
  return word + word[::-1]
if __name__ == "__main__":
  print(build("fox"))