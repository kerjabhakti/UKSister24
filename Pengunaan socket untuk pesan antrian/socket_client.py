# client.py
import socket

def send_message(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))
    s.sendall(message.encode('ascii'))
    response = s.recv(1024)
    s.close()
    return response.decode('ascii')

# Main program
print("Selamat datang di sistem pengiriman barang!")