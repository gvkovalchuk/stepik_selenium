from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    driver = webdriver.Chrome()
    driver.get(link)

    a = driver.find_element(By.CSS_SELECTOR, "h2 span:nth-child(2)").text
    b = driver.find_element(By.CSS_SELECTOR, "h2 span:last-child").text
    answer = int(a) + int(b)
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(answer))
    
    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
