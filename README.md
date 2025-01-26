# TCP Chat App
This repository contains a simple server-client communication setup. The server is implemented in Python using server.py, while the client is available both as a Python script (client.py) and a compiled executable (client.exe).

## File Overview 
server.py: The server-side Python script that listens for incoming connections on port 8080. It processes requests from clients and sends responses back.

client.py: A Python script that allows users to connect to the server by providing the server's IP address.

client.exe: An executable file of client.py for users who don't have Python installed.

## Setup Instructions
### 1. Running the Server

To start the server, follow these steps:

1. Install Python 3.x from [here](https://www.python.org/downloads/) (if not already installed).
2. Clone or download this repository.
3. Open a terminal/command prompt in the repository's directory.
4. Run the server script:

```
python server.py
```

The server will now be running and listening on localhost:8080 by default. You can modify the server script to use a different IP or port if necessary.

### 2. Running the Client

There are two ways to run the client: via the Python script or using the executable.

Option 1: Using client.py (Python Script)

1. Ensure Python is installed on your machine.
2. Open a terminal/command prompt and navigate to the repository directory.
3. Run the client script:
```
python client.py
```

4. The client will prompt you to enter the server's IP address. Enter the server's IP (e.g., 127.0.0.1 for localhost).
5. The client will connect to the server and interact with it.

Option 2: Using client.exe

1. Simply double-click on client.exe to launch the client.
2. The client will prompt you for the server's IP address.
3. Enter the server's IP (e.g., 127.0.0.1 for localhost) and the client will connect to the server.

3. Modifying the Server IP/Port (Optional)

If you want to change the server's or port, modify the necessary lines in client.py and server.py


## Example Usage

1. Start the server:

```
python server.py
```

2. Run the client:

```
python client.py
```

3. Enter the server's IP address when prompted.

## Requirements

Python 3.x for server.py and client.py.

## Troubleshooting;

Ensure that the server is running before attempting to connect with the client.
Verify that there are no firewall or network restrictions blocking communication on port 8080.
