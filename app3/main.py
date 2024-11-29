
import socket

# Setup a TCP socket server
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5003  # Port to listen on

# Create a socket object
server_socket = socket.socket(
    socket.AF_INET, 
    socket.SOCK_STREAM
    )


try:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on port {PORT}...")

    # Accept incoming connections
    conn, addr = server_socket.accept()        
    print(f"Connected by {addr}")
    print("================================ connect with app1 ================================")

    # Infinite loop to keep server running
    while True:
        data = conn.recv(1024)  # Receive data (max size 1024 bytes)  # <-
        if not data:
            print("No data received, client may have disconnected.")
            break  # Exit the loop if no data is received (client disconnects)
        print(f"Received from app1: {data.decode()}")

        # Respond to app1
        conn.sendall("Hello from app2! Keep chatting! 3333333333333333333".encode())  # ->

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    conn.close()
    print("Connection closed.")
