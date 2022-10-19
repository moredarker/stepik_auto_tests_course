import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    submit.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.ID, "input_value").text

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(x))

    send = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    send.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()