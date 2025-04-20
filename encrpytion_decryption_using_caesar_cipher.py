import tkinter as tk
from tkinter import ttk

# Caesar Cipher Logic
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Button Functions
def encrypt_text():
    message = message_entry.get()
    try:
        shift = int(shift_entry.get())
        result = caesar_encrypt(message, shift)
        result_label.config(text=f"Encrypted: {result}")
    except ValueError:
        result_label.config(text="Shift must be an integer!")

def decrypt_text():
    message = message_entry.get()
    try:
        shift = int(shift_entry.get())
        result = caesar_decrypt(message, shift)
        result_label.config(text=f"Decrypted: {result}")
    except ValueError:
        result_label.config(text="Shift must be an integer!")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher - Encrypt & Decrypt")
root.geometry("400x300")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure("TButton", padding=6, font=('Arial', 10))
style.configure("TLabel", font=('Arial', 11))
style.configure("TEntry", font=('Arial', 11))

# Widgets
ttk.Label(root, text="Enter Message:").pack(pady=10)
message_entry = ttk.Entry(root, width=40)
message_entry.pack()

ttk.Label(root, text="Enter Shift Value:").pack(pady=10)
shift_entry = ttk.Entry(root, width=10)
shift_entry.pack()

ttk.Button(root, text="Encrypt", command=encrypt_text).pack(pady=10)
ttk.Button(root, text="Decrypt", command=decrypt_text).pack()

result_label = ttk.Label(root, text="", foreground="blue", wraplength=350)
result_label.pack(pady=20)

root.mainloop()
