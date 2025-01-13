from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def line_play():
  for i in range(20, 280, 20):
    line1 = canvas.create_line(i, 290, 10, i, fill="green")
    line2 = canvas.create_line(300 - i, 10, 290, 300 - i, fill="purple")

if __name__ == "__main__":
  line_play()

root.mainloop()