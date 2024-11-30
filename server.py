import socket

def start_server():
    host = '0.0.0.0'  # Listen on all interfaces
    port = 12345      # Choose an unused port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started. Waiting for clients on {host}:{port}...")

    client_socket, addr = server_socket.accept()
    print(f"Client connected from {addr}")

    secret_number = 42  # Example secret number
    client_socket.send(b"Welcome to Guess the Number! Guess a number between 1 and 100.\n")

    while True:
        guess = client_socket.recv(1024).decode().strip()
        if not guess:
            break

        guess = int(guess)
        if guess < secret_number:
            client_socket.send(b"Too low!\n")
        elif guess > secret_number:
            client_socket.send(b"Too high!\n")
        else:
            client_socket.send(b"Correct! You guessed the number.\n")
            break

    client_socket.close()
    server_socket.close()

start_server()
