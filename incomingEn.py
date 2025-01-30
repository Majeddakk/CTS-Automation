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
file_path = os.path.abspath(r"C:\Users\s161391\Desktop\Automation\python selenium\DGE\dummy.pdf")


file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')

    # Use JavaScript to make the element visible since the automation script can't see the file explorer window
driver.execute_script('arguments[0].style.display = "block";', file_input)

    # Send keys (file path) to the visible file input element
file_input.send_keys(file_path)    

#hide it after uploading the file
driver.execute_script('arguments[0].style.display = "none";', file_input)


    

time.sleep(3)
#click continue
buttonCont = driver.find_element(By.XPATH,"//button[@type='button' and contains(@class, 'btn-text')]")

    
driver.execute_script("arguments[0].click();", buttonCont)



time.sleep(5)
driver.switch_to.default_content()


elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.v-icon.notranslate.mdi.mdi-user-add.theme--light'))
    )

if elements:
        elements[0].click()
        # Perform further actions with elements as needed


time.sleep(5)
checkboxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//input[@type="checkbox"]'))
    )

    # Check if there are at least two checkbox elements
if checkboxes and len(checkboxes) > 1:
        # Click the second checkbox element (index 1 since index starts from 0)
        checkboxes[1].click()
        print("Clicked the second checkbox element")
else:
        print("Not enough checkbox elements found")
time.sleep(5)

buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary'))
    )

    # Check if there are at least two button elements
if buttons and len(buttons) > 1:
        # Click the second button element (index 1 since index starts from 0)
        buttons[1].click()
        print("Clicked the second button element")
else:
        print("Not enough button elements found")

#driver.switch_to.default_content()
#cc


time.sleep(5)
#tags
#elements = WebDriverWait(driver, 10).until(
#        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.v-icon.notranslate.mdi.mdi-user-add.theme--light'))
#   )

# Get document id:
try:
    # Wait for the specified element to be present in the DOM
    documentid_container_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div[1]'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", documentid_container_element)
    # Highlight the container element (optional)
    highlight(documentid_container_element)
    
    # Find the input element within the container
    input_element = documentid_container_element.find_element(By.TAG_NAME, 'input')

    # Highlight the input element (optional)
    highlight(input_element)

    # Clear the input element (optional, if needed)
    input_element.clear()

    # Interact with the input element (e.g., send keys)
    input_element.send_keys("151")

except Exception as e:
    print("couldn't find the input element or perform the action", e)

time.sleep(3)

# Subject
try:
    # Wait for the parent div to be present in the DOM
    parent_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[8]'))
    )

    # Scroll the parent div into view
    driver.execute_script("arguments[0].scrollIntoView({ block: 'center' });", parent_div)

    # Find the textarea within the parent div
    textarea = parent_div.find_element(By.CSS_SELECTOR, 'textarea')

    # Highlight the textarea element (optional)
    highlight(textarea)

    # Scroll the textarea element into view (optional)
    driver.execute_script("arguments[0].scrollIntoView({ block: 'center' });", textarea)

    # Fill the textarea with the desired text
    textarea.send_keys("Automated Test")

except Exception as e:
    print(e)
time.sleep(3)


#save
button_element = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'v-btn--text') and contains(@class, 'primary--text')]")

# Scroll the button into view, centering it in the viewport

# Click the button
button_element.click()
time.sleep(5)
print('incoming by file test done successful')
driver.close()
driver.quit()