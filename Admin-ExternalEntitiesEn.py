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
username_field.send_keys("admin")
highlight(password_field)
password_field.send_keys("1")
highlight(submit_btn)
submit_btn.click()
time.sleep(wait_time)
time.sleep(wait_time)
#Switch Language
buttons = driver.find_elements(By.CSS_SELECTOR, 'button.dgs-new-button-inner.v-btn--is-elevated.v-btn--has-bg')

# Check if there are at least two buttons
if len(buttons) > 1:
    # Click on the second button (index 1 since it's zero-based)
    buttons[1].click()
else:
    print("There are less than two buttons on the page")

# Wait a few seconds to observe the result (optional)
time.sleep(5)
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

elements[4].click()
time.sleep(3)
treeview_node_contents = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.v-treeview-node__content'))
)

# Get the first element from the list
first_treeview_node_content = treeview_node_contents[0]

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView(true);", first_treeview_node_content)

# Right-click on the first element
action = ActionChains(driver)
action.context_click(first_treeview_node_content).perform()

time.sleep(3)
specific_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='menuitem' and contains(@class, 'v-list-item') and contains(., 'عرض المستخدمين')]"))
)

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView(true);", specific_element)

# Click on the element
specific_element.click()
time.sleep(5)

print('admin external entities test done successful')
driver.close()
driver.quit()