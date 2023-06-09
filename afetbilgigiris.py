

def AfetBilgileri(k_adi):
    AfetBilgi=input("Afetler hakkında bilgi almaya hoş geldin {}. Bilgi almak istediğin afeti gir.\n1-Deprem nedir?\n2-Sel nedir?\n3-Çığ nedir?\n4-Heyelan nedir?\n5-Deprem çantasında neler olmalı.\n".format(k_adi))
    AfetBilgi.lower()
    if AfetBilgi=="1":
        print("Deprem, yer sarsıntısı, seizma veya zelzele, yer kabuğunda beklenmedik bir anda ortaya çıkan enerji sonucunda meydana gelen sismik dalgalanmalar ve bu dalgaların yeryüzünü sarsması olayıdır. Sismik aktivite ile kastedilen meydana geldiği alandaki depremin frekansı, türü ve büyüklüğüdür.")
    elif AfetBilgi=="2":
        print(""""Sel, genellikle kuru olan araziyi sular altında bırakan bir su taşkını olayıdır."Akma halinde olan su" anlamına gelen kelime, gelgitin içeri akışına da uygulanabilmektedir. Taşkınlar hidroloji disiplinin bir çalışma alanıdır. Tarım, inşaat mühendisliği ve halk sağlığı gibi alanlarda önemli bir endişe kaynağıdır.""")

    elif AfetBilgi=="4":
        print("Heyelan ya da toprak kayması, zemini kaya veya yapay dolgu malzemesinden oluşan bir yamacın yer çekimi, eğim, su ve benzeri diğer kuvvetlerin etkisiyle aşağı ve dışa doğru hareketidir.")
    elif AfetBilgi=="3":
        print("Çığ, büyük miktarda kar kütlesinin dağdan aşağı kaymasıdır. Aşırı kar yağışlarında taze karın alttaki kar tabakasıyla iyi kaynaşmaması, yüksek ses, rüzgar, insan veya hayvanların oynak kar tabakasını harekete geçirmesi gibi sebeplerden meydana gelir. Büyüklüğüne göre can ve mal kaybına yol açabilir.")
    elif AfetBilgi=="5":
        print("--- DEPREM ÇANTASINDA BULUNMASI GEREKENLER ---\nKimlik bilgilerinin olduğu önemli belgelerin fotokopileri (pasaport, ehliyet, sigorta poliçeleri, banka hesap kayıt bilgilerini içeren belgeler. Evcil hayvan olması durumunda sağlık karnesi)\nİlk yardım çantası\nSu kişi başı 4 litre içme suyu")
        print("Bozulmayan, kuru gıdalar (yüksek kalorili, vitamin ve karbonhidrat içeren gıdalar. Bunlar son kullanma tarihlerine göre yenilenmelidir\nRadyo\nSabun dezenfektan\nEl feneri\nPowerbank\nKağıt kalem\nYedek pil\nUyku tulumu battaniye\nÇakı düdük makas") 
    else:
        print("-- Hatalı tuşlama tekrar deneyin!! --")
def DepremTesti():
    while(True):
        BinaYasim=int(input("Bina yaşınız: "))
        DepremDerecesi=int(input("İlinizin deprem derecesi: "))
        if BinaYasim>=27 and 1<=DepremDerecesi<=3:
            print("Çok tehlikeli durumdasınız gerekli önlemleri alın deprem çantanızı yapın.")
            break
        elif BinaYasim>=27 and 3<DepremDerecesi<=5:
            print("Orta risk içeren gruptasınız gerekli önlemleri alınız.")
            break
        elif 27<BinaYasim<=15 and 1<=DepremDerecesi<=3:
            print("Riskli durumdasınız gerekli önlemleri almanız gerekiyor.")
            break
        elif 27<BinaYasim<=15 and 3<DepremDerecesi<=5:
            print("Orta riskli konumdasınız dikkat edin. Önlem alabilirsiniz.")
            break
        elif BinaYasim<15 and 1<=DepremDerecesi<=3:
            print("Riskli durumdasınız gerekli önlemleri almanız gerekiyor.")
            break
        elif BinaYasim<15 and 3<DepremDerecesi<=5:
            print("Risksiz konumdasınız yine de deprem bilincinde olmanız önemli.")
            break
        else:
            print("-- Hatalı giriş oldu tekrar girin --")
            continue
import sqlite3
conn = sqlite3.connect('KullaniciHesaplari.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (k_adi TEXT, sifre TEXT, Yasadigi_il TEXT, bagis REAL)''')
def İlBilgileri():
           connect = sqlite3.connect('afetbilgileri.db')
           a = connect.cursor()  
           girilen_sehir=input("Sorgulamak istediğiniz şehir adı nedir? : ")
           a.execute('SELECT * FROM sehirler depremriski, digerbilgiler WHERE il = ?', (girilen_sehir,))
           result = a.fetchone()
           if result:
               deprem_riski = result[0]
               diger_bilgiler = result[1]
               print(f"{il} şehri için deprem riski: {deprem_riski}")
               print(f"{il} şehri için diğer bilgiler: {diger_bilgiler}")
           else:
               print("Belirtilen şehir bulunamadı.")
def deprembagisi():
    print("Deprem bağışı yapıyor olman bizi çok mutlu etti.")
    c.execute("SELECT SUM(bagis) FROM users")
    toplam_bagis = c.fetchone()[0]
    if toplam_bagis is None:
        toplam_bagis = 0.0
    print("An itibariyle toplam bağış miktarı:", toplam_bagis)
    bagis_miktari = float(input("Bağışlamak istediğiniz tutar : "))
    c.execute("INSERT INTO users (k_adi, sifre, Yasadigi_il, bagis) VALUES (?,?,?,?)", (k_adi, sifre, il, bagis_miktari))
    conn.commit()
    print("Bağışınız başarıyla kayedildi.")
    

while(True):
    
    print("Afet bilgi programına hoş geldiniz.")
    print("1-Giriş yap\n2-Kaydol\n")
    secim1=input()
    if secim1=="1":
        k_adi=input("Kullanıcı adınız : ")
        sifre=input("Parolanız : ")      
        c.execute("SELECT * FROM users WHERE k_adi=? AND sifre=?", (k_adi, sifre))
        result = c.fetchone()

        if result:
            print("Giriş başarılı!")
            break
        else:
            print("Kullanıcı adı veya şifre yanlış!")
    elif secim1=="2":
        k_adi=input("Kullanıcı adınızı belirleyin : ")
        sifre=input("Şifrenizi belirleyin = ")
        il = input("İlinizi yazın = ")
        if len(sifre)<4:
            print("Sifreniz adınız minumum 4 karakter olabilir")
            continue
        c.execute("INSERT INTO users (k_adi, sifre, Yasadigi_il) VALUES (?, ?, ?)", (k_adi, sifre, il))
        print("Kayıt başarılı! Giriş yap diyerek programa gir.")
        
while(True):
    print("Hoş geldin {} açılan menüden işlemini seç".format(k_adi))
    print("1-İl girerek geçmiş afetler hakkında bilgi al")
    print("2-Afetler hakkında bilgi sahibi ol")
    print("3-Depremden korkmalı mıyım?")
    print("4-Deprem bağışı yapmak istiyorum.")
    print("5-Çıkış yap")
    secim2=int(input())
    if secim2==1:
        İlBilgileri()
    elif secim2==2:
        AfetBilgileri(k_adi)
    elif secim2==3:
        DepremTesti()
    elif secim2==4:
        deprembagisi()
    elif secim2==5:
        break
