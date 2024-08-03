# echo-server.py

import socket

class Server:
    HOST = "127.0.0.1"
    PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
    def __init__(self, host = "127.0.0.1" , port = 8080) -> None:
        self.HOST = host
        self.PORT = port
    def Run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)