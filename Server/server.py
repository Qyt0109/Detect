import io
import threading
from Server.socket import SocketServer

from PIL import Image

def isImage(data):
    # Check if the data starts with common image file headers
    image_headers = [
        b'\xFF\xD8\xFF',  # JPEG
        b'\x89PNG',       # PNG
        b'GIF',           # GIF
        b'\x42\x4D',     # BMP
    ]

    for header in image_headers:
        if data.startswith(header):
            return True

    return False


def is_image(data):
    try:
        Image.open(io.BytesIO(data))
        print("image")
        return True
    except (IOError, OSError):
        print("Not image")
        return False

if __name__ == "__main__":
    def handle_callback(message, *args):
        print(message, *args)

    server = SocketServer("127.0.0.1", 1234)
    server.set_callback(handle_callback)
    server.run()

    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    while True:
        command = input("Enter a command (send/stop): ")
        if command == "send":
            data = input("Enter data to send: ")
            server.send_data(data)
        elif command == "stop":
            server.stop()
            break
