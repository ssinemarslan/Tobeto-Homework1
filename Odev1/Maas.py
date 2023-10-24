#Kullanıcının zamlı maaşını hesaplayan program.
Maas=float(input("Lütfen maaşınızı giriniz"))
Zam=float(input("Lütfen zam oranını giriniz"))
ZamliMaas=(Maas+((Maas*Zam)/100))
print("Zamlı maaşınız: "+str(ZamliMaas))