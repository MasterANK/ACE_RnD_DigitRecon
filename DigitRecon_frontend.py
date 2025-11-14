from tkinter import *

root = Tk()
root.title("Digit Recognition GUI")
root.geometry("300x350")

# canvas
canvas = Canvas(root, bg="white", width=280, height=250)
canvas.pack(pady=10)

# label
label = Label(root, text="Draw here with mouse")
label.pack()

# frame
button_frame = Frame(root)
button_frame.pack(pady=5)

# clear button
def clear_canvas():
    canvas.delete("all")

# predict button
def predict_digit():
    label.config(text="Predicted Digit: 5")

# buttons
Button(button_frame, text="Clear", width=10, command=clear_canvas).pack(side=LEFT, padx=10)
Button(button_frame, text="Predict", width=10, command=predict_digit).pack(side=LEFT, padx=10)

# drawing part
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, width=8, fill='black', capstyle=ROUND)
    last_x, last_y = event.x, event.y

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()
