import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Medical AI Chatbot")
root.geometry("400x600")  # Set window size

# Create text box for the chat display
chat_display = tk.Text(root, wrap=tk.WORD, height=20, width=50, state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)

# Create text box for user input
user_input = tk.Entry(root, width=50)
user_input.pack(padx=10, pady=10)

# Function to handle the user's message
def send_message():
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

# Run the application
root.mainloop()

