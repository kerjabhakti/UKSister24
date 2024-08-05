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

    if choice == "1":
        tracking_number = input("Masukkan nomor pelacakan: ")
        response = send_message(f"CEK {tracking_number}")
        print(f"Status pengiriman: {response}")

    elif choice == "2":
        destination = input("Masukkan alamat tujuan: ")
        weight = input("Masukkan berat barang (kg): ")
        response = send_message(f"KIRIM {destination} {weight}")
        print(f"Barang berhasil dikirim. Nomor pelacakan: {response}")

    elif choice == "3":
        print("Terima kasih telah menggunakan layanan kami.")
        break

    else:
        print("Menu tidak valid. Silakan pilih menu yang tersedia.")
