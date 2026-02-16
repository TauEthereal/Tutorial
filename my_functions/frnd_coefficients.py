def frnds(Frnd):
    if 0 <= Frnd <= 34:
     Дружелюбие = 0
    elif 35 <= Frnd <= 69:
     Дружелюбие = 1
    elif 70 <= Frnd <= 89:
     Дружелюбие = 2
    elif 90 <= Frnd <= 99:
     Дружелюбие = 3
    elif 100 <= Frnd <= 139:
     Дружелюбие = 4
    else:
     Дружелюбие = 5
    return Дружелюбие