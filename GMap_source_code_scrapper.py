'''
This code scrapes the source code of google maps url using selenium 
while going to every page using the next button and dumps it to the
output console.
'''

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/maps/search/medical+shops+in+varanasi/');
time.sleep(10)

button = driver.find_elements_by_xpath('//*[@id=\"n7lv7yjyC35__section-pagination-button-next\"]/span')[0]

while(True):
    try:
        print(driver.page_source, "\n=======================================\n")
        button.click()
        time.sleep(2)
    except:
        print('---Finished---')
        break

driver.quit()
