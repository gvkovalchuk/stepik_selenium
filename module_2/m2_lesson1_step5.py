import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/math.html"
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x)
    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(y)
    checkbox = driver.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()
    radiobutton = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
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
