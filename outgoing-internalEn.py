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


driver = webdriver.Chrome() #open chrome
driver.maximize_window() #maximize window
driver.get(cts_link) #navigate to the website link
driver.implicitly_wait(backup_time) #wait for connection

def highlight(element):
    # Add the css class to the element
    driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)
    driver.execute_script("arguments[0].style.border = '2px solid red';", element)

    # wait
    time.sleep(mini_wait_time)

    # Remove the CSS class after the desired duration
    driver.execute_script("arguments[0].removeAttribute('style');", element)



# Login
# find elements
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


# outgoing section in the menu_item
try:
    # Explicitly wait for the element to be clickable
    outgoing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[3]"))
    )
    highlight(outgoing)
    # Once element is found, click on it
    outgoing.click()

except Exception as e:
    print("couldn't find outgoing in the menu",e)



# try:
#     menu_item = WebDriverWait(driver, wait_time).until(
#         EC.presence_of_element_located((By.XPATH, "//div[@data-v-3039c26d and @tabindex='0' and @role='menuitem' and @id='list-item-125']"))
#     )
#     highlight(menu_item)
#     menu_item.click()
#     time.sleep(3)
#     print("Menu item clicked successfully")


# except Exception as e:
#     print(f"Failed to click the outgoing icon: {e}")


#element.click()
time.sleep(3)

#close notification missing

# choose outgoing by template
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@tabindex='0' and @role='menuitem' and contains(@class, 'v-list-item') and text()='بواسطة قالب']"))
    )
    # Click the element
    element.click()

except Exception as e:
    print("couldn't find outgoing by template",e)

# choose the internal template
try:
    # Switch to the iframe by index
    driver.switch_to.frame(0)  # Replace 0 with the index of the iframe (if there are multiple frames)
    print("Switched to iframe successfully by index.")
    
    # Perform actions within the iframe
    # Example: interact with elements within the iframe
    # driver.find_element(By.ID, "element_id_within_iframe").click()

except Exception as e:
    print(f"Failed to switch to iframe by index: {e}")

#close notification
#close_notification_btn = driver.find_element(By.CLASS_NAME, "ClosetblCanNotScan")
#close_notification_btn.click()
    # Find all elements matching the CSS selector

time.sleep(5)
# Using CSS selector
driver.switch_to.default_content()

elementv = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/div/div[3]/div/div/div"))
    )

# Print the text content of the element
#print(f"Element text: {element.text}")

# Click on the element
elementv.click()
    
    # Optionally, you might want to wait for a new page load or some other action
time.sleep(5)

#continue after selecting a template
try:
    # Using XPath locator to find all matching elements
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'primary') and contains(@class, 'v-btn') and contains(@class, 'v-btn--is-elevated') and contains(@class, 'v-btn--has-bg') and contains(@class, 'theme--light') and contains(@class, 'v-size--default')]//span[text()='متابعة']"))
    )

    if elements:
        first_element = elements[0]
        first_element.click()
    else:
        print("No elements found matching the criteria.")

except TimeoutException:
    print("Timed out waiting for elements to be located.")
time.sleep(5)

#apply_button = WebDriverWait(driver, 10).until(
#        EC.element_to_be_clickable((By.CLASS_NAME, 'apply-button.text-end.inner-single-component'))
#    )
#click recipient
elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.v-icon.notranslate.mdi.mdi-user-add.theme--light'))
    )

if elements:
        elements[1].click()
        # Perform further actions with elements as needed


time.sleep(5)
checkboxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//input[@type="checkbox"]'))
    )

    # Check if there are at least two checkbox elements
if checkboxes and len(checkboxes) > 1:
        # Click the second checkbox element (index 1 since index starts from 0)
        checkboxes[3].click()
        print("Clicked the second checkbox element")
else:
        print("Not enough checkbox elements found")
time.sleep(3)

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


time.sleep(3)

#driver.switch_to.default_content()
#cc


time.sleep(5)
#tags
#elements = WebDriverWait(driver, 10).until(
#        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.v-icon.notranslate.mdi.mdi-user-add.theme--light'))
#   )

#if elements:
#       driver.execute_script("arguments[0].scrollIntoView();", elements[2])
#
#       elements[2].click()
#       # Perform further actions with elements as needed

#input_element = driver.find_element(By.XPATH, "//div[@class='v-input__slot']/div[@class='v-text-field__slot']/input[@id='input-209']")

# Clear the input field if it has any pre-filled data
#input_element.clear()

# Enter the data '150' into the input field
#input_element.send_keys('150')
time.sleep(3)
# textarea_element = driver.find_element(By.XPATH, "//div[@class='v-input__slot']//div[@class='v-text-field__slot']/textarea[@id='input-369']")

# # Scroll the textarea into view
# driver.execute_script("arguments[0].scrollIntoView({ block: 'center' });", textarea_element)

# # Clear the textarea if it has any pre-filled data
# textarea_element.clear()

# # Enter the data 'automated testing subject' into the textarea
# textarea_element.send_keys('automated testing subject')

# Subject:
try:
    element_in_subject_to_scroll = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[8]/div[1]'))
    )
    
    # Scroll into view and center the element
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element_in_subject_to_scroll)
    
    # Wait for the element containing the input to be present in the DOM
    container_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#LetterDetails_DivId > div.row > div:nth-child(8) > div.v-input.light-bg.subject-txt.v-textarea.theme--light.v-text-field.v-text-field--is-booted.v-text-field--placeholder'))
    )
    
    # Highlight the container element (optional)
    highlight(container_element)

    # Find the input element within the container
    input_element = container_element.find_element(By.TAG_NAME, 'textarea')
    
    # Interact with the input element (e.g., send keys)
    input_element.send_keys("Automated test")

except Exception as e:
    print("couldn't find the subject", e)

time.sleep(3)

# Locate the input element using its class name
buttons = driver.find_elements(By.CSS_SELECTOR, 'button.dgs-new-button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default')

# Click the first button if found
if buttons:
    driver.execute_script("arguments[0].scrollIntoView();", buttons[2])

    buttons[2].click()
else:
    print("Button not found")


time.sleep(2)

#click signee
elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.v-icon.notranslate.mdi.mdi-user-add.theme--light'))
    )

if elements:
        elements[3].click()
        


time.sleep(4)
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="v-treeview-node__root"]//span[text()="dgs"]/ancestor::div[@class="v-treeview-node__root"]//button[@class="v-icon notranslate v-treeview-node__toggle v-icon--link mdi mdi-menu-down theme--light"]'))
)

# Click the button
button.click()

time.sleep(3)


    # Wait for the checkbox element with specific value to be present
checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="checkbox" and @aria-checked="false" and @role="checkbox" and @value="1-1"]'))
)



    # Click the checkbox
checkbox.click()
print("Clicked the checkbox with value '1-1'")


time.sleep(3)
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

time.sleep(3)

#save
button_element = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'v-btn--text') and contains(@class, 'primary--text')]")

# Scroll the button into view, centering it in the viewport

# Click the button
button_element.click()
time.sleep(3)

try:
    # Find all elements matching the CSS selector
    buttons = driver.find_elements(By.CSS_SELECTOR, 'button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary')

    # Print the count of elements found
    if len(buttons) >= 3:
        # Click the third button (index 2)
        buttons[2].click()
        print("Clicked the third button")
    else:
        print("Less than 3 buttons found")

except Exception as e:
    print(f"Error: {e}")

time.sleep(5)
print('outgoing test done successful')
driver.close()
driver.quit()