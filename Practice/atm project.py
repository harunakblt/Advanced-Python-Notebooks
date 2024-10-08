hesaplar = {
    "user1": {"password": "1234", "balance": 1000},
    "user2": {"password": "2345", "balance": 2000},
    "user3": {"password": "3456", "balance": 3000}
}

print("ATM Sistemine Hoşgeldiniz")
kullanici_adi = input("Kullanıcı Adı: ")
sifre = input("Şifre: ")

if kullanici_adi in hesaplar and hesaplar[kullanici_adi]["password"] == sifre:
    print(f"Hoşgeldiniz, {kullanici_adi}!")
    while True:
        print("""
              İşlemler:
              1. Bakiye Sorgulama
              2. Para Yatırma
              3. Para Çekme
              4. Çıkış
              """)
        
        secim = input("Bir işlem seçiniz (1-4): ")
        
        if secim == "1":
            bakiye = hesaplar[kullanici_adi]["balance"]
            print(f"Mevcut Bakiyeniz: {bakiye} ₺")
            
        elif secim == "2":
            miktar = float(input("Yatırmak istediğiniz miktar: "))
            
            if miktar > 0:
                hesaplar[kullanici_adi]["balance"] += miktar
                print(f"{miktar} ₺ hesabınıza yatırıldı")
                bakiye = hesaplar[kullanici_adi]["balance"]
                print(f"Mevcut Bakiyeniz: {bakiye} ₺")
                
            else:
                print("Girdiğiniz değer geçersiz bir miktrardır.")
                
        elif secim == "3":
            miktar = float(input("Çekmek istediğiniz miktar: "))
            
            if miktar > 0 and miktar <= hesaplar[kullanici_adi]["balance"]:
                hesaplar[kullanici_adi]["balance"] -= miktar
                print(f"{miktar} ₺ hesabınızdan çekildi")
                bakiye = hesaplar[kullanici_adi]["balance"]
                print(f"Mevcut Bakiyeniz: {bakiye} ₺")
                
            else:
                print("Yetersiz bakiye veya geçersiz miktar.")
                
        elif secim == "4":
            print("Çıkış yapılıyor. İyi günler!")
            break
        
        else:
            print("Geçersiz bir seçim yaptınız, lütfen 1-4 arasında bir sayı giriniz.")

else:
    print("Geçersiz kullancı adı yada şifre")