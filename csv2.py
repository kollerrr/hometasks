
'''
Найти минимальную разницу голов

Напишите функцию, которая принимает на вход имя файла и обрабатывает содержимое 
файла CSV. Содержимым будет турнирная таблица английской Премьер-лиги по итогам 
сезона. Ваша программа должна определить, какая команда имела наименьшую разницу
голов в этом сезоне.

Первая строка CSV-файла будет представлять собой заголовки столбцов, каждая 
последующая строка будет отображать данные по одной команде:

Team,Games,Wins,Losses,Draws,Goals For,Goals Against
Arsenal,38,26,9,3,79,36

Столбцы «Goals For» и «Goals Against» содержат общее количество голов, 
забитых за и против каждой команды в этом сезоне. (Итак, «Арсенал» забил 
79 голов, а в их ворота было забито 36 голов.)

Напишите программу, которая считывает файл, а затем выводит название команды с 
наименьшей разницей в числах «За» и «Против». 
'''

'''
Найти минимальную разницу голов

Напишите программу, которая принимает на вход имя файла и обрабатывает содержимое 
файла CSV. Содержимым будет турнирная таблица английской Премьер-лиги по итогам 
сезона. Ваша программа должна определить, какая команда имела наименьшую разницу
голов в этом сезоне.

Первая строка CSV-файла будет представлять собой заголовки столбцов, каждая 
последующая строка будет отображать данные по одной команде:

Team,Games,Wins,Losses,Draws,Goals For,Goals Against
Arsenal,38,26,9,3,79,36

Столбцы «Goals For» и «Goals Against» содержат общее количество голов, 
забитых за и против каждой команды в этом сезоне. (Итак, «Арсенал» забил 
79 голов, а в их ворота было забито 36 голов.)

Напишите программу, которая считывает файл, а затем выводит название команды с 
наименьшей разницей в числах «За» и «Против». 
'''

import csv

'''
Напишите функцию parse_next_line, принимающую имя файла и возвращающую следующую
непрочитанную строку из этого файла
'''
def parse_next_line(csv_file): # Генератор
    for row in csv.DictReader(csv_file):
        yield row
        


'''
Напишите функцию get_name_and_diff, которая принимает на вход словарь с данными
о команде и возвращает название команды и разницу в голах «За» и «Против»
'''
def get_name_and_diff(team_stats):
    
    diff = int(team_stats['Goals For'] - team_stats['Goals Against'])
    return team_stats['Team'], abs(diff)


'''
Напишите функцию get_min_score_difference, которая принимает на вход имя файла
и возвращает название команды с наименьшей разницей в голах
'''
def get_min_score_difference(filename):
    with open (filename, newline='') as f:
        # reader = csv.DictReader(f, delimiter = ',')
        min_diff = float('inf')
        min_team = None
        for row in parse_next_line(f):
            team, diff = get_name_and_diff(row)
            if dif < min_diff:
                min_diff = diff
                min_team = team 
    return min_team, min_diff