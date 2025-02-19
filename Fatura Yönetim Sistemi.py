from functools import reduce

fatura_listesi = ["Elektrik", "Su", "Doğalgaz", "İnternet", "Telefon"]
toplam_fatura = list()
güncel_fatura = list()

elektrik = int(input("Lütfen elektrik faturasını giriniz : "))
su = int(input("Lütfen su faturasını giriniz : "))
doğalgaz = int(input("Lütfen doğalgaz faturasını giriniz : "))
internet = int(input("Lütfen internet faturasını giriniz : "))
telefon = int(input("Lütfen telefon faturasını giriniz : "))

toplam_fatura.append(elektrik)
toplam_fatura.append(su)
toplam_fatura.append(doğalgaz)
toplam_fatura.append(internet)
toplam_fatura.append(telefon)


while True:

    print("""
    İşlem seçiniz :

    1. Fatura bilgilerini giriniz
    2. Faturaları KDV ekleyerek tekrar hesaplayınız
    3. 200 TL den büyük faturaları ayırınız 
    4. Toplam ödenecek fatura tutarını hesaplayınız
    5. Sistemden çıkınız 

    """)

    işlem = int(input("Bir işlem seçiniz : "))

    if işlem == 1:
        for i, j in zip(fatura_listesi, toplam_fatura):
            print(i, j)


    elif işlem == 2:

        def KDV(x):
            x = x + (x * (18 / 100))
            return x

        güncel_fatura = list(map(KDV, toplam_fatura))

        liste = []

        for i, j in zip(fatura_listesi, güncel_fatura):
            print(i, j)


        with open("fatura.txt", "w", encoding="utf-8") as file :

            for i, j in zip(fatura_listesi, güncel_fatura):
                file.write (f" {i} : {j} TL \n")


    elif işlem == 3:

        yüksek_fatura = list(filter(lambda x: x > 200, güncel_fatura))
        print("200 TL den yüksek gelen fatura listesi : {}".format(yüksek_fatura))

    elif işlem == 4:

        toplam_ödenecek_tutar = reduce(lambda x, y: x + y, güncel_fatura)

        print("Toplam ödenecek fatura miktarı : {}".format(toplam_ödenecek_tutar))

        with open("fatura.txt","a" ,encoding = "utf-8") as file :
            file.write(f"Toplam ödenecek tutar : {toplam_ödenecek_tutar} TL\n")


    elif işlem == 5:

        print("Sistemden çıkılıyor...")
        break

    else:

        print("Yanlış bir seçim yaptınız ...")
        break





