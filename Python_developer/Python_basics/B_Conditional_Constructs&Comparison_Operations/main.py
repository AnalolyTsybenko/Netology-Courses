# Task_1

print('\nДобро пожаловать в ипотечный калькулятор!')
print('Для расчета процентной ставки, введите запрашиваемые данные.', end='\n\n')

base_percent = float(10)
discount_amount_of_children = float(1)
discount_payroll_project = float(0.5)
discount_insurance = float(1.5)

client_region = input('Напишите Ваш регион: ')
amount_of_children = int(input('Напишите сколько у Вас детей: '))
payroll_project = input('У Вас есть зарплатный проект в нашем банке? (Да/Нет): ')
insurance = input('Вы будете оформлять страхование? (Да/Нет): ')

if client_region != 'Дальний Восток':
    if amount_of_children > 3:
        base_percent -= discount_amount_of_children
    if payroll_project == 'Да':
        base_percent -= discount_payroll_project
    if insurance == 'Да':
        base_percent -= discount_insurance

    print(f'\nВаша ставка {base_percent / 100:.1%}')

else:
    base_percent = float(2)
    if insurance == 'Да':
        base_percent -= discount_insurance
    else:
        if amount_of_children > 3:
            base_percent -= discount_amount_of_children
        if payroll_project == 'Да':
            base_percent -= discount_payroll_project

    print(f'\nВаша ставка {base_percent / 100:.1%}')

# Task_2

month = input('Введите месяц: ')
number = int(input('Введите число: '))

signs = {"март": (21, "Рыбы", "Овен"), "апрель": (21, "Овен", "Телец"), "май": (22, "Телец", "Близнецы"),
         "июнь": (22, "Близнецы", "Рак"), "июль": (23, "Рак", "Лев"), "август": (24, "Лев", "Дева"),
         "сентябрь": (24, "Дева", "Весы"), "октябрь": (24, "Весы", "Скорпион"),
         "ноябрь": (23, "Скорпион", "Стрелец"), "декабрь": (23, "Стрелец", "Козерог"),
         "январь": (21, "Козерог", "Водолей"), "февраль": (20, "Водолей", "Рыбы")}
if number >= signs[month][0]:
    print(signs[month][2])
else:
    print(signs[month][1])
