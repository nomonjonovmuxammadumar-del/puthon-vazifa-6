import lugat
 
sozlar = {}
 
lugat.soz_qosh(sozlar, "apple", "olma")
lugat.soz_qosh(sozlar, "book", "kitob")
lugat.soz_qosh(sozlar, "water", "suv")
lugat.soz_qosh(sozlar, "house", "uy")
lugat.soz_qosh(sozlar, "friend", "do'st")
 
print(lugat.soz_qidir(sozlar, "apple"))
print(lugat.soz_qidir(sozlar, "car"))
lugat.lugatni_kor(sozlar)
 