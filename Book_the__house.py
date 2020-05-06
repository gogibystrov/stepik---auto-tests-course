import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

flag = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
if(flag == True):
    button = browser.find_element_by_id("book").click()

x = int(browser.find_element_by_id("input_value").text)
answer = browser.find_element_by_id("answer").send_keys(calc(x))

button2 = browser.find_element_by_id("solve").click()

print("Ho-ho, try to catch this, GIT!")

