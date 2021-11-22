# Main.py
CassierSederhana

total1=0
total2=0
totalsemua=0
jenis1=""
jenis2=""

print("=== Dessert Cake ===")
nama = input("Masukkan nama Konsumen: ")
print ("Nama Konsumen :", nama)
print("")
print ("Menu Base Dessert")
    


def pilihan(i):
        switcher={
                1:'---- Pudding   25000----',
                2:'---- Cake      30000----',
                3:'---- Bread     25000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")


print("1. Pudding")
print("2. Cake")
print("3. Bread")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
porsi1= int(input("Jumlah Porsi: "))

if nomor==1:
    total=total1+porsi1*25000
    print ("Hasilnya = ", total1)
    jenis1=("Pudding")
if nomor==2:
    total1=total1+porsi1*30000
    print ("Hasilnya = ", total1)
    jenis1=("Cake")
if nomor==3:
    total1=total1+porsi1*25000
    print ("Hasilnya = ", total1)
    jenis1=("Bread")

def pilihan(i):
        switcher={
                1:'----Coklat 5000----',
                2:'----Keju   6000----',
                3:'----Oreo   8000----'
             }
        return switcher.get(i,"Masukan Pilihan yang Benar!")
print("\nTopping")
print("1. Coklat")
print("2. Keju")
print("3. Oreo")
nomor=int(input("Masukan Pilihan: "))
menu=pilihan(nomor)
print (menu)
#porsi2= int(input("Berapa Gelas: "))
if nomor==1:
   # total2=total2+(porsi2*5000)
    total2=total2+(porsi1*5000)
    print ("Hasilnya = ", total2)
    jenis2=("Coklat")
if nomor==2:
    #total2=total2+(porsi2*6000)
    total2=total2+(porsi1*6000)
    print ("Hasilnya = ", total2)
    jenis2=("Keju")
if nomor==3:
    #total2=total2+(porsi2*8000)
    total2=total2+(porsi1*8000)
    print ("Hasilnya = ", total2)
    jenis2=("Oreo")
    
uang=int(input("\nUang Tunai: Rp."))
totalsemua=total1+total2    
print("\n=========================")
print("======= S T R U K =======")
print("=========================")
print ("=== Nama      :",nama)
print ("=== Beli      :",porsi1,jenis1)
#print ("===            ",porsi2,jenis2)
print ("=== Topping     ",jenis2)
print ("=== Tagihan   :Rp.",totalsemua)
print ("=== Uang      :Rp.",uang)
akhir=int(uang-totalsemua)
print ("=== Kembalian :Rp.",akhir)
print("=========================")
print("=========================")
print("  TERIMAKASIH SUDAH MEMBELI")
print(" DATANG LAGI YAAAAAA.......")
print("===========================")
print("===========================")
