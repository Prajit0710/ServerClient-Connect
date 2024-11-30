import socket

def start_client():
    host = input("Enter the host's IP address: ")  # Manually enter the host's IP
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server!")

    while True:
        message = client_socket.recv(1024).decode()
        print("Server:", message)

        if "Correct!" in message:
            break

        guess = input("Enter your guess: ")
        client_socket.send(guess.encode())

    client_socket.close()

start_client()
