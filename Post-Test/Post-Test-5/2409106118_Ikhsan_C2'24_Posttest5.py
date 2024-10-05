# Inisialisasi data pengguna dan data tiket konser
akun_pengguna = []
tiket_konser = []

while True:
    print("Halo! Selamat Datang di Pemesanan Tiket Konser")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username: ")
        akuna = False
        for akun in akun_pengguna:
            if akun[0] == Username:  # Memeriksa apakah username sudah ada
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            role = input("Masukkan peran (admin/pengguna): ").lower()
            if role not in ['admin', 'pengguna']:
                print("Peran tidak valid. Harus 'admin' atau 'pengguna'.")
                continue
            akun_pengguna.append([Username, Password, role, []])  # Simpan username, password, dan tiket (sebagai list kosong)
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akun_pengguna:
            if akun[0] == Username and akun[1] == Password:  # Cocokkan username dan password
                while True:
                    print(f"\nSelamat datang {Username}!")
                    print("―――Silakan pilih aksi!―――")
                    if akun[2] == 'admin':
                        print("1. Tambah tiket konser")
                        print("2. Lihat tiket konser")
                        print("3. Edit tiket konser")
                        print("4. Hapus tiket konser")
                    else:
                        print("1. Beli tiket konser")
                        print("2. Lihat tiket konser yang sudah dibeli")
                    print("5. Exit")
                    print("―――――――――――――――――――――――――――――")

                    status = input("Pilih opsi: ")
                    print(" ")

                    if status == "1":
                        if akun[2] == 'admin':
                            judul_konser = input("Judul Konser: ")
                            harga_tiket = input("Harga Tiket: ")
                            tiket_konser.append([judul_konser, harga_tiket])  # Menambahkan tiket ke dalam list
                            print("Tiket konser berhasil ditambahkan!\n")
                        else:
                            judul_konser = input("Judul Konser: ")
                            for tiket in tiket_konser:
                                if tiket[0] == judul_konser:
                                    akun[3].append([judul_konser, tiket[1]])  # Menambahkan tiket ke dalam list
                                    print("Tiket konser berhasil dibeli!\n")
                                    break
                            else:
                                print("Tiket konser tidak tersedia.\n")

                    elif status == "2":
                        if akun[2] == 'admin':
                            for tiket in tiket_konser:  
                                print(f"Judul Konser: {tiket[0]}\nHarga Tiket: {tiket[1]}\n")
                            if not tiket_konser:
                                print("Opps, saat ini belum ada tiket konser, silahkan tambah tiket terlebih dahulu.\n")
                        else:
                            for tiket in akun[3]:  
                                print(f"Judul Konser: {tiket[0]}\nHarga Tiket: {tiket[1]}\n")
                            if not akun[3]:
                                print("Opps, saat ini kamu belum punya tiket, silahkan beli tiket terlebih dahulu.\n")
                            
                    elif status == "3":
                        if akun[2] == 'admin':
                            if not tiket_konser:
                                print("Tidak ada tiket konser yang bisa diedit.")
                            else:
                                edit = int(input("Tiket konser nomor berapa yang ingin kamu edit: ")) - 1
                                if 0 <= edit < len(tiket_konser):
                                    judul_baru = input("Masukkan judul yang baru: ")
                                    harga_baru = input("Masukkan harga yang baru: ")
                                    print("Apa kamu yakin ingin mengedit tiket konser ?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_edit = input("Pilih: ")
                                    if memastikan_edit == "1":
                                        tiket_konser[edit] = [judul_baru, harga_baru]  # Mengedit tiket konser
                                        print("Tiket konser yang kamu pilih sudah di edit ya!\n")
                                    elif memastikan_edit == "2":
                                        print("Aksi untuk mengedit tiket konser dibatalkan")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor tiket konser yang kamu maksud, silahkan input ulang.\n")
                        else:
                            print("Anda tidak memiliki akses untuk mengedit tiket konser.\n")

                    elif status == "4":
                        if akun[2] == 'admin':
                            if not tiket_konser:
                                print("Tidak ada tiket konser yang bisa dihapus.")
                            else:
                                hapus = int(input("Tiket konser nomor berapa yang ingin dihapus: ")) - 1
                                if 0 <= hapus < len(tiket_konser):
                                    print(f"Apa kamu yakin ingin menghapus tiket konser ? ")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_hapus = input("Pilih: ")
                                    if memastikan_hapus == "1":
                                        del tiket_konser[hapus]  # Menghapus tiket konser dari list
                                        print("Tiket konser yang kamu pilih sudah dihapus!\n")
                                    elif memastikan_hapus == "2":
                                        print("Aksi untuk menghapus tiket konser dibatalkan")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor tiket konser yang kamu maksud, silahkan input ulang.\n")
                        else:
                            print("Anda tidak memiliki akses untuk menghapus tiket konser.\n")

                    elif status == "5":
                        print("Aplikasi Pembelian Tiket Konser ditutup.\n")
                        break

                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
                break
        else:
            print("Username dan password anda salah, silahkan coba lagi\n")

    elif opsi == "3":
        print("Apakah kamu yakin ingin keluar dari aplikasi? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")