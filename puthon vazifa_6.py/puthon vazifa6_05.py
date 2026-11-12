from oyinlar import son_topish, tanga
 
sirli_son = son_topish.son_yarat(1, 100)
 
while True:
    taxmin = int(input("1 dan 100 gacha son toping: "))
    natija = son_topish.tekshir(taxmin, sirli_son)
    print(natija)
    if taxmin == sirli_son:
        break
 
print("Tanga tashlandi:", tanga.tanga_tashla())
 