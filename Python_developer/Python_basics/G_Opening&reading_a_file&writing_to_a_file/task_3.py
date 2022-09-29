import os


def merge_files():
    with os.scandir('task_3_files/') as list_files:
        dict_files = {}
        for file in list_files:
            with open(file, 'r') as file_obj:
                text = []
                text += file_obj.readlines()
                dict_files[file.name] = (len(text), text)
                dict_files = {k: dict_files[k] for k in sorted(dict_files, key=dict_files.get)}
        for key, value in dict_files.items():
            with open('task_3_merged_file.txt', 'a') as f:
                f.write(f'{key}\n{value[0]}\n{"".join(value[1])}\n')


merge_files()
