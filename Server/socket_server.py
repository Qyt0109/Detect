""" TCP Socket API
socket()
.bind()
.listen()
.accept()
.connect()
.connect_ex()
.send()
.recv()
.close()
"""
import socket

class SocketServer():
    def __init__(self, host:str = None, port:int = None, on_connected_callback=None) -> None:
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.on_connected_callback = on_connected_callback

    def start(self, host:str = None, port:int = None):
        if host:
            self.host = host
        if port:
            self.port = port
        if self.host and self.port:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            print(f"Server listening on {self.host}:{self.port}")
        else:
            print("Server host, port not identified")

    def accept_client(self, on_connected_callback=None):
        self.client_socket, addr = self.server_socket.accept()
        print(f"Accepted connection from {addr}")
        if on_connected_callback:
            self.on_connected_callback = on_connected_callback
        if self.on_connected_callback:
            on_connected_callback(self.client_socket, addr)
            print(f"Make a callback, content: client_socket = <object>, addr = {addr}")

    def remove_client(self):
        if self.client_socket:
            self.client_socket.close()
            print("Client disconnected")

    def send(self, data:bytes)->bool:
        if self.client_socket:
            self.client_socket.send(data)
            return True
        return False
    
    def recv(self, buffer_size:int = 1024)->bytes:
        if self.client_socket:
            return self.client_socket.recv(buffer_size)
        return None
    
    def stop(self):
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.client_socket.close()
        print("Server stopped")

class SocketClient():
    def __init__(self, host:str = None, port:int = None) -> None:
        self.host = host
        self.port = port
        self.client_socket = None
    
    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to {self.host}:{self.port}")
    
    def send(self, data:bytes)->bool:
        if self.client_socket:
            self.client_socket.send(data)
    
    def recv(self, buffer_size:int = 1024):
        if self.client_socket:
            return self.client_socket.recv(buffer_size)
        return None
    
    def disconnect(self):
        if self.client_socket:
            self.client_socket.close()
            print("Disconnected")

def handle_on_connected(client_socket, addr):
    print(f"Handled connection from {addr}")

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 65432

    server = SocketServer(HOST, PORT)
    server.start()

    message = input("Server (me): ")
    while message != "ok":
        message = input("Server (me): ")
    server.accept_client()
    while message != "bye":
        server.send(message.encode())
        client_response = server.recv()
        print(f"Server: {client_response}")
        message = input("Server (me): ")
    server.stop()