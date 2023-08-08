# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

coinNumber = int(input("Введите число монеток: "))

heads = 0
tails = 0
count = 0

while count < coinNumber:
    side = int(input("Укажите какой стороной вверх лежит монета, орел - 1, решка - 0: "))
    if side == 0 or side == 1:
        if side == 1:
            heads += 1
        else:
            tails += 1
        count += 1
    else:
        print("Укажите сторону монеты корректно!")

if heads >= tails:
    print(f"Минимальное число монет которое нужно перевернуть равно {tails}")
else:
    print(f"Минимальное число монет которое нужно перевернуть равно {heads}")
