import threading
from Server.socket import SocketServer

if __name__ == "__main__":
    def handle_callback(message, *args):
        print(message, *args)

    server = SocketServer("127.0.0.1", 1234)

    server_thread = threading.Thread(target=server._runLoop)
    server_thread.start()

    while True:
        command = input("Enter a command (send/stop): ")
        if command == "send":
            data = input("Enter data to send: ").encode()
            server._talk(data)
        elif command == "quit":
            break
