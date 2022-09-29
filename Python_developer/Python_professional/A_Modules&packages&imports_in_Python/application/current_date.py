import datetime as dt


def get_today():
    cur_date = dt.datetime.today().strftime('%d.%m.%Yг. %H:%M')
    return cur_date
