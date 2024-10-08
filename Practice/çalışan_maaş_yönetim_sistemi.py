# **1. Çalışan Maaş Yönetim Sistemi** ***----ÖDEV----***

# Bir şirketin çalışanlarının adlarını ve maaşlarını yönetmek için bir program yazıyorsunuz. Program, kullanıcıya çalışan eklemeyi, mevcut çalışanları listelemeyi, belirli bir maaştan yüksek olan çalışanları filtrelemeyi ve programdan çıkmayı seçenek olarak sunuyor.

# **Talimatlar:**

# 1. Çalışan Ekle:
# * Kullanıcıdan yeni bir çalışanın adını ve maaşını girmesi istenir.
# * Girilen maaşın geçerli bir sayı olup olmadığı kontrol edilir.
# * Geçerli ise, çalışan listesine adı ve maaşıyla birlikte eklenir ve eklenen çalışanın bilgisi kullanıcıya gösterilir.
# * Geçersiz maaş girişi durumunda kullanıcıya uyarı verilir ve işlem tekrarlanır.

# 2. Çalışanları Listele:
# * Eğer henüz hiç çalışan eklenmemişse, "Henüz çalışan eklenmedi." mesajı gösterilir.
# * Eğer çalışanlar varsa, her çalışanın adı ve maaşı sırasıyla listelenir.

# 3. Belirli Maaştan Yüksek Olan Çalışanları Filtrele:
# * Kullanıcıdan bir minimum maaş değeri girmesi istenir.
# * Girilen değerin geçerli bir sayı olup olmadığı kontrol edilir.
# * Geçerli ise, girilen maaştan yüksek olan tüm çalışanlar listelenir.
# * Bu çalışanlar varsa, her birinin adı ve maaşı gösterilir.
# * Belirtilen maaştan yüksek çalışan yoksa, kullanıcıya bilgi verilir.

# 4. Çıkış:
# * Kullanıcı programdan çıkmak istediğinde seçenek sunulur.
# * "4" tuşuna basılarak çıkış yapılır ve program sonlandırılır.


employees = []

def add_employee():
    name = input("Çalışan adını giriniz: ")
    salary = input("Maaşını giriniz :")
    if salary.isdigit():
        employees.append({"name": name, "salary" : int(salary)})
        print(f"{name} adlı çalışan eklendi")

    else:
        print("Geçersiz maaş girdiniz.Lütfen tekrar deneyiniz.")

def list_employees():
    if not employees:
        print("Henüz çalışan eklenmedi")
    else:
        for employee in employees:
            print(f"çalışan :{employee['name']}, Maaş : {employee['salary']} ")

def filter_employees_by_salary(min_salary):
    filtered_employees = list(filter(lambda employee: employee['salary'] > min_salary, employees))
    if not filtered_employees:
        print(f"{min_salary} maaşından yüksek maaşta çalışan yok.")
    else:
        for employee in filtered_employees:
            print(f"Çalışan : {employee['name']}, Maaş : {employee['salary']}")

def main():
    while True:
        print("""
              1. Çalışan Ekle
              2. Çalışanları Listele
              3. Belirli Maaştan Yüksek Olan Çalışanları Filtre
              4. Çıkış

""")
        
        choice = input("Lütfen size belirtilen listeden seçim yapınız (1-4):")
        if choice == "1":
            add_employee()
        elif choice == "2":
            list_employees()
        elif choice == "3":
            min_salary = input("Lütfen minimum maaşı giriniz:")
            if min_salary.isdigit():
                filter_employees_by_salary(int(min_salary))
            else:
                print("Geçersiz maaş girdiniz. Lütfen tekrar deneyiniz.")
        elif choice == "4":
            print("Programdan çıkış yapılıyor")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")

if __name__ == "__main__":
    main()

