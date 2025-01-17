# import socket
# import time

# # Setup TCP socket client
# HOST = "0.0.0.0"  # This will be the service name of app2 in Kubernetes
# PORT = 5001  # Port to connect to

# # Create a socket object
# client_socket = socket.socket(
#     socket.AF_INET, 
#     socket.SOCK_STREAM
#     )

# try:
#     # Connect to app2 server
#     print(f"Connecting to {HOST} on port {PORT}...")
#     client_socket.connect((HOST, PORT))
#     print("Connected to app2.")

#     # Infinite loop to send messages to app2 and keep receiving responses
#     print("================================ connect with app2 ================================")
#     while True:
#         # Send a message to app2
#         client_socket.sendall("Hello from app1! Let's keep talking.".encode())
#         print("SENDING")

#         # Receive the response from app2
#         response = client_socket.recv(1024)
#         if not response:
#             print("No response received, server may have closed the connection.")
#             break  # If no data is received, break the loop (connection might have been closed)
#         print(f"Received from app2: {response.decode()}")

#         # Optionally, add a delay to simulate a more natural chat (if needed)
#         # time.sleep(10)  # 2-second delay before sending the next message

# except socket.error as e:
#     print(f"Socket error occurred: {e}")
# except Exception as e:
#     print(f"Unexpected error occurred: {e}")
# finally:
#     print("Closing the client connection.")
#     client_socket.close()



import socket
import time
from random import randint

# Setup TCP socket client
HOST = 'app2'  # This will be the service name of app2 in Kubernetes
PORT = 5001  # Port to connect to

# Create a socket object
client_socket = socket.socket(
    socket.AF_INET, 
    socket.SOCK_STREAM
    )

try:
    # Connect to app2 server
    print(f"Connecting to {HOST} on port {PORT}...")
    client_socket.connect((HOST, PORT))
    print("Connected to app2.")

    # Infinite loop to send messages to app2 and keep receiving responses
    print("================================ connect with app2 ================================")
    while True:
        # Send a message to app2
        # select = 2
        select = randint(1,3)
        if select == 1:
            message = "Hello from app1! Let's keep talking."
        elif select == 2:
            message = "WTF again"
        else:
            message = "WTF"
        client_socket.sendall(message.encode())   # ->
        print("SENDING")

        # Receive the response from app2
        response = client_socket.recv(1024) # <- 
        if not response:
            print("No response received, server may have closed the connection.")
            break  # If no data is received, break the loop (connection might have been closed)
        print(f"Received from app2: {response.decode()}")


except socket.error as e:
    print(f"Socket error occurred: {e}")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
finally:
    print("Closing the client connection.")
    client_socket.close()

