#### **LAN Multiplayer Functionality**

### 1. Enable LAN Communication
Ensure both devices can communicate over the same LAN. You can use sockets for TCP or UDP communication. Python’s socket module is a good choice.

### 2. Host Creates a Room (User1)
Enable the hotspot: User1 creates a personal hotspot.
Run a socket server: User1 starts a server that listens for incoming connections from User2.
Share connection details: The server broadcasts its availability (e.g., IP and port).
### 3. Client Joins the Room (User2)
Connect to the host's hotspot: User2 connects to the same Wi-Fi network.
Find the host's server: Either:
Enter the host's IP address manually, or
Use a UDP broadcast to discover the server automatically




#### Future Enhancements
### Automatic Discovery: 
Use UDP broadcasting for automatic server discovery instead of manually entering the IP address.

### Multiple Clients: 
Modify the server to handle multiple clients using threading or asyncio.

### User Interface: 
Add a graphical interface using libraries like Tkinter or PyQt for a more user-friendly experience.

### Data Validation: 
Handle edge cases, such as invalid input or disconnected clients.

### Encryption: 
If privacy is important, encrypt data using SSL or Python’s cryptography module.


________________________________________


#### **Setup for Testing**

To test the provided server and client code, You will need two devices or at least two terminals on the same computer. 
Here's a step-by-step guide:

### 1. Ensure Network Connectivity
- **If testing on two physical devices:**
Start a personal hotspot on one device (User1).
Connect the second device (User2) to this hotspot.

- **If testing on the same device:**
Use localhost (127.0.0.1) as the host IP address for both server and client.



### 2. Run the Server
```python
python server.py
```
### 3. Run the Client
```python 
python client.py
```
### 4. If prompted, enter the server's IP address:
- **For testing on the same device**: Enter 127.0.0.1.
- **For different devices**: Enter the IP address of the server device. (Find this by running ipconfig on Windows or ifconfig on Linux/Mac.)


________________________________________


#### **Sample Output**

### Server Terminal:
```plaintext
Server started. Waiting for clients on 0.0.0.0:12345...
Client connected from ('127.0.0.1', 54321)
```
### Client Terminal:
```plaintext
Enter the host's IP address: 127.0.0.1
Connected to the server!
Server: Welcome to Guess the Number! Guess a number between 1 and 100.
Enter your guess: 50
Server: Too high!
Enter your guess: 25
Server: Too low!
Enter your guess: 42
Server: Correct! You guessed the number.
```