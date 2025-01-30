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
username_field.send_keys("majed")
highlight(password_field)
password_field.send_keys("P@$$w0rd@123")
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
delegation_div = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.col-3.profile-icons-container > a.profile-icons[href="/delegation"] > i.mdi.mdi-delegation'))
    )

delegation_div.click()
time.sleep(5)
try:
    element = driver.find_element(By.CSS_SELECTOR, "#sub-app > div.p-4.w-100.mr-4.delegation.v-card.v-sheet.theme--light > div.v-data-table.position-relative.white.flex-1.d-flex.overflow-auto.v-data-table--fixed-header.theme--light.result_available > div > table > tbody > tr > td:nth-child(1)")
    
    # Click the element
    element.click()
    # Locate the element that triggers the hover
    time.sleep(2)
    script = '''
    var button = document.querySelector("#sub-app > div.p-4.w-100.mr-4.delegation.v-card.v-sheet.theme--light > div.v-data-table.position-relative.white.flex-1.d-flex.overflow-auto.v-data-table--fixed-header.theme--light.result_available > div > table > tbody > tr > td.text-start > div > div:nth-child(2) > button");
    if (button) {
        button.click();
    } else {
        console.log("Button not found.");
    }
    '''
    driver.execute_script(script)
    time.sleep(2)
    button_xpath = '//button[@type="button" and @class="v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--default primary" and @style="width: 100px;"]'
    button = driver.find_element(By.XPATH, button_xpath)
    
    # Click the button element
    button.click()
    print("Button clicked successfully.")
    print("Element clicked successfully.")
    
    
except NoSuchElementException:
    print("Element not found.")
time.sleep(5)

icon_element = driver.find_element(By.CSS_SELECTOR, "i[data-v-32066f34]")

        # Click the icon element
icon_element.click()




time.sleep(5)
elements = driver.find_elements(By.CSS_SELECTOR, 'button.v-icon.notranslate.v-treeview-node__toggle.v-icon--link.mdi.mdi-menu-down.theme--light')


# Click on the first element if it exists
if elements:
    elements[1].click()
else:
    print("No elements found with the class 'v-treeview-node__label'")

time.sleep(3)
checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="checkbox" and @aria-checked="false" and @role="checkbox" and @value="16309-50065"]'))
)


# Click the checkbox
checkbox.click()
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div.dialog-body.white-container > div > div > div.dialog-footer.d-flex.align-items-center.justify-content-end.gap-3 > button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary'))
)

# Click the button using JavaScript
driver.execute_script("""
    document.querySelector("#app > div.v-dialog__content.v-dialog__content--active > div > div.dialog-body.white-container > div > div > div.dialog-footer.d-flex.align-items-center.justify-content-end.gap-3 > button.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary").click();
""")
time.sleep(3)
elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.multiselect__tags'))
)

# Click the second element in the list (index 1, since indexing is 0-based)
if len(elements) > 1:
    elements[1].click()
else:
    print("There are less than 2 elements found")
time.sleep(3)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'li#null-0.multiselect__element'))
)

# Click the element
element.click()
time.sleep(3)
# click outside
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.d-flex.align-items-center.gap-3.justify-content-between'))
)

# Click the element
element.click()
time.sleep(3)
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "primary") and contains(@class, "v-btn") and contains(@class, "v-btn--is-elevated") and contains(@class, "v-btn--has-bg") and contains(@class, "theme--light") and contains(@class, "v-size--default")]//span[contains(text(), "إضافة تفويض")]'))
)
button.click()

time.sleep(10)
print('Delegation test done successful')
driver.close()
driver.quit()