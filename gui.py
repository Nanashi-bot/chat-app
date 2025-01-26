import tkinter as tk
import time

root = tk.Tk()

# Setting the window size
root.geometry("600x400")


# Function to update the display with the new message
def updatedisplay():
    messg = messg_var.get()
    if messg!="":
        print("Message is: ", messg)
        chat_display.insert(tk.END, f"{time.ctime()} --- {messg}\n")
        chat_display.see(tk.END)  # Auto-scroll to the bottom
        messg_var.set("")  # Clear the input field


# Chat display area
chat_display = tk.Text(root, wrap=tk.WORD, height=20, state=tk.NORMAL)
chat_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Entry field for message input
messg_var = tk.StringVar()
messg_label = tk.Label(root, text='Send Message', font=('calibre', 10, 'bold'))
messg_label.grid(row=1, column=0)
messg_entry = tk.Entry(root, textvariable=messg_var, font=('calibre', 10, 'normal'), width=50)
messg_entry.grid(row=1, column=1)
messg_entry.bind('<Return>', lambda event: updatedisplay())

# Send button
sub_btn = tk.Button(root, text='Send', command=updatedisplay)
sub_btn.grid(row=1, column=2)

# Main event loop
root.mainloop()
