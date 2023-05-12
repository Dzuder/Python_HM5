# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

numb = int(input("Введите число: "))
exponent = int(input("Введите степень числа: "))


def square_number(x, y):  
    if y == 1:
        return x
    return square_number(x, y - 1) * x

    
print(f"{numb} в степени {exponent} = {square_number(numb, exponent)}")