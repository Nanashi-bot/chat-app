# TCP Chat App
This repository contains a simple server-client communication setup. The server is implemented in Python using `server.py`, while the client is available in multiple formats:
- A Python script (`client.py`) for command-line interaction.
- A GUI client for Linux (`./client`), implemented in Python via `gui.py`.
- A compiled executable for Windows (`windowsclient.exe`).

## File Overview
- `server.py`: The server-side Python script that listens for incoming connections on port 8080. It processes requests from clients and sends responses back.
- `client.py`: A command-line Python script that allows users to connect to the server by providing the server's IP address.
- `windowsclient.exe`: A compiled executable for Windows users who prefer a GUI client.
- `./client`: The Linux GUI client, runnable from the terminal.
- `gui.py`: The Python script that powers the Linux GUI client.

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

The server will now be running and listening on `localhost:8080` by default. You can modify the script to use a different IP or port if necessary.

**Note:** If you are connecting over the internet, make sure port 8080 is exposed in your firewall settings. If you are hosting the server on an Amazon EC2 instance, ensure that:
- The EC2 instance has a public IP address.
- Port 8080 is allowed in the EC2 security group settings.
- Any firewall rules on the instance permit inbound traffic on port 8080.

### 2. Running the Client

There are multiple ways to run the client: via the command-line script, the Windows GUI, or the Linux GUI.

#### Option 1: Using `client.py` (Command-Line)

1. Ensure Python is installed on your machine.
2. Open a terminal/command prompt and navigate to the repository directory.
3. Run the client script:

```
python client.py
```

4. The client will prompt you to enter the server's IP address. Enter the server's IP (e.g., `127.0.0.1` for localhost or the EC2 instance's public IP if hosting on AWS).
5. The client will connect to the server and interact with it.

#### Option 2: Using `windowsclient.exe` (Windows GUI)

1. Double-click on `windowsclient.exe` to launch the client.
2. The GUI will prompt you for the server's IP address.
3. Enter the server's IP (e.g., `127.0.0.1` for localhost or the EC2 instance's public IP), and the client will connect to the server.

#### Option 3: Using `./client` (Linux GUI)

1. Open a terminal in the repository directory.
2. Make sure the file has execution permissions:

```
chmod +x ./client
```

3. Run the GUI client:

```
./client
```

4. The GUI will prompt you for the server's IP address.
5. Enter the server's IP (e.g., `127.0.0.1` for localhost or the EC2 instance's public IP), and the client will connect to the server.

### 3. Modifying the Server IP/Port (Optional)

If you want to change the server's IP or port, modify the necessary lines in `client.py`, `server.py`, or the GUI clients as needed.

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

- Python 3.x for `server.py` and `client.py`.
- Windows users can use `windowsclient.exe` without needing Python.
- Linux users can use the GUI client `./client`.

## Troubleshooting

- Ensure that the server is running before attempting to connect with the client.
- Verify that there are no firewall or network restrictions blocking communication on port 8080.
- If hosting on an EC2 instance:
  - Ensure that the security group allows inbound traffic on port 8080.
  - Check if the EC2 instance has a public IP.
  - Confirm that the instance’s firewall settings permit external connections.


