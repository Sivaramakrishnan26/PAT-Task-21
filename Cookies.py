from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path of the Chrome Webdriver
chrome_driver_path = 'E://SIVARAMAKRISHNAN T//GUVI//Selenium Webdrivers//WebDrivers//chromedriver.exe'

# Setup the service object
chrome_service = Service(chrome_driver_path)

# Initialize the Chrome Webdriver
driver = webdriver.Chrome(service=chrome_service)

# Maximize the Browser Window
driver.maximize_window()

# Open a website
driver.get("https://www.saucedemo.com/")

# Print the cookies before login
Cookie_Before_Login = driver.get_cookies()

# Check whether the cookies are available before login
if Cookie_Before_Login:
    print("Cookie Before Login:", Cookie_Before_Login)
else:
    print("Cookie Before Login: No Cookies available before login.")
time.sleep(2)

# Perform the Actions
User_Name = driver.find_element(By.ID, "user-name")
User_Name.send_keys("standard_user")
User_Name.send_keys(Keys.RETURN)

Password = driver.find_element(By.ID, "password")
Password.send_keys("secret_sauce")
Password.send_keys(Keys.RETURN)

Login = driver.find_element(By.ID, "login-button")
Login.click()

# Print the cookies after login
Cookie_After_Login = driver.get_cookies()

# Check whether the cookies are available after login
if Cookie_After_Login:
    print("Cookie After Login:", Cookie_After_Login)
else:
    print("Cookie After Login: No Cookies available after login.")

# Initialize the driver to wait for 10 seconds until the expected condition is satisfied
wait = WebDriverWait(driver, 10)

# Perform the Actions
Menu_Button = wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
Menu_Button.click()

Logout = wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
Logout.click()
time.sleep(2)

# Print the cookies after login
Cookie_After_Logout = driver.get_cookies()

# Check whether the cookies are available after logout
if Cookie_After_Logout:
    print("Cookie After Logout:", Cookie_After_Logout)
else:
    print("Cookie After Logout: No Cookies available after logout.")

# Close the webdriver
driver.quit()
