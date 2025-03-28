import tkinter as tk
from tkinter import ttk
import time
import threading
import socket
import pygame

# Initialize Tkinter window
root = tk.Tk()
root.geometry("600x400")
root.title("Chat App")

# Variables
ip_var = tk.StringVar()
messg_var = tk.StringVar()
user_var = tk.StringVar()
client = None
user = None

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("arabesque.mp3")
    pygame.mixer.music.play(-1)  # Loop indefinitely
    
    # Get the song duration
    time.sleep(1)  # Small delay to ensure pygame initializes properly
    global song_length
    song_length = pygame.mixer.Sound("arabesque.mp3").get_length()
    
    # Set progress bar maximum value
    progress_bar["maximum"] = song_length

    # Start updating the progress bar
    update_progress()

def update_progress():
    """ Updates the progress bar every 500ms based on the song position """
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000  # Convert to seconds
        progress_var.set(current_time)
        root.after(500, update_progress)

def socket_connect(server_ip, user):
    """ Connect to the chat server """
    global client
    server_port = 8080
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    client.send(f"{user} has joined the chat!".encode('utf-8'))
    print("Connected to server. Type 'quit' to leave the chat.")
    return client

# Switch from IP entry to chat
def enable_chat():
    global user, client
    ip = ip_var.get()
    user = user_var.get()
    if validate_ip(ip, user):
        client = socket_connect(ip, user)
        # Hide IP entry widgets
        ip_label.grid_forget()
        ip_entry.grid_forget()
        username_label.grid_forget()
        username_entry.grid_forget()
        connect.grid_forget()
        ip_error_label.grid_forget()
        # Show chat widgets
        show_chat_widgets()
        thread = threading.Thread(target=receive_messages, daemon=True)
        thread.start()
    else:
        ip_error_label.config(text="Empty username! Please try again.")
        ip_error_label.grid(row=3, column=1)

# Function to check if username is blank
def validate_ip(ip, user):
    return user.strip() != ""

def receive_messages():
    """ Receive messages from the server """
    global client
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                root.after(0, update_display, message)
        except:
            root.after(0, update_display, "[ERROR] Disconnected from server.")
            if client:
                client.close()
            break

def update_display(message):
    """ Display received messages in the chat window """
    chat_display.insert(tk.END, f"{time.ctime()} --- {message}\n")
    chat_display.see(tk.END)  # Auto-scroll to the bottom

def send_message():
    """ Send a message to the chat server """
    global client, user
    messg = messg_var.get().strip()
    if messg:
        try:
            client.send(f"{user}: {messg}".encode('utf-8'))
            update_display(f"You: {messg}")
            messg_var.set("")  # Clear input field
        except:
            update_display("[ERROR] Unable to send message.")

def show_chat_widgets():
    """ Show chat interface widgets """
    chat_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    messg_label.grid(row=1, column=0)
    messg_entry.grid(row=1, column=1)
    messg_entry.bind('<Return>', lambda event: send_message())
    sub_btn.grid(row=1, column=2)
    progress_bar.grid(row=2, column=1, pady=10)  # Correctly place the progress bar in the grid

# IP Entry Section
ip_label = tk.Label(root, text="Enter Server IP:", font=("calibre", 12, "bold"))
ip_label.grid(row=0, column=0, pady=10, padx=10)

ip_entry = tk.Entry(root, textvariable=ip_var, font=("calibre", 12), width=30)
ip_entry.grid(row=0, column=1, pady=10, padx=10)

username_label = tk.Label(root, text="Enter Username:", font=("calibre", 12, "bold"))
username_label.grid(row=1, column=0, pady=0, padx=0)

username_entry = tk.Entry(root, textvariable=user_var, font=("calibre", 12), width=30)
username_entry.grid(row=1, column=1, pady=0, padx=0)

connect = tk.Button(root, text="Connect", command=enable_chat)
connect.grid(row=2, column=1, pady=10, padx=10)

root.bind('<Return>', lambda event: enable_chat() if connect.winfo_ismapped() else None)

ip_error_label = tk.Label(root, text="", font=("calibre", 10), fg="red")

# Chat Section
chat_display = tk.Text(root, wrap=tk.WORD, height=20, state=tk.NORMAL)

messg_label = tk.Label(root, text='Send Message', font=('calibre', 10, 'bold'))

messg_entry = tk.Entry(root, textvariable=messg_var, font=('calibre', 10, 'normal'), width=50)

sub_btn = tk.Button(root, text='Send', command=send_message)

# Progress Bar UI
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, length=300, mode="determinate")

# Start the music in a separate thread
threading.Thread(target=play_music, daemon=True).start()

# Main event loop
root.mainloop()

