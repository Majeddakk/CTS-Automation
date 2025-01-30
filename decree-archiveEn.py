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

# Click on decree
try:
    # Explicitly wait for the element to be clickable
    decree = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[@tabindex="0" and @role="menuitem" and contains(@class, "v-list-item") and contains(@class, "v-list-item--link") and contains(@class, "theme--light")])[3]'))
)
    highlight(decree)
    # Once element is found, click on it
    decree.click()

except Exception as e:
    print("couldn't find decree in the menu",e)

# choose a decree template
try:
    # Switch to the iframe by index
    driver.switch_to.frame(0)  # Replace 0 with the index of the iframe (if there are multiple frames)
    print("Switched to iframe successfully by index.")
    
    # Perform actions within the iframe
    # Example: interact with elements within the iframe
    # driver.find_element(By.ID, "element_id_within_iframe").click()

except Exception as e:
    print(f"Failed to switch to iframe by index: {e}")

time.sleep(5)

# Using CSS selector, select the decree template
driver.switch_to.default_content()

decree_template = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/div/div[3]/div/div/div"))
    )

# Click on the element
decree_template.click()

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
time.sleep(10)

# Fill in the designated person
# Fill in the cc
# tags
# tags = WebDriverWait(driver, 10).until(
#     #    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.v-icon.notranslate.mdi.mdi-user-add.theme--light'))
#  EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#LetterDetails_DivId > div.row > div:nth-child(7) > div > div.multiselect__tags'))
    
#   )
# tags.send
# #highlight(tags)
# if tags:
#     #   driver.execute_script("arguments[0].scrollIntoView();", tags[2])

#       tags[1].click()
#       # Perform further actions with elements as needed

# filing plan
# classification plan
# attachments
# notes
# linked mails
# fill in the subject:
try:
    # Wait for the element to be present in the DOM
    element_to_scroll = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[8]'))
    )
    
    # Scroll into view and center the element
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element_to_scroll)
    
    
    # Wait for the textarea element to be present in the DOM
    textarea_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[8]//textarea'))
    )
    
    # Highlight the textarea element (optional)
    highlight(textarea_element)

    # Interact with the textarea element (e.g., send keys)
    textarea_element.send_keys("Automated test")

except Exception as e:
    print("Couldn't find or interact with the element:", e)

time.sleep(3)

#click on save button:
button_element = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'v-btn--text') and contains(@class, 'primary--text')]")

# Scroll the button into view, centering it in the viewport

# Click the button
button_element.click()
time.sleep(3)


archive_icon_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "i.v-icon.notranslate.mdi.mdi-archive-tick.theme--light"))
    )
    # Click the <i> element
archive_icon_element.click()
time.sleep(3)
textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea#input-478"))
    )
    # Fill the <textarea> with the specified text
textarea.send_keys("archive test")
time.sleep(3)
driver.execute_script("""
        var button = document.querySelector("#app > div:nth-child(6) > div > div > div.v-card__actions.gap-2.sticky-actions > button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary > span");
        if (button) {
            button.click();
        } else {
            console.log('Button not found');
        }
    """)

time.sleep(3)



print('decree-archive test done successfully')
driver.close()
driver.quit()