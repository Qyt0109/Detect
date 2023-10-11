import socket
import time

class SocketClient:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_running = False
        self.callback = None
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
                self._connectToServer()
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
        if self.client_socket and self.is_running:
            try:
                print(len(data))
                self.client_socket.sendall(data if isinstance(data, bytes) else data.encode())
            except Exception as e:
                print(f"Error sending data: {str(e)}")
    
    def _close(self):
        self.is_running = False
        self.client_socket.close()
    
    def _open(self):
        self.is_running = True

