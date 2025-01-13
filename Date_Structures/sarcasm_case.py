def sarcasm(word: str) -> str:
  out: str = ""
  counter: int = 0
  for c in word:
    if counter % 2 == 0:
      out += c.upper()
    else:
      out += c
    counter += 1
  return out
if __name__ == "__main__":
  print(sarcasm("facebook pays it's taxes"))