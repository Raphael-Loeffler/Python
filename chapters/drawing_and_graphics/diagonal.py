from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws a single line
# Use this function to draw the canvas' diagonals
# If the line starts from the upper-left corner it should be green, otherwise it should be red
# Make decision about the color in the function
#blackline = canvas.create_line(0, 0, 300, 300)
def drawDiagonal(x1, y1, x2, y2):
  if x1 == 0 and y1 == 0:
    line = canvas.create_line(x1, y1, x2, y2, fill="red")
  else:
    line = canvas.create_line(x1, y1, x2, y2, fill="black")

if __name__ == "__main__":
  drawDiagonal(0, 0, 300, 300)
  drawDiagonal(300, 0, 0, 300)
root.mainloop()