import baholash
 
oquvchilar = {
    "Ali": 95,
    "Vali": 82,
    "Dilnoza": 67,
    "Aziz": 45,
    "Madina": 100,
}
 
for ism, ball in oquvchilar.items():
    print(f"{ism}: {ball} - {baholash.baho_aniqla(ball)}")
 
balllar = list(oquvchilar.values())
print("O'rtacha ball:", baholash.ortacha_hisobla(balllar))
print("Eng yuqori ball:", baholash.eng_yaxshi_ball(balllar))
 