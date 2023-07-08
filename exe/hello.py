from tkinter import *
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import ImageTk, Image

# Create a Tkinter instance (root window) to start developing a Tkinter project. Name the window (.title) and provide
# the default size (.size)
root = Tk()
root.title("Hello World!")
root.geometry("1800x900")
root.iconbitmap("/Users/Deepee/Desktop/Desktop/LEARN/Intro to tkinter widgets - C/tkinter widgets/ade.png")
# # #
# # # #Define a Menu
# # # my_menu = Menu(root)
# # # root.config(menu=my_menu)
# # #
# # # # Create "File" Menu items
# # # def fake_command():
# # #     pass
# # #
# # #
# # # file_menu = Menu(my_menu)
# # # my_menu.add_cascade(label="File", menu=file_menu)
# # # file_menu.add_command(label="New", command=fake_command)
# # # file_menu.add_separator()
# # # file_menu.add_command(label="Exit", command=root.quit)
# # #
# # # # Create "Edit" Menu items
# # # def fake_command():
# # #     pass
# # #
# # # edit_menu = Menu(my_menu)
# # # my_menu.add_cascade(label="Edit",menu=edit_menu)
# # # edit_menu.add_command(label="Cut", command=fake_command)
# # # edit_menu.add_separator()
# # # edit_menu.add_command(label="Copy", command=fake_command)
# # # edit_menu.add_command(label="Paste", command=fake_command)
# # # #
# # # # # Add Images
# # # # # my_image = ImageTk.PhotoImage(Image.open("ade.png"))
# # # # # image_label = Label(image=my_image)
# # # # # image_label.pack()
# # # #
# # # # # Create Labels
# # # # my_label = Label(root, text="Hello!", fg="green", relief="raised")
# # # # my_label.pack(pady=20)
# # # #
# # # # my_label_1 = Label(root, text="Hello World!", fg="green", relief="raised")
# # # # my_label_1.pack(pady=20)
# # # #
# # # # my_label_2 = Label(root, text="Hello World Again!", bg="blue", relief="sunken", cursor="arrow")
# # # # my_label_2.pack(pady=20)
# # # #
# # # # # Create input boxes/Entry widgets and get the value input in the box
# # # # my_entry = Entry(root, width=20, font="Ariel")
# # # # my_entry.pack()
# # # #
# # # #
# # # # # Create a clickable and functional button that prints the input box entry
# # # # def clicked():
# # # #     global entry, display_entry
# # # #     entry = my_entry.get()
# # # #     display_entry = Label(root, text=entry)
# # # #     display_entry.pack()
# # # #
# # # #
# # # def hide():
# # #     display_entry.pack_forget()
# # #     # display_entry.destroy()
# # #
# # #
# # # def show():
# # #     display_entry.pack()
# # # #
# # # #
# # # # # To pass params into functions being called by command, use the format below
# # # # # my_button = Button(root, text="click ME!", command=lambda: clicked(params)
# # # # my_button = Button(root, text="Print my text!", command=clicked)
# # # # my_button.pack(pady=20)
# # # #
# # # # hide_button = Button(root, text="Hide!", command=hide)
# # # # hide_button.pack(pady=20)
# # # #
# # # # show_button = Button(root, text="Show!", command=show)
# # # # show_button.pack(pady=20)
# # #
# # # # Create buttons in frames
# # # shows_button = Button(root, text="Show!", command=show)
# # # hides_button = Button(root, text="Hide!", command=hide)
# # #
# # # shows_button.pack(pady=20)
# # # hides_button.pack()
# # #
# # # # Define frame
# # # my_frame = Frame(root, width=200, height=200, bd = 5, bg = "blue", relief="sunken")
# # # my_frame.pack(pady=20)
# # # my_frame = Label(my_frame, text="Here you are")
# # # my_frame.pack(pady=20)
# # #
# # # # Create radio buttons
# # # def radio():
# # #     my_label = Label(root, text=v.get()).pack()
# # #
# # # v = StringVar()
# # # v.set("Egusi")
# # #
# # # r1 = Radiobutton(root, text="Egusi", variable=v, value="Egusi").pack()
# # # r1 = Radiobutton(root, text="Efo riro", variable=v, value="Efo riro").pack()
# # # r1 = Radiobutton(root, text="Ewedu", variable=v, value="Ewedu").pack()
# # #
# # # radio_button = Button(root, text="Click to print your selection", command=radio).pack()
# # #
# # # # Create check buttons
# # # def check():
# # #     my_label = Label(root, text=v.get()).pack()
# # #
# # # v = StringVar()
# # # v.set("Egusi")
# # #
# # # c1 = Checkbutton(root, text="Egusi", variable=v, onvalue="Egusi", offvalue="Efo riro")
# # # c1.deselect()
# # # c1.pack()
# # #
# # #
# # # check_button = Button(root, text="Click to print your selection", command=check).pack()
# # #
# # # Create pop up boxes - showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# #
# # def popup():
# #     response = messagebox.askyesno("Title", "Message")
# #     my_label = Label(root, text=response).pack()
# #
# # pop_button = Button(root, text="Click To Pop up", command=popup).pack()
# #
# #
# Create New Window

# def open_window():
#     new = Toplevel()
#     new.title("Hello World page 2!")
#     new.geometry("800x900")
#
#     my_label = Label(new, text="here's my second window").pack()
#
#     my_img = ImageTk.PhotoImage(Image.open("ade.png"))
#     img_label = Label(new, image=my_img).pack(pady=10)
#     new.mainloop()

# def open_image():
#     root.filename = filedialog.askopenfile(initialdir="/tkinter widgets", title="Open an image file", filetypes=(
#     ("Png File", "*.png"), ("Icon files", "*.ico"), ("All Files", "*.*")))
#     my_label = Label(root, text=root.filename).pack(pady=20)
#
#
# my_button = Button(root, text="Open Image", command=open_image).pack(pady=10)
#
#
# Create Combo boxes (drop down menu)
#
# def select():
#     my_label = Label(root, text=my_combo.get()).pack()
#
# options = ["Monday", "Tuesday", "Wednesday"]
#
# my_combo = ttk.Combobox(root, value=options)
# my_combo.current(0)
# my_combo.pack(pady=10)
#
# my_button = Button(root, text="Select", command=select).pack()
# #
# #
# # # #Create status bar
# # # current_status = StringVar()
# # # current_status.set("Waiting!")
# # # my_status = Label(root, textvariable=current_status, bd=2, relief="sunken", width="55", anchor=E)
# # # my_status.pack()

# Create Color Chooser

def color():
    my_color = colorchooser.askcolor()
    print(my_color)
    my_label = Label(root, text=my_color).pack()

my_button = Button(root, text="Display Color Palette", command=color).pack()

# Create a looping point for Tkinter. Loop = instance to .mainloop
root.mainloop()
