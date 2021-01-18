import base64
import tkinter as tk
from tkinter.ttk import *


def Encoded():

    f = open("file.txt", "r").read()
    messageBytes = f.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')
    Message = base64Message

    f = open("file.txt", "w")
    f.write(Message)
    f.close()

    Output.delete('1.0', "end")
    Output.insert('1.0', "")
    Output.insert(tk.END, Message)

    print("The Encoded Message Is", end='\n')
    print(Message)


def Decoded():

    f = open("file.txt", "r").read()
    base64Bytes = f.encode('ascii')
    messageBytes = base64.b64decode(base64Bytes)
    Message = messageBytes.decode('ascii')

    f = open("file.txt", "w")
    f.write(Message)
    f.close()

    Output.delete('1.0', "end")
    Output.insert('1.0', "")
    Output.insert(tk.END, Message)

    print("The Decoded Message Is", end='\n')
    print(Message)


def quit():
    parent.destroy()


parent = tk.Tk()

parent.title('Base64 Encode-Decode')
parent.iconbitmap('icon.ico')
parent.geometry("400x400")

frame = tk.Frame(parent)
frame.pack()

l = tk.Label(parent, text=" Select Your Choice ", font=("Arial Bold", 20))
# l.grid(column=0, row=0)

Output = tk.Text(parent, height=18,
                 width=40,
                 bg="lavender")

l.pack()
Output.pack()


encode_button = tk.Button(frame,
                          text=" Encode ",
                          font=("Arial Bold", 10),
                          fg='white',
                          bg="green",
                          command=Encoded
                          )

encode_button.pack(side=tk.LEFT)

decode_button = tk.Button(frame,
                          text=" Decode ",
                          font=("Arial Bold", 10),
                          fg='white',
                          bg="blue",
                          command=Decoded)
decode_button.pack(side=tk.RIGHT)

quit_button = tk.Button(parent,
                        text=" Commit Sudoku ",
                        font=("Arial Bold", 10),
                        fg='white',
                        bg="red",
                        command=quit)
quit_button.pack(side=tk.TOP)


parent.mainloop()
