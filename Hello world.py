Height, Weight, Frnd, Catch, Health, Atk,Def, SpAtk, SpDef, Spd = map(int, input("Введите в строгой последовательности значения Height Weight Frnd Catch Health Atk Def SpAtk SpDef целым числом через пробел").split())
#Этап 1. Цикл для Роста
x1=Height
Рост = None
МРУ = None
МРБ = None

if 0.1 <= x1 <= 0.49:
    Рост = "Крошечный"
    МРУ = 8
    МРБ = -2
elif 0.5 <= x1 <=0.99:
    Рост = "Маленький"
    МРУ = 5
    МРБ = -2
elif 1.0 <= x1 <= 1.49:
    Рост = "Ниже среднего"
    МРУ = 3
    МРБ = -1
elif 1.5 <= x1 <= 1.99:
    Рост = "Средний"
    МРУ = 0
    МРБ = 0
elif 2.0 <= x1 <= 2.99:
    Рост = "Высокий"
    МРУ = -6
    МРБ = +1
else:
    a = 0
    b = 0

# Теперь a и b определены и готовы к дальнейшим расчётам
print(f"a = {a}, b = {b}")