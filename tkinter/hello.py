from tkinter import *
from PIL import ImageTk, Image

# Create a Tkinter instance (root window) to start developing a Tkinter project. Name the window (.title) and provide
# the default size (.size)
root = Tk()
root.title("Hello World!")
root.geometry("1800x900")
root.iconbitmap("/Users/Deepee/Desktop/Desktop/LEARN/Intro to tkinter - C/tkinter/ade.png")

# Add Images
my_image = ImageTk.PhotoImage(Image.open("ade.png"))
image_label = Label(image=my_image)
image_label.pack()

# Label is the heading of the program. Think of 'H1' in HTML. .pack or .grid always follows a command to display the
# command in the window
my_label = Label(root, text="Hello!", fg="green", relief="raised")
my_label.pack(pady=20)

my_label_1 = Label(root, text="Hello World!", fg="green", relief="raised")
my_label_1.pack(pady=20)

my_label_2 = Label(root, text="Hello World Again!", bg="blue", relief="sunken", cursor="arrow")
my_label_2.pack(pady=20)

# Create input boxes/Entry widgets and get the value input in the box
my_entry = Entry(root, width=20, font="Ariel")
my_entry.pack()


# Create a clickable and functional button that prints the input box entry
def clicked():
    global entry, display_entry
    entry = my_entry.get()
    display_entry = Label(root, text=entry)
    display_entry.pack()


def hide():
    display_entry.pack_forget()
    # display_entry.destroy()


def show():
    display_entry.pack()


# To pass params into functions being called by command, use the format below
# my_button = Button(root, text="click ME!", command=lambda: clicked(params)
my_button = Button(root, text="Print my text!", command=clicked)
my_button.pack(pady=20)

hide_button = Button(root, text="Hide!", command=hide)
hide_button.pack(pady=20)

show_button = Button(root, text="Show!", command=show)
show_button.pack(pady=20)

# Create a looping point for Tkinter. Loop = instance to .mainloop
root.mainloop()
