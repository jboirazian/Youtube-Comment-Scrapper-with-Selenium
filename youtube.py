import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.command import Command
import pandas as pd   
import os

cwd = os.getcwd()
video = []

with open('videos.txt', 'r') as f:
    f.readline()  # skip first line
    for vod in f:
        video.append(str(vod).rstrip("\n"))

print("Download the following comments from this videos\n")
for vid in video:
	print(vid)

input("Press Enter to Start...")



chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : cwd}
chromeOptions.add_experimental_option("prefs",prefs)

#### PUT THE LOCAL ADRESS OF YOUR chromedriver.exe
driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe",options=chromeOptions)
  
wait = WebDriverWait(driver,5)
driver.get("https://youtuberandomcomment.com/")
phone_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bd"]/div/ul/li[2]/a')))
phone_button .click()  
wait = WebDriverWait(driver,5)

for V in video:
	link = driver.find_element_by_xpath('//*[@id="linkAll"]')
	link.send_keys(V)
	driver.find_element_by_id('getAllComments').click()
	time.sleep(4)
	link.clear()
	time.sleep(1)
	
input("DONE ! , Press Enter to End...")
exit()
