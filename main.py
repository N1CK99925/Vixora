import tkinter as tk
import dialogue as d
from tkinter import PhotoImage
import Data as data




















































# Create main window
root = tk.Tk()
root.title("Vexora")
root.geometry("400x600")  # Set window size
blank_icon = PhotoImage(width=1, height=1)  # Provide the path to your icon file
root.iconphoto(False, blank_icon)
#Will change the icon later
# Create text box for the chat display
chat_display = tk.Text(root, wrap=tk.WORD, height=20, width=50, state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)


user_input = tk.Entry(root, width=50)
user_input.pack(padx=10, pady=10)

# Function to handle the user's message
def send_message(event = None):
    user_message = user_input.get()
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_message + "\n")
    chat_display.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)  # Clear input field

    # Simulate AI response (replace this with actual AI logic)
    bot_response = "AI: " + "This is a response for: " + user_message + "\n"
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, bot_response)
    chat_display.config(state=tk.DISABLED)

# Button to send the message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

user_input.bind("<Return>", send_message)


# Run the application
root.mainloop()

