# Accidentally I messed up this quote from Richard Feynman
# Two words are out of place
# Your task is to fix it by swapping the right words with code
# To do this: create a method called "swap_quote()"
# Expected output: "What I cannot create I do not understand."
def swap_quote(list_):
  temp = list_[5]
  list_[5] = list_[2]
  list_[2] = temp
  return list_
if __name__ == "__main__":
  words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]
  print(swap_quote(words))