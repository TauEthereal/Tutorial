import my_functions.height_coefficients
import my_functions.weight_coefficients
Height, Weight, Frnd, Catch, Health, Atk,Def, SpAtk, SpDef, Spd = map(int, input("Введите в строгой последовательности значения Height (в метрах) Weight Frnd Catch Health Atk Def SpAtk SpDef целым числом через пробел").split())
#Этап 1. Цикл для Роста
Рост,МРУ,МРБ = height_coefficients.heights(Height)
#Этап 2. Цикл для Массы
Масса, ММУ, ММБ,ММЗ = weight_coefficients.weights(Weight)
print(Масса)