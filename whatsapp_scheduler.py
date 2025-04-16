import pywhatkit
import tkinter as tk
from tkinter import messagebox

def schedule_message():
    phone = phone_entry.get()
    msg = message_entry.get()
    hour = hour_entry.get()
    minute = minute_entry.get()

    if not phone.startswith("+"):
        messagebox.showerror("Error", "Phone number must include country code (e.g., +92)")
        return
    if not msg:
        messagebox.showerror("Error", "Message cannot be empty")
        return
    if not hour.isdigit() or not minute.isdigit():
        messagebox.showerror("Error", "Hour and minute must be numbers")
        return

    hour = int(hour)
    minute = int(minute)

    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        messagebox.showerror("Error", "Invalid time. Hour (0-23), Minute (0-59)")
        return

    try:
        pywhatkit.sendwhatmsg_instantly(phone, msg, wait_time=90)
        messagebox.showinfo("Success", f"Message sent to {phone}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send message: {str(e)}")


root = tk.Tk()
root.title("WhatsApp Message Scheduler")
root.geometry("400x300")

tk.Label(root, text="Phone Number (with country code, e.g., +92xxxxxxxxxx):").pack(pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()

tk.Label(root, text="Message:").pack(pady=5)
message_entry = tk.Entry(root, width=30)
message_entry.pack()

tk.Label(root, text="Hour (24-hour format, 0-23):").pack(pady=5)
hour_entry = tk.Entry(root, width=10)
hour_entry.pack()

tk.Label(root, text="Minute (0-59):").pack(pady=5)
minute_entry = tk.Entry(root, width=10)
minute_entry.pack()

schedule_button = tk.Button(root, text="Schedule Message", command=schedule_message)
schedule_button.pack(pady=20)

root.mainloop()

 
 
 
