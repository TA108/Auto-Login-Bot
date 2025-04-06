import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def startBot(username, password, url):
    # Set the path to your manually downloaded ChromeDriver
    chrome_driver_path = r"D:\Chrome Driver\chromedriver-win64\chromedriver.exe"
    
    # Set the path to your Chrome browser executable 
    chrome_binary_path = r"D:\Chrome Driver\chrome-win64\chrome.exe"
    os.environ["webdriver.chrome.driver"] = chrome_driver_path
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path
    
    # Create a Service object with the path to ChromeDriver
    service = Service(chrome_driver_path)
    
    # Initialize the WebDriver with the Service object and Chrome options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open the URL in Chrome
    driver.get(url)
    
    # Find the username and password field and enter them
    driver.find_element(By.NAME, "username_field_name").send_keys(username)
    driver.find_element(By.NAME, "password_field_name").send_keys(password)  
    
    # Find the login button and click it
    driver.find_element(By.CSS_SELECTOR, "login_button_css_selector").click() 
    time.sleep(5)

    #Check if login was successful
    try:
        dashboard_element = driver.find_element(By.ID, "dashboard_element_id")
        print("Login successful!")
    except:
        print("Login failed.")
        
    driver.quit()

username = "********"
password = "****"
url = "www.****.com"

startBot(username, password, url)
