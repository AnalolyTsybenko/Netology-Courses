# Task_1

side_length_square = int(input('Введите длину стороны квадрата: '))

print()
print('Вывод:')
print(f'Периметр: {side_length_square * 4}')
print(f'Площадь: {side_length_square ** 2}', end='\n\n')

rectangle_length = int(input('Введите длину прямоугольника: '))
rectangle_width = int(input('Введите ширину прямоугольника: '))

print()
print('Вывод:')
print(f'Периметр: {2 * (rectangle_width + rectangle_length)}')
print(f'Площадь: {rectangle_width * rectangle_length}', end='\n\n')


# Task_2

salary_per_month = int(input('Введите заработную плату в месяц: '))
what_percentage_of_mortgage = int(input('Введите, какой процент(%) уходит на ипотеку: '))
what_percentage_of_life = int(input('Введите, какой процент(%) уходит на жизнь: '))

print()
print('Вывод:')
print(f'На ипотеку было потрачено: {int(((salary_per_month * what_percentage_of_mortgage) / 100) * 12)} рублей')
print(f'Было накоплено: {int(salary_per_month * 12 - (((salary_per_month * what_percentage_of_mortgage) / 100) * 12 + ((salary_per_month * what_percentage_of_life) / 100) * 12))} рублей')


# Task_3

delimiter = input('Введите символ для разделения задач: ')
print()
print(delimiter * (side_length_square * 4 + rectangle_width * rectangle_length), end='\n\n')
