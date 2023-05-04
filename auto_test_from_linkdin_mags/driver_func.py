


from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Import variables from main.py file
from vars import link_un, link_pw, path, task

# Initialize webdriver

# driver = webdriver.Chrome()

# Function to write post and tag users to write post with the output...
def write_post(func):
    global path
    
    # Wait for page to load
    time.sleep(30)
    
    # Get list of usernames from directory
    import os
    users = os.scandir(path)
    usernames = [user.name for user in users]
    
    # Find all paragraph elements
    elements = driver.find_elements(By.TAG_NAME, "p")
    for elem in elements:
        try:
            # Tag all usernames in post
            for user in usernames:
                elem.click()
                elem.send_keys("@"+user[:10],Keys.ENTER)
                time.sleep(2)
                
            # Call provided function with post text as argument
            func(elem.text) 
            time.sleep(30)
        except:
            print("error")

# Function to get list of usernames from chat
def get_users(elements):
    
    global driver

    users = []
    for i in elements:
    
        try:
            # Extract username from element
            username = i.text
            
            # Add username to list
            if username:
                users+=[username]
                print(username)
            else:
                print("bad!"+username)
        except:
            print("error")
    return users

# Function to get messages and timestamps from chat
def get_msg_text(elements):
    global driver, path, task
    users = []
    for i in elements:
    
        try:
            
            # Extract username from element and click on it
            username = i.text
            i.click()
            time.sleep(2)
            
            # Get latest message element and timestamp element
            elem = driver.find_elements(By.CLASS_NAME, "msg-s-event-listitem__body")[-1]
            timeEl = driver.find_elements(By.CLASS_NAME, "msg-s-message-group__timestamp")[-1]
            
            # Write timestamp to file
            if timeEl.text:
                with open(f"{path}\\{username}\\{task}-time.txt", "x") as f:
                    f.write(timeEl.text)
            
            # Write message to file
            msg = elem.text
            with open(f"{path}\\{username}\\{task}.py", "x") as f:
                f.write(msg.replace("space"," "))

        except:
            print("error")

# Function to get list of messages and call provided function
def see_last_msgs_and(func):
    global driver,time
    
    # Wait for page to load
    time.sleep(40)

    # Scroll to bottom of chat until messages from recent months are visible
    elem = driver.find_elements(By.CSS_SELECTOR, 'ul')[1]
    timeEl = elem.find_elements(By.CSS_SELECTOR, 'time')[-1]
    while  not any ( month in timeEl.text for month in ["Mar","Nov","Feb","Oct","Aug"]):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", elem )
        time.sleep(2)
        timeEl = elem.find_elements(By.CSS_SELECTOR, 'time')[-1]

    # Find all header elements
    elements = driver.find_elements(By.CSS_SELECTOR, 'h3')
   
    # Call provided function with header elements as argument
    return func(elements)

# Function to login and call provided functions
def login_and(*func):
    global driver
    driver = webdriver.Chrome()

    # Navigate to login page and enter

    driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fmessaging%2F&fromSignIn=true&trk=cold_join_sign_in")
    time.sleep(3)
    elem = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
    elem.send_keys(link_un)
    elem = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
    elem.send_keys(link_pw)
    time.sleep(1)

    elem.send_keys(Keys.RETURN)
    time.sleep(5)

    return func[0](func[1]) # continue with to steps.

    
    
    
    

    

