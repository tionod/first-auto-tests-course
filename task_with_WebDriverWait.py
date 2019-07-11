from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def fn(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

optimal_price = '10000 RUR'
rent_button = browser.find_element_by_id('book')

if WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), optimal_price)
    ):
    rent_button.click()

browser.implicitly_wait(5)
x = int(browser.find_element_by_id('input_value').text)
result = fn(x)

f = browser.find_element_by_id('answer')
f.send_keys(result)

end = browser.find_element_by_id("solve")
end.click()

time.sleep(5)
alert = browser.switch_to.alert
alert.accept()
browser.close()
