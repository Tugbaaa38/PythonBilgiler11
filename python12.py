
ogrenciListesi=[]
Ogr_sayisi=int(input("Kac tane ogrenci listelenecek?="))
i=0;
while i < Ogr_sayisi:
    isim=input("Ogrenci isim:")
    soyisim=input("Ogrenci soyisim:")
    ogrenciListesi.append(
        {'isim':isim,
         'soyisim':soyisim
        })
    i+=1

for Ogrenci in ogrenciListesi:
    print(f'Ogrenci adi:{Ogrenci["isim"]} ----- Ogrenci soyad:{Ogrenci["soyisim"]}')  
    #Burada " " kullanmadim.Cunku isim ve soyisim de kullandigim icin karisacakti.Bu yuzden de ' ' ile yazdirdim.

