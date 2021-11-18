#Mendatar atau Menurun

data= input("Mendatar/Menurun?: ")
if data== "Mendatar":
    kolom = int(input("Masukkan kolom: "))
    print(("#")*kolom)
elif data== "Menurun":
    baris = int(input("Masukkan baris: "))
    print (("*\n")*baris)
else:
    print("Pola tidak dikenali")
