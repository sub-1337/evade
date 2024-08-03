# echo-client.py

import socket

class Client:
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server
    def __init__(self, host = "127.0.0.1", port = 8080) -> None:
        self.HOST = host
        self.PORT = port
    def Run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.HOST, self.PORT))
                s.sendall(b"Hello, world")
                data = s.recv(1024)
            except:
                print("Sme error")

        print(f"Received {data!r}")