# Write a program that reads a number from the standard input and
# then draws a chess table of the specified size
#
# Example:
#
# Please enter the chess table size: 8
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
if __name__ == "__main__":
  size = int(input("Please enter the chess table size: "))
  for i in range(size):
    for j in range(size):
      if (j + i) % 2 == 0:
        print("%", end="")
      else:
        print(" ", end="")
    print()