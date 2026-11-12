import random
import string
 
 
def parol_yarat(uzunlik):
    belgilar = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(random.choice(belgilar) for _ in range(uzunlik))
 
 
def parol_tekshir(parol):
    return len(parol) >= 8
 