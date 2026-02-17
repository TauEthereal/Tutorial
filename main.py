import my_functions
Height, Weight, Frnd, Catch, Health, Atk,Def, SpAtk, SpDef, Spd = map(int, input("Введите в строгой последовательности значения Height (в метрах) Weight Frnd Catch Health Atk Def SpAtk SpDef целым числом через пробел").split())
Growth = input("Введите значение атрибута Growth Rate на английском, как-то: Medium Fast")
#Этап 1. Цикл для Роста
Рост,МРУ,МРБ = my_functions.height_coefficients.heights(Height)
print(Рост)
#Этап 2. Цикл для Массы
Масса, ММУ, ММБ,ММЗ = my_functions.weight_coefficients.weights(Weight)
print(Масса)
#Этап 3. Цикл для Дружелюбия
Дружелюбие = my_functions.frnd_coefficients.frnds(Frnd)
print(Дружелюбие)
#Этап 4. Цикл для теста Опыта
XP = my_functions.growth_coefficients.growths(Growth)
print(XP)
#Этап 5. Цикл для поимки