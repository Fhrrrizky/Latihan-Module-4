database = {
    "Fahrur"    : "07352311144",
    "Rizky"     : "07352311244",
    "A.I"       : "07352311344"
}

mata_kuliah = {
    "Daspro"    : "Pak Yasir",
    "Aljabar"   : "Pak Fuad",
    "Arsikom"   : "Pak Ceko"
}

def login():
    username = input("Masukkan Username: ")
    if username in database:
        password = input("Masukkan Password: ")
        if database[username] == password:
            print("Autentikasi Berhasil!")
            return True
    print("Autentikasi gagal. Username Atau Password Salah.")
    return False

def input_mata_kuliah():
    print("Pilih Mata Kuliah Yang Ingin Diinput:")
    for i, (mata_kuliah_nama, dosen_pengampuh) in enumerate(mata_kuliah.items(), 1):
        print(f"{i}. {mata_kuliah_nama} (Pengampuh: {dosen_pengampuh})")

    pilihan = int(input("Masukkan Pilihan: "))
    if 1 <= pilihan <= len(mata_kuliah):
        mata_kuliah_nama = list(mata_kuliah.keys())[pilihan - 1]
        dosen_pengampuh = mata_kuliah[mata_kuliah_nama]
        print(f"Anda Memilih Mata Kuliah {mata_kuliah_nama} Yang Diajarkan Oleh {dosen_pengampuh}.")
    else:
        print("Pilihan Tidak Valid.")

def main():
    if login():
        input_mata_kuliah()

main()
