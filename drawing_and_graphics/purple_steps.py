from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws a single line
# Use this function to draw the canvas' diagonals
# If the line starts from the upper-left corner it should be green, otherwise it should be red
# Make decision about the color in the function
#blackline = canvas.create_line(0, 0, 300, 300)
def purple_steps():
  for i in range(20, 250, 20):
    box = canvas.create_rectangle(i, i, i + 20, i + 20, fill="purple")

if __name__ == "__main__":
  purple_steps()
root.mainloop()