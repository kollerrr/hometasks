import numpy as np


"""Напишите функцию, возвращающую нулевой вектор размера n 
с i-ым элементом равным 1"""
def task1(n, i):
        
        vector = np.zeros(n)
        vector[i] = 1
        return vector

"""Напишите функцию, возвращающую вектор значений от a до b"""
def task2(a, b):

    if a > b:
        vector = np.arrange(b, a)[::-1]
    else:   
        vector = np.arange(a,b)
    return vector


"""Напишите функцию, возвращающую матрицу размера n х n, заполненную числами от 0 до n^2 - 1"""
def task3(n):

    matrix = np.arange(0, n**2).reshape(n, n)
    return matrix



"""Напишите функцию, возвращающую индексы ненулевых элементов из вектора v"""
def task4(v):

    indexes = []
    for i in range(len(v)):
        if v[i] != 0:
            indexes.append(i)
    return(indexes)


"""Напишите функцию, возвращающую случайную матрицу размера n х n x n"""
def task5(n):

    random_matrix = np.random.random((n, n, n))
    return random_matrix


"""Напишите функцию, меняющую знак на противоположный у элементов, лежащих в диапазоне от a до b в векторе v"""
def task6(v, a, b):

    for i in range(len(v)):
        if a <= v[i] <= b:
            v[i] *= -1


"""Напишите функцию, возвращающую вектор, состоящий из элементов, присутствующих в обоих векторах"""
def task7(v1, v2):

    vector = [elem for elem in v1 if elem in v2]
    return vector


"""Напишите функцию, возвращающую вектор дат, соответствующих месяцу m и году y"""
def task8(m, y):

    date1 = datetime(y, m, 1) 
    days_in_month = 31 if m in {1, 3, 5, 7, 8, 10, 12} else 30
    if m == 2:
        days_in_month = 29 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 28

    vector_of_dates = [date1 + timedelta(days=i) for i in range(days_in_month)]
    
    return vector_of_dates