import socket
import time
import random

# Buat objek socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dapatkan nama mesin lokal
host = socket.gethostname()
port = 9999

# Bind ke port
serversocket.bind((host, port))

# Tunggu hingga 5 permintaan
serversocket.listen(5)

# Simulasi data pengiriman (misalnya untuk pelacakan)
tracking_data = {
    '123456': 'Barang sedang dalam perjalanan',
    '654321': 'Barang telah tiba di tujuan',
}

# Menjalankan server dan menerima koneksi dari klien
while True:
    clientsocket, addr = serversocket.accept()
    print("Terhubung dengan %s:%d" % addr)
    print("Server terhubung dengan pengguna")

    # Terima data dari klien
    data = clientsocket.recv(1024).decode('ascii')
    command_parts = data.split()
    command = command_parts[0]

    if command == 'KIRIM':
        print("Memproses pengiriman...")

        # Simulasi pembuatan nomor pelacakan
        tracking_number = str(random.randint(100000, 999999))
        destination = command_parts[1]
        weight = command_parts[2]
        time.sleep(3)

        # Tambahkan data pelacakan baru
        tracking_data[tracking_number] = f"Barang sedang dalam perjalanan ke {destination}, berat: {weight} kg"

        response = tracking_number
        clientsocket.send(response.encode('ascii'))
    
    elif command == 'CEK':
        tracking_number = command_parts[1]
        response = tracking_data.get(tracking_number, 'Nomor pelacakan tidak ditemukan')

        clientsocket.send(response.encode('ascii'))
    
    else:
        response = "Perintah tidak valid"
        clientsocket.send(response.encode('ascii'))

    clientsocket.close()
