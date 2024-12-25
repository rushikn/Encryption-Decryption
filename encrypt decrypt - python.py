from tkinter import *
from tkinter import messagebox
import base64

def encrypt_message():
    message = message_entry.get("1.0", "end-1c")
    secret_key = secret_key_entry.get()
    if message == "" or secret_key == "":
        messagebox.showerror("Error", "Please enter a message and secret key.")
        return
    encrypted_message = base64.b64encode((message + secret_key).encode("utf-8")).decode("utf-8")
    encrypted_result_text.config(state=NORMAL)
    encrypted_result_text.delete("1.0", "end")
    encrypted_result_text.insert("1.0", encrypted_message)
    encrypted_result_text.config(state=DISABLED)

def decrypt_message():
    encrypted_message = encrypted_result_text.get("1.0", "end-1c")
    secret_key = secret_key_entry.get()
    if encrypted_message == "" or secret_key == "":
        messagebox.showerror("Error", "Please enter a message and secret key.")
        return
    try:
        decrypted_message = base64.b64decode(encrypted_message.encode("utf-8")).decode("utf-8")
        if decrypted_message.endswith(secret_key):
            original_message = decrypted_message[:-len(secret_key)]
            messagebox.showinfo("Decrypted Message", f"Original Message: {original_message}")
        else:
            messagebox.showerror("Error", "Incorrect secret key. Decryption failed.")
    except Exception:
        messagebox.showerror("Error", "Invalid encrypted message. Decryption failed.")

def reset_fields():
    message_entry.delete("1.0", "end")
    secret_key_entry.delete(0, "end")
    encrypted_result_text.config(state=NORMAL)
    encrypted_result_text.delete("1.0", "end")
    encrypted_result_text.config(state=DISABLED)

def main_screen():
    screen = Tk()
    screen.geometry("500x550")
    screen.title("Message Encryption and Decryption Tool")
    screen.config(bg="#f0f0f0")

    title_label = Label(screen, text="Message Encryption & Decryption", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#00796b")
    title_label.pack(pady=20)

    instruction_label = Label(screen, text="Enter your message and secret key below:", font=("Helvetica", 12), bg="#f0f0f0")
    instruction_label.pack(pady=10)

    global message_entry
    message_entry = Text(screen, width=45, height=6, font=("Helvetica", 12), wrap=WORD)
    message_entry.pack(pady=10)

    secret_key_label = Label(screen, text="Enter Secret Key for Encryption/Decryption:", font=("Helvetica", 12), bg="#f0f0f0")
    secret_key_label.pack(pady=10)

    global secret_key_entry
    secret_key_entry = Entry(screen, font=("Helvetica", 12), show="*")
    secret_key_entry.pack(pady=10)

    button_frame = Frame(screen, bg="#f0f0f0")
    button_frame.pack(pady=20)

    encrypt_button = Button(button_frame, text="Encrypt", font=("Helvetica", 12), bg="#388e3c", fg="white", width=15, height=2, command=encrypt_message)
    encrypt_button.grid(row=0, column=0, padx=10)

    decrypt_button = Button(button_frame, text="Decrypt", font=("Helvetica", 12), bg="#d32f2f", fg="white", width=15, height=2, command=decrypt_message)
    decrypt_button.grid(row=0, column=1, padx=10)

    reset_button = Button(button_frame, text="Reset", font=("Helvetica", 12), bg="#f57c00", fg="white", width=15, height=2, command=reset_fields)
    reset_button.grid(row=1, column=0, columnspan=2, pady=10)

    global encrypted_result_text
    encrypted_result_text = Text(screen, height=4, width=45, font=("Helvetica", 12), wrap=WORD, state=DISABLED)
    encrypted_result_text.pack(pady=10)

    screen.mainloop()

main_screen()
