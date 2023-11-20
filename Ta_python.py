import modul_tugas

print("pilih bangun ruang yang akan diitung?")
print("1.Lingkaran")
print("2.Segi Tiga")

opsi = int(input("\nKetik Pllih: "))
if opsi == 1:
    print("Hitung lingkaran:")
    modul_tugas.lingkaran()
elif opsi == 2:
    alas = int(input("Masukan nilai alas: "))
    tinggi = int(input("Masukan nilai tinggi: "))
    sisi = int(input("Masukan sisinya: "))
    modul_tugas.segitiga(alas,tinggi,sisi)
    