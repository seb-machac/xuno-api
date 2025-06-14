"""
Filename: Get_Image.py
Author: Seb Machac
Purpose: Sets your Xuno timetable as your windows background
Revision: 14 June 2025
"""

#All the imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Set up all the configurations
options = Options()
options.add_argument("--headless")                                                          #Make the window invisible
options.add_argument("guest")                                                               #Make the chrome user a guest
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920,1200)                                                           #Set window size for a good screenshot
wait = WebDriverWait(driver, 10)                                                            #Set timings for delays and things
driver.get("https://pmsc.xuno.com.au/index.php/login")                                      #Set the website

#Sign in page
driver.find_element(By.NAME, "username").send_keys("Your username here")                    #Types your username
driver.find_element(By.NAME, "password").send_keys("Your password here")                    #Types your password
driver.find_element(By.XPATH, "//button[text()='Sign-in']").click()                         #Clicks the submit button
#You need at least a comment here to take enough time for the driver to load completely

#Main page
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "title")))                  #Waits for the timetable button to be clickable
element.click()                                                                             #Clicks the timetable button

#Timetable page
element = wait.until(EC.visibility_of_element_located((By.ID, "timetable-large")))          #Waits until the timetable page has loaded
driver.execute_script("document.body.style.zoom='100%'")                                    #Zooms out for a screenshot
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")                      #Aligns the page
element.screenshot("Images/screenshot.png")                                                 #Takes a screenshot and saves it in Images Folder
driver.quit()                                                                               #Quits