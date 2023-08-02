import time
import pandas as pd
import numpy as np
import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


ser = Service(r'C:\Users\keehu\Downloads\chromedriver_win32 (ver109)\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
industry_code = {}
driver.get('https://www.linkedin.com/login')
driver.maximize_window()
if driver.current_url != "https://www.linkedin.com/feed/":
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()

driver.get(f'https://www.linkedin.com/jobs/search/?&f_I=4&refresh=False&sortBy=R')
time.sleep(3)
try:
    driver.find_element(By.XPATH, "//button[@class='jobs-unified-top-card__job-insight-text-button']").click()
    time.sleep(2)
    skill_list = driver.find_elements(By.XPATH, f'//ul[@class="job-details-skill-match-status-list"]/li/div/div[2]')
    skills = ", ".join(skill.text for skill in skill_list)
    dismiss_btn = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
    dismiss_btn.click()
    job_desc = driver.find_element(By.XPATH, "//article").text
    job_desc_with_html = driver.find_element(By.XPATH, "//article").get_attribute("outerHTML")
    while True:
        if input() == "q":
            break
finally:
    driver.close()