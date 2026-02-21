def catch(Catch):
    if 0 <= Catch <= 9:
     Поимка = "РП 35+"
    elif 10 <= Catch <= 35:
     Поимка = "РП 30+"
    elif 36 <= Catch <= 70:
     Поимка = "РП 25+"
    elif 71 <= Catch <= 125:
     Поимка = "РП 20+"
    elif 126 <= Catch <= 160:
     Поимка = "РП 15+"
    elif 126 <= Catch <= 160:
     Поимка = "РП 10+"
    else:
     Поимка = "РП 8+"
    return Поимка