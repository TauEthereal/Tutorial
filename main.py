import my_functions
import math
Height, Weight, Frnd, Catch, Health, Atk,Def, SpAtk, SpDef, Spd = map(float,input("Введите в строгой последовательности значения Height в метрах, Weight Frnd Catch Health Atk Def SpAtk SpDef Spd целым числом через пробел").split())
Growth = input("Введите значение атрибута Growth Rate на английском, как-то: Medium Fast")
#Этап 1. Цикл для Роста
Рост,МРУ,МРБ = my_functions.heights(Height)
#Этап 2. Цикл для Массы
Масса, ММУ, ММБ,ММЗ = my_functions.weights(Weight)
#Этап 3. Цикл для Дружелюбия
Дружелюбие = my_functions.frnds(Frnd)
#Этап 4. Цикл для теста Опыта
XP = my_functions.growths(Growth)
#Этап 5. Цикл для поимки
Поимка = my_functions.catch(Catch)
#Этап 6. Цикл для здоровья
Здоровье = math.ceil(Health/10 + ММЗ)
#Этап 7. Основные статы
Атака = my_functions.stats(Atk)
Защита = my_functions.stats(Def)
Спецатака = my_functions.stats(SpAtk)
Спецзащита = my_functions.stats(SpDef)
Уворот = my_functions.stats(Spd,МРУ,ММУ)
#Этап 8. Быстрота
Быстрота = math.ceil(Spd/15)+МРБ+ММБ
#Этап 9. Вывод
print(Рост)
print(Масса)
print(Дружелюбие)
print(XP)
print(Поимка)
print(Здоровье)
print(Атака)
print(Защита)
print(Спецатака)
print(Спецзащита)
print(Уворот)
print(Быстрота)