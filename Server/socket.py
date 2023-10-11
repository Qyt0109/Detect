import socket
import time

from Backend.Common.image_features import get_image_type, bytes_to_image

class SocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.is_running = False
        self._open_host()

    def _open_host(self):
        while True:
            try:
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.bind((self.host, self.port))
                self.server_socket.listen(1)
                print(f"Server started on {self.host}:{self.port}")
                break
            except Exception as e:
                print(f"Error starting host at {self.host}:{self.port}: {e}")
                time.sleep(5)   # Delay

    def _accept_client(self):
        try:
            print("Waiting for client...")
            self.client_socket, client_address = self.server_socket.accept()
            print(f"Client {client_address} connected")
        except Exception as e:
            print(f"Error accepting client: {str(e)}")

    def _listen(self):
        try:
            data = b""    # Emty bytes buffer
            # Reading client data in 1024 bytes chunks
            while True:
                data_chunk = self.client_socket.recv(1024)
                if not data_chunk:
                    break
                data += data_chunk
            if not data:
                return None
            image_type = get_image_type(data)
            if image_type:
                image = bytes_to_image(data)
                image.save(f"client_image.{image_type}")
                print(f"Received client's image: client_image.{image_type}")
            else:
                print(f"Received client's data: {data.decode()[:20]}")
            return data
        except Exception as e:
            print(f"Error listening client: {e}")

    def _talk(self, data):
        try:
            self.client_socket.send(data)
        except Exception as e:
            print(f"Error sending data: {str(e)}")

    def _runLoop(self):
        while True:
            try:
                print("WAIT CLIENT")
                self._accept_client()
                data = self._listen()
            except Exception as e:
                self._open_host()
                continue

    def _open(self):
        pass


    def _close(self):
        pass


class SocketClient:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.is_running = False
        # self.callback = None
        self._connectToServer()

    def _connectToServer(self):
        # Trying to connect to the HOST until connected successfully
        while True:
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((self.server_host, self.server_port))
                print("Connected to server")
                break       # Connected successfully
            except Exception as e:
                print(f"Error connecting to server: {str(e)}")
                time.sleep(5)  # Delay
                continue    # Continue trying to reconnect

    def _runLoop(self):
        while True:
            try:
                data = self._listen()
                if not data:
                    self._connectToServer()
                    continue    # Continue trying to reconnect
            except Exception as e:
                self._connectToServer()
                continue    # Continue trying to reconnect
    
    def _listen(self)->bytes:
        data = self.client_socket.recv(1024)
        if not data:
            print("Server disconnected")
            return None
        else:
            print(f"Server {len(data)}: {data}")
            return data
    
    def _talk(self, data):
        #if self.client_socket and self.is_running:
        try:
            print(len(data))
            self.client_socket.sendall(data if isinstance(data, bytes) else data.encode())
        except Exception as e:
            print(f"Error sending data: {str(e)}")
    
    def _close(self):
        # self.is_running = False
        self.client_socket.close()
    
    # def _open(self):
    #     self.is_running = True