# import library
from tkinter import *
from tkinter import messagebox
import math

# main function
def main():
    # Calculation function
    def calculate():
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, END)
            entry.insert(END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Button click function
    def button_click(number):
        current = entry.get()
        entry.delete(0, END)
        entry.insert(END, current + str(number))

    # Clear function
    def clear():
        entry.delete(0, END)

    Main = Tk()
    Main.title("Calculator")
    Main.geometry("340x300")
    Main.resizable(False, False)
    Main.config(bg="black")

    # Entry field for the calculator
    entry = Entry(Main, width=30, font=("Arial", 14))
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # buttons (numbers, +, -, *, /, =, clear, exit)
    btn1 = Button(Main, text="1", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"), command=lambda: button_click(1))
    btn1.grid(row=1, column=0, padx=5, pady=5)
    btn2 = Button(Main, text="2", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"), command=lambda: button_click(2))
    btn2.grid(row=1, column=1, padx=5, pady=5)
    btn3 = Button(Main, text="3", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"), command=lambda: button_click(3))
    btn3.grid(row=1, column=2, padx=5, pady=5)
    btn4 = Button(Main, text="4", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"), command=lambda: button_click(4))
    btn4.grid(row=2, column=0, padx=5, pady=5)
    btn5 = Button(Main, text="5", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"), command=lambda: button_click(5))
    btn5.grid(row=2, column=1, padx=5, pady=5)
    btn6 = Button(Main, text="6", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"), command=lambda: button_click(6))
    btn6.grid(row=2, column=2, padx=5, pady=5)
    btn7 = Button(Main, text="7", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"), command=lambda: button_click(7))
    btn7.grid(row=3, column=0, padx=5, pady=5)
    btn8 = Button(Main, text="8", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"), command=lambda: button_click(8))
    btn8.grid(row=3, column=1, padx=5, pady=5)
    btn9 = Button(Main, text="9", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"),
                  command=lambda: button_click(9))
    btn9.grid(row=3, column=2, padx=5, pady=5)
    btn0 = Button(Main, text="0", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"),
                  command=lambda: button_click(0))
    btn0.grid(row=4, column=0, padx=5, pady=5)
    btnPlus = Button(Main, text="+", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"),
                     command=lambda: button_click("+"))
    btnPlus.grid(row=1, column=3, padx=5, pady=5)
    btnMinus = Button(Main, text="-", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"),
                      command=lambda: button_click("-"))
    btnMinus.grid(row=2, column=3, padx=5, pady=5)
    btnMultiply = Button(Main, text="*", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"),
                         command=lambda: button_click("*"))
    btnMultiply.grid(row=3, column=3, padx=5, pady=5)
    btnDivide = Button(Main, text="/", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"),
                       command=lambda: button_click("/"))
    btnDivide.grid(row=4, column=3, padx=5, pady=5)
    btnEqual = Button(Main, text="=", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"),
                      command=calculate)
    btnEqual.grid(row=4, column=2, padx=5, pady=5)
    btnClear = Button(Main, text="Clear", width=5, height=2, bg="black", fg="gray", font=("Arial", 10, "bold"),
                      command=clear)
    btnClear.grid(row=4, column=1, padx=5, pady=5)

    # put buttons on the screen

    # loop
    Main.mainloop()


# call main function
if __name__ == "__main__":
    main()
