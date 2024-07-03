import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer = driver.find_element(By.ID, "answer")
    answer.send_keys(y)
    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = driver.find_element(By.ID, "robotsRule")
    driver.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
