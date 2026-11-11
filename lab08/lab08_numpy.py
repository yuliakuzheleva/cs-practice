import numpy as np
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
unknown_table = np.full((2,3), -1)
identity = np.eye(3)
print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
    ])
print('Форма: ',temperatures.shape)
print('Измерения: ',temperatures.ndim)
print('Количество элементов: ',temperatures.size)
print('Вторая строка, третий столбец: ',temperatures[1, 2])
print('Первая строка: ',temperatures[0])
print('Последний столбец: ',temperatures[:, -1])
print('Первые две строки без первого столбца',temperatures[2:, 1:])
print('Цетральный фрагмент: ',temperatures[:2, 1:3])

matrix = np.arange(1, 26).reshape(5, 5)
task1 = matrix[:3, :]
print("Первые три строки: ", task1)
print("Shape:", task1.shape)
task2 = matrix[3:, :]
print("Последние две строки: ", task2)
print("Shape:", task2.shape)
task3 = matrix[:, :2]
print("Первые два столбца: ", task3)
print("Shape:", task3.shape)
task4 = matrix[1:4, 2:5]
print("Строки 1–3 и столбцы 2–4: ", task4)
print("Shape:", task4.shape)
task5 = matrix[3:5, 3:5]
print("Правый нижний блок 2x2: ", task5)
print("Shape:", task5.shape)

changed_hours = hours.copy()
changed_hours[2:4]= 99
changed_hours[::2]=-1
print(changed_hours)
print(hours)
#Создала копию, чтобы не изменять исходный массив
changed_matrix = matrix.copy()
changed_matrix[1,:]=0
changed_matrix[:,-1]=-1
changed_matrix[1:4, 1:4]=100
print('Исходная: ', matrix)
print('измененная: ', changed_matrix)

numbers =np.arange(12)
table = numbers.reshape(3,4)
transpored = table.T
print(numbers)
print(numbers.shape)
print(table)
print(table.shape)
print(transpored)
print(transpored.shape)
#reshape(5,3) вызовет ошибку потому что 5*3=15, а в исходном массиве только 12 элементов 



