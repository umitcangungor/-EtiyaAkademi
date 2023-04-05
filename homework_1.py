baslik = "HABERİNİZ OLSUN" #str
vade = 12 #int
faizOrani1 = 1.48 #float
faizOrani2 = 1.44
faizOrani = 1.47

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "Hoşgeldin"
musteriAdi ="Ümit"
musteriSoyadi = "Güngör"
sonucMesaj = mesaj+" "+musteriAdi+" "+musteriSoyadi+"!"
print(sonucMesaj)

sayi1 = 10
sayi2 = 20

print(sayi1+sayi2)

print(sonucMesaj)

dolarDun = 7.65
dolarBugun = 7.75

# if  dolarDun>dolarBugun:
#     print("Azalış oku")
# if dolarDun<dolarBugun:
#     print("Artış oku")
# if dolarDun==dolarBugun:
#     print("Eşittir oku")

if  dolarDun>dolarBugun:
    print("Azalış oku")
    print("Bitti")
elif dolarDun<dolarBugun:
    print("Artış oldu")
else:
    print("Eşittir oku")

print("Bitti")

krediler = ["Hızlı kredi" , "Maaşını Halkbank'tan alanlara özel" , "Mutlu emekli ihtiyaç kredisi"]

print(krediler)

print(krediler[1])
print(krediler[2])
print(krediler[0])

print(len(krediler))

krediler[0] = "Çabuk kredi"

print(krediler[1])

for kredi in krediler:
    print(kredi)

for kredi in krediler:
  print("<option>"+kredi+"<option>")

for i in range(len(krediler)):
   print(krediler[i])
       
for i in range(3,10):
    print(i)

for i in range(0,11,2):
    print(i)

def kredileriListele():
    krediler = ["Hızlı kredi" , "Maaşını Halkbank'tan alanlara özel" , "Mutlu emekli ihtiyaç kredisi"]
    for kredi in krediler:
      print("<option>"+kredi+"<option>")
kredileriListele()

s
