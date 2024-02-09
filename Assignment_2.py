import time
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

url = "https://www.saucedemo.com"

driver = webdriver.Chrome(options=options)
driver.get(url)

# Maximize the window
driver.maximize_window()

Password = "secret_sauce"

#LOCKED_OUT_USER
Usernamelocked_out_user = "locked_out_user"
userlocked_out_user = driver.find_element(By.ID, "user-name").send_keys(Usernamelocked_out_user)
driver.find_element(By.ID, "password").send_keys(Password)
driver.find_element(By.NAME, "login-button").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container h3'))).text

#STANDART_USER
Usernamestandard_user = "standard_user"
driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, "user-name").send_keys(Usernamestandard_user)
driver.find_element(By.NAME, "login-button").click()
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]').click()

# Add product to cart
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button').click()

# Go to the cart
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a').click()
time.sleep(2)

# Proceed to checkout
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/button[2]').click()

# Fill shipping information
driver.find_element(By.ID, 'first-name').send_keys('Test')
driver.find_element(By.ID, 'last-name').send_keys('online1')
driver.find_element(By.ID, 'postal-code').send_keys('12341')
driver.find_element(By.ID, 'continue').click()
time.sleep(2)

# Click Finish
driver.find_element(By.ID, 'finish').click()
time.sleep(2)

# Verify order confirmation
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header'))).text
time.sleep(2)

# Back to Home
driver.find_element(By.ID, 'back-to-products').click()

# Add product to cart
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button').click()

#Logout
driver.find_element(By.ID, 'react-burger-menu-btn').click()
time.sleep(2)
driver.find_element(By.ID, 'logout_sidebar_link').click()

#PROBLEM_USER
Usernameproblem_user= "problem_user"
driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, "user-name").send_keys(Usernameproblem_user)
driver.find_element(By.ID, "password").send_keys(Password)
driver.find_element(By.NAME, "login-button").click()
time.sleep(2)

driver.find_element(By.ID, 'remove-sauce-labs-backpack').click()

if WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'remove-sauce-labs-backpack'))).is_displayed():
    #Logout
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(2)
    driver.find_element(By.ID, 'logout_sidebar_link').click()

#ERROR_USER
Usernameerror_user = "error_user"
driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, "user-name").send_keys(Usernameerror_user)
driver.find_element(By.ID, "password").send_keys(Password)
driver.find_element(By.NAME, "login-button").click()
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]').click()

# Add product to cart
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button').click()

# Go to the cart
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a').click()
time.sleep(2)

# Proceed to checkout
driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/button[2]').click()

# Fill shipping information
driver.find_element(By.ID, 'first-name').send_keys('Test')
driver.find_element(By.ID, 'last-name').send_keys('online1')
driver.find_element(By.ID, 'postal-code').send_keys('12341')
driver.find_element(By.ID, 'continue').click()

# Click Finish
driver.find_element(By.ID, 'finish').click()

if WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'finish'))).is_displayed():
    #Logout
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(2)
    driver.find_element(By.ID, 'logout_sidebar_link').click()