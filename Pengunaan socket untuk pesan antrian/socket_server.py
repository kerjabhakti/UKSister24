import socket
import time

# Buat objek socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dapatkan nama mesin lokal
host = socket.gethostname()
port = 9999

# Bind ke port
serversocket.bind((host, port))

# Tunggu hingga 5 permintaan
serversocket.listen(5)

# Menjalankan server dan menerima koneksi dari klien
while True:
    clientsocket, addr = serversocket.accept()
    print("Terhubung dengan %s:%d" % addr)
    print("Server terhubung dengan pengguna")

    # Terima data dari klien
    data = clientsocket.recv(1024).decode('ascii')

    if data == 'kirim':
        print("Memproses pengiriman...")

       

        response = "Barang telah berhasil dikirim!"
        clientsocket.send(response.encode('ascii'))
    else:
        response = "Perintah tidak valid"
        clientsocket.send(response.encode('ascii'))

    clientsocket.close()