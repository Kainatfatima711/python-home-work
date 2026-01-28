import tkinter as tk

def calculate_product():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    result_label.config(text="Product: " + str(result))

window = tk.Tk()
window.title("Product Calculator")

tk.Label(window, text="Enter First Number:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter Second Number:").pack()
entry2 = tk.Entry(window)
entry2.pack()

tk.Button(window, text="Calculate Product", command=calculate_product).pack()

result_label = tk.Label(window, text="Product: ")
result_label.pack()

window.mainloop()
