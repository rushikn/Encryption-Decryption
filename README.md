# 🛡️ Message Encryption and Decryption Tool 🔒

This is a simple Python-based application for encrypting and decrypting messages using AES (Advanced Encryption Standard) encryption. The application is built with a graphical user interface (GUI) using Tkinter. Users can enter a message and a secret key to encrypt the message. The encrypted message is then displayed in a base64-encoded format, and users can also decrypt the message using the correct key.

## 🌟 Features:
- 🔐 **AES Encryption**: Encrypt your messages securely using AES.
- 🔓 **Decryption**: Decrypt messages using the secret key.
- 🔑 **Base64 Encoding**: Encrypted messages are shown in base64 format.
- 🖥️ **GUI Interface**: Simple and easy-to-use graphical interface built with Tkinter.
- ⚠️ **Error Handling**: Error messages are shown if the message or secret key is missing, or if decryption fails.

## ⚙️ Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/rushikn/Encryption-Decryption.git
   
2. Install required libraries: This application requires the pycryptodome and tkinter libraries. Install them using pip:
bash
**pip install pycryptodome**
## 🚀 Usage:
⚙️ Running the Application:
Open the terminal or command prompt and navigate to the project directory.
Run the main.py file:
**python main.py**
Encrypting a Message:

✍️ Enter a message in the provided text box.
🔑 Enter a secret key (for encryption).
🔒 Click on the "Encrypt" button to encrypt the message. The encrypted message will be displayed in the lower text area.
Decrypting a Message:

📋 Copy the encrypted message from the result area.
🔑 Paste it into the result area if necessary.
🔓 Enter the same secret key you used for encryption.
➡️ Click the "Decrypt" button to reveal the original message.
Resetting Fields:

🔄 Click the "Reset" button to clear the message, secret key, and encrypted message fields.
🖼️ Example Screenshot:
![Screenshot 2024-12-25 193914](https://github.com/user-attachments/assets/29ef78d0-fc2a-4fa9-a493-48699011ec7c)


