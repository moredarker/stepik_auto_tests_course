import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys('moredarker')

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys('ivanovich')

    email = browser.find_element(By.NAME, "email")
    email.send_keys('dm.kaftailov@gmail.com')

    folder = os.path.dirname(__file__)
    text = os.path.join(folder, "empty.txt")
    attach = browser.find_element(By.NAME, "file")
    attach.send_keys(text)

    submit = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    submit = submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()