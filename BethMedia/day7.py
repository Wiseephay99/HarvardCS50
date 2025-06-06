print()

# Graphic User Interface using TKINTER
'''
Introduction to tkinter
tkinter is a standard Python library used to create simple graphical user interfaces (GUls). It provides a set of tools for creating windows, buttons, labels, text fields, and more. Since it's included with most Python installations, you don't need to install any external libraries
'''
#************************************************************************
'''import tkinter as tk

#   Create the main Window
root = tk.Tk()
#   Set the window title
root.title("Simple Wise GUI")
#   Set the window size
root.geometry("300x200")

#************************************************************************

#   Adding Wdget to the GUI
#   Create and Add a label to the main window
label = tk.Label(root, text='Welcome to Wise GUI..!')
label.pack() # Pack adds the widget to the window

#************************************************************************

def on_button_click():
    print('Button Clicked!')
#   Adding a Button
#   Create and add a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

#************************************************************************

# Adding a Text Entry Field
# Create an Entry widget
entry = tk.Entry(root)
entry.pack()

#************************************************************************

# Function to retrieve text from the entry field
def get_entry_text():
    print(f'Entered Text: {entry.get()}')
# Button to fetch the text from the entry field
fetch_button = tk.Button(root, text="Get Text", command=get_entry_text)
fetch_button.pack()

#************************************************************************

#Start the GUI event Loop
root.mainloop()

#************************************************************************'''

#   Putting it all Together
#   Function to get from entry and update the label

import tkinter as tk

def update_label():
    name = entry.get()
    label.config(text=f'Hello, {name}!')
    
# Create the main window
root = tk.Tk()
root.title('Simple GUI')
root.geometry("400x400")

#    Add a label to the window
label = tk.Label(root, text='Enter your Name : ')
label.pack(pady=10) 

#   Add a text entry widget
entry = tk.Entry(root)
entry.pack(pady=20)

#   Add a button to the window
button = tk.Button(root, text="Submit", command=update_label)
button.pack(pady=20)

#Start the GUI event Loop
root.mainloop()


'''
Practice Questions
1. Create a simple to-do list app where users can add tasks. Each task should appear in a list, and the user should be able to remove tasks once they're completed
2 Create a GUI taht displays a random motivational quote when a user clicks a 'Generate Quuote" button
3. Build a simple GUI app that converts temperatures between Celsius and Fahrenheit. The user should input a temperature, and the program should convert it to the other unit when a button is clicked

'''