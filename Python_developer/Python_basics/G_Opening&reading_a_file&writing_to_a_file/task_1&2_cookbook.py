from pprint import pprint


def get_shop_list_by_dishes(dishes, person_count):
    with open('recipes.txt', 'r') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish = line.strip()
            ingredient_count = file_obj.readline()
            ingredient_list = []
            for ingredient in range(int(ingredient_count)):
                ingredient_details = file_obj.readline().strip()
                list_items = ingredient_details.split('|')
                dict_items = {'ingredient_name': list_items[0], 'quantity': list_items[1], 'measure': list_items[2]}
                ingredient_list.append(dict_items)
            file_obj.readline()

            cook_book[dish] = ingredient_list

    result = {}
    for dish in dishes:
        for dish_recipe in cook_book:
            if dish_recipe == dish:
                ingredient_list = cook_book.get(dish_recipe)
                for ingredient in ingredient_list:
                    if ingredient.get('ingredient_name') in result:
                        ingredient_name = ingredient.get('ingredient_name')
                        r_ingredient = result.get(ingredient_name)
                        r_ingredient['quantity'] = int(ingredient.get('quantity')) + int(r_ingredient.get('quantity'))
                    else:
                        result[ingredient.get('ingredient_name')] = \
                            {'measure': ingredient.get('measure'),
                             'quantity': (int(ingredient.get('quantity')) * person_count)}

    return result


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
