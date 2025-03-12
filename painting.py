import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab

root = tk.Tk()
root.title("برنامه نقاشی با موس")
root.geometry("600x500")

current_color = "black"
pen_size = tk.IntVar(value=10)
current_tool = "pen"

canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack(fill=tk.BOTH, expand=True)

def draw(event):
    x1, y1 = event.x - pen_size.get(), event.y - pen_size.get()
    x2, y2 = event.x + pen_size.get(), event.y + pen_size.get()

    if current_tool == "pen":
        canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)
    elif current_tool == "line":
        canvas.create_line(event.x, event.y, event.x + 50, event.y + 50, fill=current_color, width=pen_size.get())
    elif current_tool == "rectangle":
        canvas.create_rectangle(event.x, event.y, event.x + 50, event.y + 50, outline=current_color, width=pen_size.get())
    elif current_tool == "circle":
        canvas.create_oval(event.x, event.y, event.x + 50, event.y + 50, outline=current_color, width=pen_size.get())

def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def clear_canvas():
    canvas.delete("all")

def save_canvas():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    
    ImageGrab.grab().crop((x, y, x1, y1)).save("drawing.png")
    print("تصویر ذخیره شد!")

def set_tool(tool):
    global current_tool
    current_tool = tool

def add_text():
    text = text_entry.get()
    if text:
        canvas.create_text(250, 200, text=text, fill=current_color, font=("Arial", 20))

canvas.bind("<B1-Motion>", draw)

btn_color = tk.Button(root, text="انتخاب رنگ", command=change_color)
btn_color.pack(side=tk.LEFT, padx=5)

size_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, variable=pen_size, label="ضخامت قلم")
size_slider.pack(side=tk.LEFT, padx=5)

btn_pen = tk.Button(root, text="قلم", command=lambda: set_tool("pen"))
btn_pen.pack(side=tk.LEFT, padx=5)

btn_line = tk.Button(root, text="خط", command=lambda: set_tool("line"))
btn_line.pack(side=tk.LEFT, padx=5)

btn_rect = tk.Button(root, text="مستطیل", command=lambda: set_tool("rectangle"))
btn_rect.pack(side=tk.LEFT, padx=5)

btn_circle = tk.Button(root, text="دایره", command=lambda: set_tool("circle"))
btn_circle.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(root, text="پاک کردن", command=clear_canvas)
btn_clear.pack(side=tk.RIGHT, padx=5)

btn_save = tk.Button(root, text="ذخیره تصویر", command=save_canvas)
btn_save.pack(side=tk.RIGHT, padx=5)

text_entry = tk.Entry(root)
text_entry.pack(side=tk.LEFT, padx=5)

btn_text = tk.Button(root, text="افزودن متن", command=add_text)
btn_text.pack(side=tk.LEFT, padx=5)

root.mainloop()