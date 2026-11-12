def baho_aniqla(ball):
    if ball >= 90:
        return "A'lo"
    if ball >= 70:
        return "Yaxshi"
    if ball >= 50:
        return "Qoniqarli"
    return "Qoniqarsiz"
 
 
def ortacha_hisobla(balllar):
    return sum(balllar) / len(balllar)
 
 
def eng_yaxshi_ball(balllar):
    return max(balllar)
 