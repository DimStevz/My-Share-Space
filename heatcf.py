#Dimas Stevano Ethanuel | X IPA 3 | 8
import time

print ("Alat Apa yang anda ingin buka?")
Choice = int (input ("1.Pengkonversi, dari celcius ke farenheit \n2.Menentukan Kelulusan Siswa \n> "))

if Choice == 1 :
    print ("----------------------------------------------------")
    print ("     Pengubah suhu, dari celcius ke farenheit       ")
    print ("----------------------------------------------------")
    time.sleep(1)
    Converter = int (input ("Masukkan nilai (Celcius) : "))
    print ((Converter*9/5)+32, "°F")

if Choice == 2 :
    nama = input ("Nama Siswa: ")
    kelas = input ("Kelas : ")
    Nilai = int (input ("Masukkan nilai siswa : "))
    time.sleep(1)
    
    if Nilai >=70 :
        time.sleep(0.5)
        print("\nNama siswa: ", nama)
        print("Kelas : ", kelas)
        print ("Siswa dinyatakan lulus")
    if Nilai < 70 :
        time.sleep(0.5)
        print("\nNama siswa: ", nama)
        print("Kelas : ", kelas)
        print ("Siswa dinyatakan tidak lulus")
