loop = 0
while loop < 3:
    print("Masukkan Nama Anda:")
    nama = input()
    print("Masukkan Password Anda:")
    password = int(input())
    if nama == "ikhsan" and password == 118:
        print("Masukkan Merk Mobil Yang Ingin Anda Beli:..!")
        merkmobil = input()
        print("Masukkan Harga Mobil:..!")
        harga = int(input())
        harga = harga
        if merkmobil == "tesla":
            diskon = harga * 0.17
            bayartotal = harga - diskon
            print(merkmobil)
            print(bayartotal)
            print("Terimakasih Telah Berbelanja")
        else:
            if merkmobil == "toyota":
                diskon = harga * 0.21
                bayartotal = harga - diskon
                print(merkmobil)
                print(bayartotal)
                print("Terimakasih Telah Berbelanja")
            else:
                if merkmobil == "hyundai":
                    diskon = harga * 0.23
                    bayartotal = harga - diskon
                    print(merkmobil)
                    print(bayartotal)
                    print("Terimakasih Telah Berbelanja")
                else:
                    print("Mobil Yang Anda Cari Tidak Ada!")
                    print("Terimakasih Telah Datang Kemari")
    else:
        print("Apa Anda Ingin Mengakhiri Program Ini:(lanjut / tidak)")
        program = input()
        if program == "lanjut":
            print("Program Anda Telah Selesai!")
        else:
            loop = loop + 1
            print("Batas Percobaan Yang Tersisa Tinggal:!")
            print(loop)
print("Batas Pengulangan Yang Anda Miliki Telah Habis, Terimakasih Telah Mencoba!!")
