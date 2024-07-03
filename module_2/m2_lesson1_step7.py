import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    driver = webdriver.Chrome()
    driver.get(link)

    treasure = driver.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = driver.find_element(By.ID, "robotsRule")
    radiobutton.click()
    

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
