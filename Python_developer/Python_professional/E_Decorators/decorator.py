from datetime import datetime


def logger(path):
    def logger_(some_function):
        def new_function(*args, **kwargs):
            date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            name = some_function.__name__
            args_ = args
            result = some_function(*args, **kwargs)
            with open(path + '/log.txt', 'a') as file:
                file.write(f'{date} | {name} | {args_} | {result}\n')
            return result
        return new_function
    return logger_
