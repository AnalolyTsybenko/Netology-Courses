# Task_1

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

key_not_russia_visit = []
counter = 0

for not_russia in geo_logs:
    for country in not_russia:
        not_russian = not_russia.get(country)
        if 'Россия' not in not_russian:
            key_not_russia_visit.append(counter)
        counter += 1

for key in key_not_russia_visit[::-1]:
    del geo_logs[key]

print(geo_logs)


# Task_2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

ids_list_list = list(ids.values())
ids_list = list(set(sum(ids_list_list, [])))
print(sorted(ids_list))


# Task_3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'один два три четыре',
    'один два три четыре пять'
    ]

base = {}
for query in queries:
    words = len(query.split())
    if words in base:
        base[words] += 1
    else:
        base[words] = 1

for key, value in base.items():
    percent = float((value / len(queries)))
    print(f'Поисковых запросов из {key} слов: {percent:.1%}')


# Task_4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

list_tuple = list(stats.items())
tuple_max_value = max(list_tuple, key=lambda tuple_value: tuple_value[1])
print(tuple_max_value[0])
