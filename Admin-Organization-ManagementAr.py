import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from common_variables import mini_wait_time, wait_time, backup_time, username, password, cts_link
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome() 
driver.maximize_window() 
driver.get(cts_link) 
driver.implicitly_wait(backup_time) 

#highlight function to show the user where the automated script is clicking
def highlight(element):
    driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
    driver.execute_script("arguments[0].style.border = '2px solid red';", element)

    time.sleep(mini_wait_time)

    
    driver.execute_script("arguments[0].removeAttribute('style');", element)



# Login
username_field = driver.find_element(By.ID, 'Username')
password_field = driver.find_element(By.ID, 'Password')
submit_btn = driver.find_element(By.ID, 'btnSubmit')

# fill login form
highlight(username_field)
username_field.send_keys(username)
highlight(password_field)
password_field.send_keys(password)
highlight(submit_btn)
submit_btn.click()
time.sleep(wait_time)
time.sleep(wait_time)

#value of the btton needs to be updated after deployments
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'user-btn'))
)

    # Click on the profile icon
if elements:
        first_element = elements[0]
        first_element.click()
        
time.sleep(5)
admin_div = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/admin" and contains(@class, "profile-icons") and contains(@class, "profileIconsCustom")]'))
)

admin_div.click()
time.sleep(5)
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.v-card.v-card--link.v-sheet.theme--light'))
)

# Click the first element in the list (index 0, since indexing is 0-based)
if len(elements) > 0:
    elements[0].click()
else:
    print("No elements found")

time.sleep(3)
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button.v-icon.notranslate.v-treeview-node__toggle.v-icon--link.mdi.mdi-menu-down.theme--light'))
)

# Click the button
button.click()
time.sleep(3)
buttons = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.v-icon.notranslate.v-treeview-node__toggle.v-icon--link.mdi.mdi-menu-down.theme--light'))
)

# Click the first button in the list (index 0, since indexing is 0-based)
if len(buttons) > 1:
    buttons[1].click()
else:
    print("No buttons found")

time.sleep(3)
print('admin organization management test done successful')
driver.close()
driver.quit()