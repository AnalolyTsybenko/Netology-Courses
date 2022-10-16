from selenium import webdriver
from time import sleep
from config import EMAIL, PASS


def get_user_name(email: str) -> list:
    user_name = []
    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth/')
    assert 'Авторизация' in driver.title

    elem = driver.find_element(by='css selector', value='div.AuthLoginInputToggle-type')
    elem.click()
    elem = driver.find_element(by='id', value='passp-field-login')
    elem.send_keys(email)
    elem = driver.find_element(by='id', value='passp:sign-in')
    elem.click()
    elem = driver.find_element(by='id', value='passp-field-passwd')
    elem.send_keys(PASS)
    elem = driver.find_element(by='id', value='passp:sign-in')
    elem.click()
    sleep(5)
    elem_first = driver.find_element(by='css selector', value='div.personal-info__first')
    user_name.append(elem_first.text)
    elem_last = driver.find_element(by='css selector', value='div.personal-info__last')
    user_name.append(elem_last.text)
    driver.close()

    return user_name


if __name__ == '__main__':
    print(get_user_name(EMAIL))
