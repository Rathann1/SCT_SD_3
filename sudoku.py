import tkinter as tk
from tkinter import messagebox


# ---------------- SUDOKU SOLVER ---------------- #

def is_valid(board, row, col, num):

    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False

    return True


# ---------------- GUI FUNCTIONS ---------------- #

def solve():

    board = []

    for i in range(9):
        row = []

        for j in range(9):
            value = entries[i][j].get()

            if value == "":
                row.append(0)
            elif value.isdigit() and 1 <= int(value) <= 9:
                row.append(int(value))
            else:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter numbers from 1 to 9 only."
                )
                return

        board.append(row)

    if solve_sudoku(board):

        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, board[i][j])

    else:
        messagebox.showinfo(
            "No Solution",
            "This Sudoku puzzle has no solution."
        )


def clear_board():

    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)


def load_example():

    example = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    clear_board()

    for i in range(9):
        for j in range(9):
            if example[i][j] != 0:
                entries[i][j].insert(0, example[i][j])


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("500x650")
root.resizable(False, False)

title = tk.Label(
    root,
    text="SUDOKU SOLVER",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)


# Sudoku grid
grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)

entries = []

for i in range(9):

    row_entries = []

    for j in range(9):

        entry = tk.Entry(
            grid_frame,
            width=3,
            font=("Arial", 18),
            justify="center"
        )

        entry.grid(
            row=i,
            column=j,
            padx=2,
            pady=2,
            ipady=5
        )

        row_entries.append(entry)

    entries.append(row_entries)


# Buttons
solve_button = tk.Button(
    root,
    text="SOLVE",
    font=("Arial", 12, "bold"),
    width=15,
    height=2,
    command=solve
)
solve_button.pack(pady=8)


clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 11),
    width=15,
    command=clear_board
)
clear_button.pack(pady=5)


# --------- CHANGED: LOAD EXAMPLE BUTTON ---------

example_button = tk.Button(
    root,
    text="LOAD EXAMPLE",
    font=("Arial", 11, "bold"),
    width=20,
    height=2,
    command=load_example
)
example_button.pack(pady=8)


root.mainloop()