import csv
import re
from patterns_subs import pattern_name, pattern_phone, substitution_phone


def open_csv(csv_file: str):
    with open(csv_file) as file:
        rows = csv.reader(file, delimiter=',')
        contacts_list = list(rows)

        return contacts_list


def change_name(cont_list, pattern):
    for contact in cont_list:
        name_list = list(filter(None, [*pattern.split(contact[0]), *pattern.split(contact[1])]))
        if len(name_list) == 3:
            contact[0], contact[1], contact[2] = name_list[0], name_list[1], name_list[2]
        elif len(name_list) == 2:
            contact[0], contact[1] = name_list[0], name_list[1]
        else:
            contact[0] = name_list[0]


def change_number(cont_list, pattern, subs):
    for contact in cont_list:
        contact[5] = re.sub(pattern, subs, contact[5]).strip(' ')


def combining_duplicates(table):
    result_table = []
    group_list = []
    for key in table:
        if key[0:2] not in result_table:
            result_table.append(key[0:2])
            group_list.append([key[2:]])
        else:
            count = result_table.index(key[0:2])
            group_list[count].append(key[2:])

    for i, element in enumerate(group_list):
        if len(element) > 1:
            contact = list(zip(element[0], element[1]))
            for j, elem in enumerate(contact):
                if elem[0] == elem[1]:
                    contact[j] = elem[0]
                elif elem[0] == '':
                    contact[j] = elem[1]
                elif elem[1] == '':
                    contact[j] = elem[0]
            group_list[i] = contact
        else:
            group_list[i] = [item for i in element for item in i]

    for i, name in enumerate(result_table):
        result_table[i] = name + group_list[i]

    return result_table


def writer_csv(result: list):
    with open('phonebook.csv', 'w') as file:
        datawriter = csv.writer(file, delimiter=',')
        datawriter.writerows(result)


p_n = re.compile(pattern_name)
p_p = re.compile(pattern_phone)
s_p = substitution_phone

if __name__ == '__main__':
    contact_list = open_csv('phonebook_raw.csv')
    change_name(contact_list, p_n)
    change_number(contact_list, p_p, s_p)
    writer_csv(combining_duplicates(contact_list))
