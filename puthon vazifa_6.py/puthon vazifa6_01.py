import parol
 
uzunlik = int(input("Parol uzunligini kiriting: "))
yangi_parol = parol.parol_yarat(uzunlik)
 
print("Yaratilgan parol:", yangi_parol)
print("Parol yetarlimi:", parol.parol_tekshir(yangi_parol))
 