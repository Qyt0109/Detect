import base64
import io
import socket
import threading
import time
import pdb


from Server.socket import SocketClient

from PIL import Image

if __name__ == "__main__":
    """
    def handle_callback(message, *args):
        print(message, *args)

    client = SocketClient("127.0.0.1", 1234)
    client.set_callback(handle_callback)

    client_thread = threading.Thread(target=client.start)
    client_thread.start()

    while True:
        command = input("Enter a command (send/stop): ")
        if command == "send":
            data = input("Enter data to send: ")
            client.send_data(data)
        if command == "img":
            img = Image.open("test.jpg")
            # Convert the image to bytes
            # Save the modified image to bytes.
            with io.BytesIO() as byte_io:
                img.save(byte_io, format='JPEG')
                byte_io.seek(0)
                image_bytes = byte_io.read()
            base64_image_bytes = base64.b64encode(image_bytes).decode('utf-8')
            print(len(base64_image_bytes))
            client.send_data(image_bytes)
        elif command == "stop":
            client.stop()
        elif command == "resume":
            client.resume()
    """
    HOST = "127.0.0.1"
    PORT = 1234

    client = SocketClient(HOST, PORT)
    client._open()

    client_thread = threading.Thread(target=client._runLoop)
    client_thread.start()

    while True:
        command = input("Enter a command (send/img/close/open): ")
        if command == "send":
            data = input("Enter data to send: ")
            client._talk(data)
        if command == "img":
            img = Image.open("test.jpg")
            # Convert the image to bytes
            # Save the modified image to bytes.
            with io.BytesIO() as byte_io:
                img.save(byte_io, format='JPEG')
                byte_io.seek(0)
                image_bytes = byte_io.read()
            base64_image_bytes = base64.b64encode(image_bytes).decode('utf-8')
            print(len(base64_image_bytes))
            client._talk(image_bytes)
        elif command == "close":
            client._close()
        elif command == "open":
            client._open()
