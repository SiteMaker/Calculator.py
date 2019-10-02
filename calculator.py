# Дебильный калькулятор v2

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)
print(Back.RED)
print("Дебильный калькулятор v2")

print(Back.CYAN)
a = float(input("Первое число: "))
b = float(input("Второе число: "))
print(Back.GREEN)
op = input("Операция (+, -, *, /, %): ")

c = "Результат: "
if op == "+":
    c += str(a + b)
elif op == "-":
    c += str(a - b)
elif op == "*":
    c += str(a * b)
elif op == "/":
    c += str(a / b)
elif op == "%":
    c += str(a % b)
else:
    c = "Ошибка: неверная операция"

print(Back.YELLOW)
print(c)

input()
