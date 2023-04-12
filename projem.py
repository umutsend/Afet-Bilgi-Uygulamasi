k_adi="umut"
parola="123"
while (True):
    giris=input("Deprem bilgilendirme programına hoş geldin!\n1-Giriş yap\n2-Üye ol\n3-Şifremi unuttum\n")
    if giris=="1":
            while (True):
                giris_k_adi=input("Kullanıcı adınızı giriniz = ")
                giris_parola=input("Parolanızı giriniz = ")
                if giris_k_adi==k_adi and giris_parola==parola:
                    print("HOŞ GELDİNİZ {}".format(k_adi.upper()))
                    break
                if not giris_parola:
                    print("Parola kısmı boş bırakılamaz!!")
                if not giris_k_adi:
                    print("kullanıcı adı kısmı boş bırakılamaz")
                else:
                    print("hatalı kullanıcı adı veya parola")
    elif giris=="2":
            while(True):
                k_adi=input("Kullanıcı adınızı belirleyin = ")
                parola=input("Parolanızı belirleyiniz = ")
                if len(k_adi)<5:
                    print("kullanıcı adı 5 karakterden az olmamalıdır.")
                    continue
                if len(parola)<4:
                    print("parolanız 4 karakterden az olamaz")
                    continue
                if not parola:
                    print("Parola kısmı boş bırakılamaz!!")
                if not k_adi:
                    print("kullanıcı adı kısmı boş bırakılamaz")
                break                        
    elif giris=="3":
                parola=str(input("yeni parolanızı girin= "))
                continue
    
    
   
    
   secim1=input("{} Hoş geldin! açılacak menüden yapacağın işlemi seç. \n1-İl girerek yaşanmış afetleri görüntüle \n2-Afetler hakkında bilgi al \n3-Programdan çık.\n".format(k_adi))








        
        
        

