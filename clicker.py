from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import time

# Create options for Chrome
chrome_options = ChromeOptions()

# Disable notifications
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Launch the Chrome browser
driver = Chrome(options=chrome_options)

driver.get('http://127.0.0.1:8080')

print('Bot has enetered chat.')

try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i1"))
    )
finally:
	print('Found requested element')

	button.click()

	print('Clicked the requested element')

	driver.quit()

	print('Bot has exited chat.')



# time.sleep(2)
# button = driver.find_element(By.ID, "i1")
# time.sleep(3)













