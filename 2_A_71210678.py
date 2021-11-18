#Kalkulator Advance Sederhana

print ("############################")
print ("Kalkulator Advance Sederhana")
print ("############################")
print ("1. Menghitung sisa hasil bagi")
print ("2. Membulatkan ke bawah hasil pembagian")
print ("3. Mencari akar kubik sebuah bilangan")

menu = int(input("Masukkan menu yang dipilih: "))

if menu == 1:
    a=float(input("Masukkan bilangan yang ingin dibagi: "))
    b=float(input("Masukkan bilangan pembagi: "))
    sisa=a%b
    print("Sisa hasil bagi ",a, "dibagi dengan",b, "adalah", sisa)
elif menu == 2:
    a=float(input("Masukkan bilangan yang ingin dibagi: "))
    b=float(input("Masukkan bilangan pembagi: "))
    hasil=a/b
    print("Hasil pembagian ",a, "dibagi dengan",b, "dibulatkan kebawah adalah", hasil)
elif menu == 3:
    a=float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    kubik= a**(1/3)
    print("Akar kubik dari", a, "adalah", kubik)
else:
    print("Menu yang anda pilih tidak tersedia")

    
