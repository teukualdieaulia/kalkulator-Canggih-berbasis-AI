import tkinter as tk

def tekan_tombol(angka):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(angka))

def tekan_operator(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + operator)

def hasil():
    entry.delete(0, tk.END)
    entry.insert(0, "Hello World")

def hapus():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Kalkulator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, width=25, font=('Arial', 20), borderwidth=2, relief="ridge", justify='right')
entry.pack(pady=20)

tombol_frame = tk.Frame(root)
tombol_frame.pack()

tombol_list = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for baris in tombol_list:
    row = tk.Frame(tombol_frame)
    row.pack(expand=True, fill='both')
    for item in baris:
        if item == '=':
            tombol = tk.Button(row, text=item, width=6, height=2, font=('Arial', 16),
                               command=hasil)
        elif item in '+-*/':
            tombol = tk.Button(row, text=item, width=6, height=2, font=('Arial', 16),
                               command=lambda op=item: tekan_operator(op))
        else:
            tombol = tk.Button(row, text=item, width=6, height=2, font=('Arial', 16),
                               command=lambda num=item: tekan_tombol(num))
        tombol.pack(side='left', expand=True, fill='both')

clear_btn = tk.Button(root, text="C", width=10, height=2, font=('Arial', 16), bg="red", fg="white", command=hapus)
clear_btn.pack(pady=10)

root.mainloop()