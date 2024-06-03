"""
Напишите скрипт который выводит надпись "Hello, world",
 если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. 
В таком случае выведите надпись "Hello, {Имя}"
Пример ввода: python file.py Argument --name John
Пример вывода: Hello, John
"""
import sys

args = sys.argv[1:]

if not args:
    print('Hello, world')

elif args[0] == '--name':
    name = args[1]
    print(f'Hello, {name}')
    
else:
    print('Unexpected arg')

"""
Напишите скрипт который получает системный ввод от пользователя 
и выводит надпись "команда принята" если ввод начинается
с sys.in.
"""

import sys

input = sys.stdin.readline()

if input.startswith("sys.in"):
    print("команда принята")

"""
Напишите скрипт который принимает 2 аргумента и записывает 
первый аргумент в файл, где имя файла - второй аргумент.
"""

import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]

with open(arg2, "w") as file:
    file.write(arg1)

"""
Напишите скрипт-калькулятор, который принимает 3 аргумента:
1. первый аргумент
2. второй аргумент
3. операцию
и вычисляет результат
"""
import sys

def calc(arg1, arg2, operation):

    if operation == "+":
        return arg1 + arg2

    elif operation == "-":
        return arg1 - arg2

    elif operation == "*":
        return arg1*arg2

    elif operation == "/":
        if arg2 == 0:
            return('Division by zero')
        return arg1/arg2
   
    else:
        return('Operation is not supported')

def main():
   
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    operation = sys.argv[3]

    result = calc(arg1, arg2, operation)
    print(result)

if __name__ == "__main__":
    main()

"""
Напишите скрипт, который читает ввод в стандартный поток ввода и 
выводит длину введенных строк в стандартный поток вывода. Скрипт должен работать 
пока не будет введена пустая строка.
"""
import sys

while True:

    string = sys.stdin.readline()

    if not string:
        break

print(len(string))