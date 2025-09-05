from utils import konversi_suhu

print("- - - Konversi Suhu - - -")
batas = "=" * 30
print(batas)
print("Selamat datang di program konversi suhu by Cihuy Company !")
print("Silahkan pilih opsi konversi suhu yang diinginkan:")
print(batas)
nilai = float(input("Masukkan nilai suhu: "))
dari = str(input("Masukkan satuan suhu awal (C/F/K): ")).lower()
ke = str(input("Masukkan satuan suhu akhir (C/F/K): ")).lower()
print(batas)
hasil = konversi_suhu(nilai, dari, ke)
print(f"Hasil dari: {nilai}°{dari.upper()} adalah = {hasil}°{ke.upper()}")
print("Terima kasih telah menggunakan program konversi suhu by Cihuy Company!")
print("semoga harimu menyenangkan, Cihuyyyy !")
