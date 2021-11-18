#Skor Pertandingan Sepak Bola

artikel=input("Masukkan artikel yang ingin dipindai: ")
klub=input("Masukkan nama klub favorit anda: ")
skor=input("Masukkan skor yang ingin dicari: ")

if klub in artikel and skor in artikel:
    print("Hasil pencarian ditemukan")
elif klub in artikel:
    print("Hanya",klub,"yang ditemukan pada artikel ini")
elif skor in artikel:
    print("Hanya",skor," yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian",klub,"dan",skor,"tidak ditemukan")
