import pyperclip
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from art import *

def generate_ascii():
    input_text = input_text_area.get("1.0", END).strip()
    ascii_art = text2art(input_text, font='Doom')
    output_text_area.delete("1.0", END)
    output_text_area.insert(END, ascii_art)

def copy_ascii():
    ascii_text = output_text_area.get("1.0", END)
    pyperclip.copy(ascii_text)

# Create the GUI
root = Tk()
root.title("ASCII Art Converter")

# Input text area
input_label = Label(root, text="Enter text:")
input_label.pack()
input_text_area = ScrolledText(root, height=5)
input_text_area.pack()

# Generate button
generate_button = Button(root, text="Generate ASCII Art", command=generate_ascii)
generate_button.pack()

# Output text area
output_label = Label(root, text="ASCII Art:")
output_label.pack()
output_text_area = ScrolledText(root, height=10)
output_text_area.pack()

# Copy button
copy_button = Button(root, text="Copy ASCII Art", command=copy_ascii)
copy_button.pack()

root.mainloop()
