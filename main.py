import math
import tkinter as tk
from tkinter import messagebox


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_keys():
    p = int(p_entry.get())
    q = int(q_entry.get())
    n = p * q
    phi = (p - 1) * (q - 1)
    e = int(e_entry.get())
    while math.gcd(e, phi) != 1:
        e = int(input("Введіть відкритий ключ e->"))
    d = mod_inverse(e, phi)
    return n, e, d


def encrypt_button_click():
    try:
        n, e, d = generate_keys()
        word = message_entry.get()
        message = [ord(char) for char in word]
        ciphertext = [encrypt(char, n, e) for char in message]
        result_label.config(text="Шифр: " + ' '.join(map(str, ciphertext)))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def decrypt_button_click():
    try:
        n, e, d = generate_keys()
        ciphertext = [int(char) for char in ciphertext_entry.get().split()]
        plaintext = ''.join([chr(decrypt(char, n, d)) for char in ciphertext])
        result_label.config(text="Розшифроване повідомлення: " + plaintext)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def encrypt(message, n, e):
    return pow(message, e, n)


def decrypt(ciphertext, n, d):
    return pow(ciphertext, d, n)


root = tk.Tk()
root.title("RSA Encryption")

tk.Label(root, text="Просте число p:").pack()
p_entry = tk.Entry(root)
p_entry.pack()

tk.Label(root, text="Просте число q:").pack()
q_entry = tk.Entry(root)
q_entry.pack()

tk.Label(root, text="Відкритий ключ e:").pack()
e_entry = tk.Entry(root)
e_entry.pack()

tk.Label(root, text="Слово для шифрування:").pack()
message_entry = tk.Entry(root)
message_entry.pack()

tk.Label(root, text="Зашифроване повідомлення:").pack()
ciphertext_entry = tk.Entry(root)
ciphertext_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()

encrypt_button = tk.Button(root, text="Зашифрувати", command=encrypt_button_click)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Розшифрувати", command=decrypt_button_click)
decrypt_button.pack()

root.mainloop()
