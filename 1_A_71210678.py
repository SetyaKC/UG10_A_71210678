#Menghitung nilai rata-rata UG, TTS, dan TAS PrakTekKom
#Nilai rata-rata UG 70%
#Nilai rata-rata TTS 15%
#Nilai rata-rata TAS 15%

#standar nilai A: >=85, A-: >=80,  B+: >=75, B: >=70,  B-: >=65, C+: >=60, C: >=55, D: >=45, E: >=0
A = float(input("Masukkan nilai rata-rata UG anda: "))
B= float(input("Masukkan nilai TTS anda: "))
C= float(input("Masukkan nilas TAS anda: "))

print("=========================")
UG = 70/100*A
TTS = 15/100*B
TAS = 15/100*C
NILAI = float(UG+TTS+TAS)

print("Nilai anda: ", NILAI)

if NILAI >=85:
    print("Nilai huruf anda: A")
elif NILAI >=80:
     print("Nilai huruf anda: A-")
elif NILAI >=75:
     print("Nilai huruf anda: B+")
elif NILAI >=70:
     print("Nilai huruf anda: B")
elif NILAI >=65:
     print("Nilai huruf anda: B-")
elif NILAI >=60:
     print("Nilai huruf anda: C+")
elif NILAI >=55:
     print("Nilai huruf anda: C")
elif NILAI >=45:
     print("Nilai huruf anda: D")
else:
     print("Nilai huruf anda: E")
     

     
    


