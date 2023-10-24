#Girilen sayının polindrom olup olmadığını bulan program.
sayi = (input("Lütfen sayi giriniz"))
ters=(sayi[::-1])


if ters == sayi:
    print("Sayi palindromdur")
else:
    print("Girilen sayi palindrom değildir")