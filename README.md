# 📲 WhatsApp Messages Automator

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)](https://docs.python.org/3/library/tkinter.html)
[![PyWhatKit](https://img.shields.io/badge/Library-pywhatkit-green)](https://pypi.org/project/pywhatkit/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)

A simple and user-friendly Python desktop application to **schedule and instantly send WhatsApp messages**. Built using **Tkinter** for the interface and **pywhatkit** under the hood, this tool automates WhatsApp messaging right from your desktop with just a few clicks.

---

## 🚀 Features

- ✅ Easy-to-use GUI (no command-line needed)
- ✅ Schedule messages with time (hour and minute)
- ✅ Input validation for phone numbers and message content
- ✅ Uses your default browser & WhatsApp Web to send messages
- ✅ Instant message sending for quick testing

---

## 🛠️ Tech Stack

- **Python 3.7+**
- **Tkinter** – for the graphical user interface
- **PyWhatKit** – to interact with WhatsApp Web

---

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/momina02/WhatsApp-Message-Automator.git
   cd automating-whatsapp-messages
   ```

2. **Install required packages**  
   ```bash
   pip install pywhatkit
   ```

---

## 🧠 How It Works

- Enter a phone number (with country code, e.g., `+92xxxxxxxxxx`)
- Type your message
- Enter the **hour** and **minute** (24-hour format)
- Click **"Schedule Message"**
- WhatsApp Web will open automatically and send the message at the scheduled time!

> 💡 Tip: For instant sending (for testing), the app uses `sendwhatmsg_instantly()` from pywhatkit.

---

## 📸 GUI Preview

<p align="center">
  <img src="assets/1.png" alt="App Screenshot" width="50%" />
</p>

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

Contributions, issues, and suggestions are welcome!  
Feel free to fork the repository and open a pull request.

---

Made with 💚 by a Python enthusiast automating everyday tasks.
