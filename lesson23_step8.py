from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)



    pricewait = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    browser.find_element(By.ID, "book").click()
    
    
    input1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    input2 = browser.find_element(By.ID, "input_value").text
    rez = math.log(abs(12*math.sin(int(input2))))
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(str(rez))
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

