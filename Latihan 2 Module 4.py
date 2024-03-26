nama = input("Masukkan Nama: ")
kehadiran = int(input("Masukkan Total Kehadiran: "))
tugas = int(input("Masukkan Total Tugas: "))
nilai_uts = int(input("Masukkan Nilai UTS: "))
nilai_uas = int(input("Masukkan Nilai UAS: "))

total_nilai = (kehadiran * 16) + tugas + nilai_uts + nilai_uas
nilai_akhir = total_nilai / 4

if nilai_akhir >= 90:
    hasil_nilai = 'A'
elif nilai_akhir >= 80:
    hasil_nilai = 'B'
elif nilai_akhir >= 70:
    hasil_nilai = 'C'
elif nilai_akhir >= 60:
    hasil_nilai = 'D'
else:
    hasil_nilai = 'E'

print("\nNama: ", nama)
print("Nilai Akhir: {:.2f}".format(nilai_akhir))
print("Hasil Nilai Kelulusan:", hasil_nilai)