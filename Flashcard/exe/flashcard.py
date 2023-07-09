from tkinter import *
from random import randint

root = Tk()
root.title("Flashcard App!")
root.geometry("450x850")
root.iconbitmap("")

########## Addition ##########
# Create Addition result checker
def addition_checker(num_1,num_2):
    correct = num_1 + num_2
    correct_answer = StringVar()
    incorrect_answer = StringVar()
    correct_answer.set("Correct, " + str(num_1) + " plus " + str(num_2) + " = " + str(correct))
    incorrect_answer.set("Incorrect, " + str(num_1) + " plus " + str(num_2) + " is " + str(correct) + ", not " + str(addition_answer.get()))
    if correct == int(addition_answer.get()):
        addition_answer_label.config(text=correct_answer.get())
    else:
        addition_answer_label.config(text=incorrect_answer.get())

    # clear the answer box
    addition_answer.delete(0, 'end')

    # Generate new random numbers
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0, 100))
    addition_flash.config(text=str(num_1.get()) + "+" + str(num_2.get()))

# Create Math functions
def add_menu():
    hide_menu_frames()
    add_frame.pack(fill="both", expand=1)
    # Generate two random numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    # Display generated random numbers in frame
    global addition_flash
    addition_flash = Label(add_frame, text=str(num_1.get()) + "+" + str(num_2.get()))
    addition_flash.pack(pady=10)
    #Create answer box
    global addition_answer
    addition_answer = IntVar()
    addition_answer = Entry(add_frame)
    addition_answer.pack(pady=10)
    # Create answer button
    addition_button = Button(add_frame, text="Answer", command=lambda: addition_checker(num_1.get(), num_2.get()))
    addition_button.pack(pady=10)
    # Create Answer Label
    # answer_label = Label(add_frame, text = "Enter your answer in the space above")
    # answer_label.pack(pady=10)
    global addition_answer_label
    addition_answer_label = Label(add_frame, text="Enter your answer in the space above")
    addition_answer_label.pack(pady=10)

########## Subtraction ##########
# Create Addition result checker
def subtraction_checker(num_1,num_2):
    correct = num_1 - num_2
    correct_answer = StringVar()
    incorrect_answer = StringVar()
    correct_answer.set("Correct, " + str(num_1) + " minus " + str(num_2) + " = " + str(correct))
    incorrect_answer.set("Incorrect, " + str(num_1) + " minus " + str(num_2) + " is " + str(correct) + ", not " + str(subtraction_answer.get()))
    if correct == int(subtraction_answer.get()):
        subtraction_answer_label.config(text=correct_answer.get())
    else:
        subtraction_answer_label.config(text=incorrect_answer.get())

    # clear the answer box
    subtraction_answer.delete(0, 'end')

    # Generate new random numbers
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0, 100))
    subtraction_flash.config(text=str(num_1.get()) + "-" + str(num_2.get()))

# Create Math functions
def subtraction_menu():
    hide_menu_frames()
    subtraction_frame.pack(fill="both", expand=1)
    # Generate two random numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    # Display generated random numbers in frame
    global subtraction_flash
    subtraction_flash = Label(subtraction_frame, text=str(num_1.get()) + "-" + str(num_2.get()))
    subtraction_flash.pack(pady=10)
    #Create answer box
    global subtraction_answer
    subtraction_answer = IntVar()
    subtraction_answer = Entry(subtraction_frame)
    subtraction_answer.pack(pady=10)
    # Create answer button
    subtraction_button = Button(subtraction_frame, text="Answer", command=lambda: subtraction_checker(num_1.get(), num_2.get()))
    subtraction_button.pack(pady=10)
    # Create Answer Label
    # answer_label = Label(add_frame, text = "Enter your answer in the space above")
    # answer_label.pack(pady=10)
    global subtraction_answer_label
    subtraction_answer_label = Label(subtraction_frame, text="Enter your answer in the space above")
    subtraction_answer_label.pack(pady=10)


########## Multiplication ##########
# Create Addition result checker
def multiplication_checker(num_1,num_2):
    correct = num_1 * num_2
    correct_answer = StringVar()
    incorrect_answer = StringVar()
    correct_answer.set("Correct, " + str(num_1) + " times " + str(num_2) + " = " + str(correct))
    incorrect_answer.set("Incorrect, " + str(num_1) + " times " + str(num_2) + " is " + str(correct) + ", not " + str(multiplication_answer.get()))
    if correct == int(multiplication_answer.get()):
        multiplication_answer_label.config(text=correct_answer.get())
    else:
        multiplication_answer_label.config(text=incorrect_answer.get())

    # clear the answer box
    multiplication_answer.delete(0, 'end')

    # Generate new random numbers
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0, 100))
    multiplication_flash.config(text=str(num_1.get()) + "*" + str(num_2.get()))

# Create Math functions
def multiplication_menu():
    hide_menu_frames()
    multiplication_frame.pack(fill="both", expand=1)
    # Generate two random numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    # Display generated random numbers in frame
    global multiplication_flash
    multiplication_flash = Label(multiplication_frame, text=str(num_1.get()) + "*" + str(num_2.get()))
    multiplication_flash.pack(pady=10)
    #Create answer box
    global multiplication_answer
    multiplication_answer = IntVar()
    multiplication_answer = Entry(multiplication_frame)
    multiplication_answer.pack(pady=10)
    # Create answer button
    multiplication_button = Button(multiplication_frame, text="Answer", command=lambda: multiplication_checker(num_1.get(), num_2.get()))
    multiplication_button.pack(pady=10)
    # Create Answer Label
    # answer_label = Label(add_frame, text = "Enter your answer in the space above")
    # answer_label.pack(pady=10)
    global multiplication_answer_label
    multiplication_answer_label = Label(multiplication_frame, text="Enter your answer in the space above")
    multiplication_answer_label.pack(pady=10)

########## Division ##########
# Create Addition result checker
def division_checker(num_1,num_2):
    correct = num_1 / num_2
    correct_answer = StringVar()
    incorrect_answer = StringVar()
    correct_answer.set("Correct, " + str(num_1) + " divided by " + str(num_2) + " = " + str(correct))
    incorrect_answer.set("Incorrect, " + str(num_1) + " divided by " + str(num_2) + " is " + str(correct) + ", not " + str(division_answer.get()))
    if correct == float(division_answer.get()):
        division_answer_label.config(text=correct_answer.get())
    else:
        division_answer_label.config(text=incorrect_answer.get())

    # clear the answer box
    division_answer.delete(0, 'end')

    # Generate new random numbers
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(1,100))
    num_2.set(randint(1, 100))
    division_flash.config(text=str(num_1.get()) + "-" + str(num_2.get()))

# Create Math functions
def division_menu():
    hide_menu_frames()
    division_frame.pack(fill="both", expand=1)
    # Generate two random numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(1,100))
    num_2.set(randint(1,100))
    # Display generated random numbers in frame
    global division_flash
    division_flash = Label(division_frame, text=str(num_1.get()) + "/" + str(num_2.get()))
    division_flash.pack(pady=10)
    #Create answer box
    global division_answer
    division_answer = IntVar()
    division_answer = Entry(division_frame)
    division_answer.pack(pady=10)
    # Create answer button
    division_button = Button(division_frame, text="Answer", command=lambda: division_checker(num_1.get(), num_2.get()))
    division_button.pack(pady=10)
    # Create Answer Label
    # answer_label = Label(add_frame, text = "Enter your answer in the space above")
    # answer_label.pack(pady=10)
    global division_answer_label
    division_answer_label = Label(division_frame, text="Enter your answer in the space above")
    division_answer_label.pack(pady=10)

# Hide Frame Function when not called and destroy each frame's children widget when reloaded
def hide_menu_frames():
    for widget in add_frame.winfo_children():
        widget.destroy()
    add_frame.pack_forget()
    for widget in subtraction_frame.winfo_children():
        widget.destroy()
    subtraction_frame.pack_forget()
    for widget in division_frame.winfo_children():
        widget.destroy()
    division_frame.pack_forget()
    for widget in multiplication_frame.winfo_children():
        widget.destroy()
    multiplication_frame.pack_forget()
    for widget in start_frame.winfo_children():
        widget.destroy()
    start_frame.pack_forget()
# define Main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

def home_menu():
    hide_menu_frames()
    global start_frame
    start_frame = Frame(root, width=400, height=400)
    start_frame.pack(fill="both", expand=1)
    Label(start_frame, text="Welcome to Math Flashcards!", font=("Helvetica, 18")).pack(pady=50)
    # Start buttons
    a_button = Button(start_frame, text="Click to Start Addition Flashcards", command=add_menu).pack(pady=10)
    s_button = Button(start_frame, text="Click to Start Subtraction Flashcards", command=subtraction_menu).pack(pady=10)
    m_button = Button(start_frame, text="Click to Start Multiplication Flashcards", command=multiplication_menu).pack(pady=10)
    d_button = Button(start_frame, text="Click to Start Division Flashcards", command=division_menu).pack(pady=10)


#Create Main Menu
math_menu = Menu(my_menu)
my_menu.add_cascade(label="MathCards", menu=math_menu)
math_menu.add_command(label="Addition", command=add_menu)
math_menu.add_command(label="Subtraction", command=subtraction_menu)
math_menu.add_command(label="Multiplication", command=multiplication_menu)
math_menu.add_command(label="Division", command=division_menu)
math_menu.add_separator()
math_menu.add_command(label="Home", command=home_menu)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=root.quit)

# Create Maths Frames
add_frame = Frame(root, width=450, height=850, bg="blue")
subtraction_frame = Frame(root, width=450, height=850, bg="red")
division_frame = Frame(root, width=450, height=850, bg="yellow")
multiplication_frame = Frame(root, width=450, height=850, bg="green")
start_frame = Frame(root, width=450, height=850)


# Start Screen
home_menu()

root.mainloop()