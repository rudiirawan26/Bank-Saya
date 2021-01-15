while True:
    if option == "x":
        print("============================")
        print("Selamat Datang di ATM saya")
        print("============================")
        print('')
        option1 = print("1. Chek Uang saya")
        option2 = print("2. Ambil Uang saya")
        option3 = print("3. Tabung Uang saya")
        print('')
        total = 0
        option = int(input("Silakan pilih Option: "))
        if option == 1:
            print("Uang kamu berjumlah: ",total)
        elif option == 2:
            ngambil_uang = eval(input("Masukan nominal uang yang akan di ambil: "))
            rumus = total - ngambil_uang
            if ngambil_uang <= total:
                print("Selamat anda berhasil ngambil unang")
            else:
                print("Saldo anda tidak mencukupi")
        elif option == 3:
            menabung = eval(input("Masukan nominal uang yang kan di tabung: "))
            rumus_menabung = menabung + total
            print("Proses menabung SUKSES")
        else:
            print("Masukan tidak di kenali")
else:
    print("Anda telah keluar dari program")
