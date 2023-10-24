#Kullanıcıdan alınan 3 sayının en büyüğünü bulan program.
sayi1=int(input("1.sayiyi giriniz"))
sayi2=int(input("2.sayiyi giriniz"))
sayi3=int(input("3.sayiyi giriniz"))

if sayi1>sayi2 and sayi1>sayi3:
    print("En büyük sayı :"+ str(sayi1))
elif sayi2>sayi1 and sayi2>sayi3:
    print("En büyük sayı :"+str(sayi2))
elif sayi3>sayi1 and sayi3>sayi2:
    print("En büyük sayı:"+str(sayi3))
else:
    print("Lütfen geçerli bir ifade giriniz")