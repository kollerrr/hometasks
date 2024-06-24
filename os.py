import os

def t1():
    """
    Создайте программу возвращающую информацию о системе вида:
    Операционная система - ХХХ
    Имя компьютера - ХХХ
    Имя пользователя - ХХХ
    """

    print(f"Операционная система - {os.name}")
    print(f"Имя компьютера - {os.environ.get('COMPUTERNAME')}")
    print(f"Имя пользователя - {os.environ.get('USERNAME')}")

################################################################################



def t2(dir: str, num: int):
    """
    Создайте программу создающую папку dir внутри которой еще num папок,
    имена которых цифры от 1 до num
    """
    os.mkdir(r'C:\Code VS\python-2-2-cxZvezdochet')
    num = int(input())

    for num in (1, num):

        os.path.mkdir(dir, 'num')
        print(f"Создана папка номер {num} в папке dir")
        
################################################################################


def t3(dir: str, name: str):
    """
    Напишите программу-вирус, которая переименовывает папки c четными номерами 
    в ранее созданной папке dir, новые имена должны начинаться со строки name.
    """
    dir = r'C:\Code VS\python-2-2-cxZvezdochet'
    name = 'name'
    os.mkdir(os.path.join(r'C:\Code VS\python-2-2-cxZvezdochet'), 'dir')

    for item in (os.listdir + 1):
    
        new_name = f'{name}_{folder_number}'
        os.rename(os.path.join(dir, folder), os.path.join(dir, 'dir', new_name))

################################################################################

import sys


def t4(dir: str, text: str):
    """
    Напишите программу которая создает папку dir и записывает 
    текст text в файл answer.txt
    """

    dir = r'C:\Code VS\python-2-2-cxZvezdochet'
    os.mkdir(os.path.join(r'C:\Code VS\python-2-2-cxZvezdochet'), 'dir')

    arg1 = "text"
    arg2 = "answer.txt"

    with open(arg2, "w") as answer:

        answer.write(arg1)
