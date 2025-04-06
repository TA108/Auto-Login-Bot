import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def startBot(username, password, url):
    chrome_driver_path = r".\chromedriver-win64\chromedriver.exe"
    chrome_binary_path = r".\chrome-win64\chrome.exe"
    
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    chrome_options.add_argument("--disable-dev-shm-usage")
        
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open the URL in Chrome
    driver.get(url)
    
    # Find the username and password field and enter them
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)  
    
    # Find the login button and click it
    driver.find_element(By.ID, "submit").click() 
    time.sleep(5)

    #Check if login was successful
    try:
        dashboard_element = driver.find_element(By.CLASS_NAME, "post-title")
        if "Logged In Successfully" in dashboard_element.text:
                print("Login successful!!!")
        else:
            print("Login failed: Unexpected message.")
    except  Exception as e:
        print(f"Login failed: {e}")
    
    driver.quit()

username = "student"
password = "Password123"
url = "https://practicetestautomation.com/practice-test-login/"

startBot(username, password, url)