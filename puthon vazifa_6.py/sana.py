from datetime import date, datetime
 
 
def bugungi_sana():
    return date.today()
 
 
def hozirgi_vaqt():
    return datetime.now().strftime("%H:%M:%S")
 
 
def yilni_aniqla(sana):
    return datetime.strptime(sana, "%Y-%m-%d").year
 