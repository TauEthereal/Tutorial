import height_coefficients
Height, Weight, Frnd, Catch, Health, Atk,Def, SpAtk, SpDef, Spd = map(int, input("Введите в строгой последовательности значения Height (в метрах) Weight Frnd Catch Health Atk Def SpAtk SpDef целым числом через пробел").split())
#Этап 1. Цикл для Роста
x1=Height
Рост,МРУ,МРБ = height_coefficients.heights(x1)
print(Рост,МРУ,МРБ)