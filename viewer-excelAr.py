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

#create button
try:
    create_button = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'menu-toggle-btn') and contains(@class, 'btn-add')]"))
    )
    highlight(create_button)
    create_button.click()
    time.sleep(3)
    print("Create button clicked successfully")
except Exception as e:
    print(f"Failed to click the create button: {e}")
try:
    menu_item = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, "//div[@tabindex='0' and @role='menuitem' and contains(@class, 'v-list-item--link')]"))
    )
    highlight(menu_item)
    menu_item.click()
    time.sleep(3)
    print("Menu item clicked successfully")
except TimeoutException:
    print("Menu item not found")


except Exception as e:
    print(f"Failed to click the outgoing icon: {e}")


time.sleep(3)


try:
    # Switch to the iframe by index
    driver.switch_to.frame(0)  
    print("Switched to iframe successfully by index.")
    


except Exception as e:
    print(f"Failed to switch to iframe by index: {e}")
#close notification
close_notification_btn = driver.find_element(By.CLASS_NAME, "ClosetblCanNotScan")
close_notification_btn.click()

time.sleep(3)

#driver.switch_to.default_content()


js_click_script = """
    const element = document.querySelector("#my-app123 > div > div > div.custom-col.col-lg-4.p-1.position-relative.bg-white.d-flex.h-100.overflow-auto > div > div.v-item-group.theme--light.v-expansion-panels.v-expansion-panels--focusable > div:nth-child(1) > button");
    if (element) {
        element.click();
    } else {
        console.error("Element not found.");
    }
    """
    
driver.execute_script(js_click_script)
print("Clicked the element successfully.")
time.sleep(3)
#path to the file being uploaded
file_path = os.path.abspath(r"C:\Users\s161391\Desktop\Automation\python selenium\DGE\Test Document Excel.xlsx")


file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')

    # Use JavaScript to make the element visible since the automation script can't see the file explorer window
driver.execute_script('arguments[0].style.display = "block";', file_input)

    # Send keys (file path) to the visible file input element
file_input.send_keys(file_path)    

#hide it after uploading the file
driver.execute_script('arguments[0].style.display = "none";', file_input)


    

time.sleep(5)
#click continue
buttonCont = driver.find_element(By.XPATH,"//button[@type='button' and contains(@class, 'btn-text')]")

    
driver.execute_script("arguments[0].click();", buttonCont)



time.sleep(15)
print('Viewer-excel by file test done successful')
driver.close()
driver.quit()