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
while True:
    print("\nMenu:")
    print("1. Cek status pengiriman")
    print("2. Kirim barang")
    print("3. Keluar")

    choice = input("Pilih menu (1/2/3): ")
