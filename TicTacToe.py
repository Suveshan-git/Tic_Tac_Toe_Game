# TIC-TAC-TOE GAME

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe Game")

clicked = True
moves = 0
win = False


def check_tie():
    if moves == 9:
        messagebox.showinfo("TIC TAC TOE", "It's a Tie!!!")
        exit()
    else:
        pass


def check_winner():
    global win

    # Check if X is the Winner
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "X is the Winner!!!")
        exit()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "X is the Winner!!!")
        exit()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "X is the Winner!!!")
        exit()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "X is the Winner!!!")
        exit()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "X is the Winner!!!")
        exit()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "X is the Winner!!!")
        exit()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "X is the Winner!!!")
        exit()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "X is the Winner!!!")
        exit()

    # Check if O is the Winner
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "O is the Winner!!!")
        exit()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "O is the Winner!!!")
        exit()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "O is the Winner!!!")
        exit()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "O is the Winner!!!")
        exit()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "O is the Winner!!!")
        exit()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "O is the Winner!!!")
        exit()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "O is the Winner!!!")
        exit()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        win = True
        messagebox.showinfo("TIC TAC TOE", "O is the Winner!!!")
        exit()


def button_click(button):
    global clicked, moves

    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        moves += 1
        check_tie()
        check_winner()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        moves += 1
        check_tie()
        check_winner()
    else:
        messagebox.showerror("Tic Tac Toe", "Box has already been selected!")


# Create the grid using buttons
b1 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b1))
b2 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b2))
b3 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b3))

b4 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b4))
b5 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b5))
b6 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b6))

b7 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b7))
b8 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b8))
b9 = Button(root, text=" ", font=("New Times Roman", 20), height=2, width=4, bg="SystemButtonFace", command=lambda: button_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()
