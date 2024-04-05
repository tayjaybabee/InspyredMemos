"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/__init__.py
 

Description:
    

"""
import socket
import threading


class MemoServer:
    """
    A simple memo server using sockets to receive and store memos.

    Attributes:
        host (str): The server host.
        port (int): The server port.
        memos (list): List to store memos.
    """

    def __init__(self, host='127.0.0.1', port=65432):
        """
        Initializes the memo server with host and port.

        Args:
            host (str): The host to bind the server. Defaults to '127.0.0.1'.
            port (int): The port to bind the server. Defaults to 65432.
        """
        self.host = host
        self.port = port
        self.memos = []

    def handle_client(self, connection, address):
        """
        Handles the client connection to receive memos.

        Args:
            connection (socket.socket): The client connection.
            address (tuple): The client address.
        """
        print(f"Connected by {address}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            memo = data.decode('utf-8')
            print(f"Received memo: {memo}")
            self.memos.append(memo)
        connection.close()

    def start(self):
        """
        Starts the memo server to accept connections and receive memos.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server started at {self.host}:{self.port}")
            while True:
                conn, addr = s.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()


# Example of starting the server
if __name__ == '__main__':
    server = MemoServer()
    server.start()
