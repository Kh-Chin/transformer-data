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

# 爬虫设置
save_path = 'D:\\其桦D盘\\其桦大学\\毕业论文\\scrapper\\scrap_result'
driver_path = r'C:\Users\keehu\Downloads\chromedriver_win32 (ver109)\chromedriver.exe'
username = ""
password = ""

code_list = [43,51,57,75,77,80,84,91,112,116,118,140,141,143,147]
industry_codes = {
    1: 'Defense and Space Manufacturing',
    3: 'Computer Hardware Manufacturing',
    4: 'Software Development',
    5: 'Computer Networking Products',
    6: 'Technology, Information and Internet',
    7: 'Semiconductor Manufacturing',
    8: 'Telecommunications',
    9: 'Law Practice',
    10: 'Legal Services',
    11: 'Business Consulting and Services',
    12: 'Biotechnology Research',
    13: 'Medical Practices',
    14: 'Hospitals and Health Care',
    15: 'Pharmaceutical Manufacturing',
    16: 'Veterinary Services',
    17: 'Medical Equipment Manufacturing',
    18: 'Personal Care Product Manufacturing',
    19: 'Retail Apparel and Fashion',
    20: 'Sporting Goods Manufacturing',
    21: 'Tobacco Manufacturing',
    22: 'Retail Groceries',
    23: 'Food and Beverage Manufacturing',
    24: 'Computers and Electronics Manufacturing',
    25: 'Manufacturing',
    26: 'Furniture and Home Furnishings Manufacturing',
    27: 'Retail',
    28: 'Entertainment Providers',
    29: 'Gambling Facilities and Casinos',
    30: 'Travel Arrangements',
    31: 'Hospitality',
    32: 'Restaurants',
    33: 'Spectator Sports',
    34: 'Food and Beverage Services',
    35: 'Movies, Videos, and Sound',
    36: 'Broadcast Media Production and Distribution',
    37: 'Museums, Historical Sites, and Zoos',
    38: 'Artists and Writers',
    39: 'Performing Arts',
    40: 'Recreational Facilities',
    41: 'Banking',
    42: 'Insurance',
    43: 'Financial Services',
    44: 'Real Estate',
    45: 'Investment Banking',
    46: 'Investment Management',
    47: 'Accounting',
    48: 'Construction',
    49: 'Wholesale Building Materials',
    50: 'Architecture and Planning',
    51: 'Civil Engineering',
    52: 'Aviation and Aerospace Component Manufacturing',
    53: 'Motor Vehicle Manufacturing',
    54: 'Chemical Manufacturing',
    55: 'Machinery Manufacturing',
    56: 'Mining',
    57: 'Oil and Gas',
    58: 'Shipbuilding',
    59: 'Utilities',
    60: 'Textile Manufacturing',
    61: 'Paper and Forest Product Manufacturing',
    62: 'Railroad Equipment Manufacturing',
    63: 'Farming',
    64: 'Ranching',
    65: 'Dairy Product Manufacturing',
    66: 'Fisheries',
    67: 'Primary and Secondary Education',
    68: 'Higher Education',
    69: 'Education Administration Programs',
    70: 'Research Services',
    71: 'Armed Forces',
    72: 'Legislative Offices',
    73: 'Administration of Justice',
    74: 'International Affairs',
    75: 'Government Administration',
    76: 'Executive Offices',
    77: 'Law Enforcement',
    78: 'Public Safety',
    79: 'Public Policy Offices',
    80: 'Advertising Services',
    81: 'Newspaper Publishing',
    82: 'Book and Periodical Publishing',
    83: 'Printing Services',
    84: 'Information Services',
    85: 'Libraries',
    86: 'Environmental Services',
    87: 'Freight and Package Transportation',
    88: 'Individual and Family Services',
    89: 'Religious Institutions',
    90: 'Civic and Social Organizations',
    91: 'Consumer Services',
    92: 'Truck Transportation',
    93: 'Warehousing and Storage',
    94: 'Airlines and Aviation',
    95: 'Maritime Transportation',
    96: 'IT Services and IT Consulting',
    97: 'Market Research',
    98: 'Public Relations and Communications Services',
    99: 'Design Services',
    100: 'Non-profit Organizations',
    101: 'Fundraising',
    102: 'Strategic Management Services',
    103: 'Writing and Editing',
    104: 'Staffing and Recruiting',
    105: 'Professional Training and Coaching',
    106: 'Venture Capital and Private Equity Principals',
    107: 'Political Organizations',
    108: 'Translation and Localization',
    109: 'Computer Games',
    110: 'Events Services',
    111: 'Retail Art Supplies',
    112: 'Appliances, Electrical, and Electronics Manufacturing',
    113: 'Online Audio and Video Media',
    114: 'Nanotechnology Research',
    115: 'Musicians',
    116: 'Transportation, Logistics, Supply Chain and Storage',
    117: 'Plastics Manufacturing',
    118: 'Computer and Network Security',
    119: 'Wireless Services',
    120: 'Alternative Dispute Resolution',
    121: 'Security and Investigations',
    122: 'Facilities Services',
    123: 'Outsourcing and Offshoring Consulting',
    124: 'Wellness and Fitness Services',
    125: 'Alternative Medicine',
    126: 'Media Production',
    127: 'Animation and Post-production',
    128: 'Leasing Non-residential Real Estate',
    129: 'Capital Markets',
    130: 'Think Tanks',
    131: 'Philanthropic Fundraising Services',
    132: 'E-Learning Providers',
    133: 'Wholesale',
    134: 'Wholesale Import and Export',
    135: 'Industrial Machinery Manufacturing',
    136: 'Photography',
    137: 'Human Resources Services',
    138: 'Retail Office Equipment',
    139: 'Mental Health Care',
    140: 'Graphic Design',
    141: 'International Trade and Development',
    142: 'Beverage Manufacturing',
    143: 'Retail Luxury Goods and Jewelry',
    144: 'Renewable Energy Semiconductor Manufacturing',
    145: 'Glass, Ceramics and Concrete Manufacturing',
    146: 'Packaging and Containers Manufacturing',
    147: 'Automation Machinery Manufacturing',
    148: 'Government Relations Services'
}


# 初始化爬虫
def initialize(driver_path, username, password):
    ser = Service(driver_path)
    driver = webdriver.Chrome(service=ser)
    driver.get('https://www.linkedin.com/login')
    if driver.current_url != "https://www.linkedin.com/feed/":
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").click()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()
    time.sleep(1)
    return driver

# 提取元素文本
def find_element_text(driver, by, path):
    try:
        return driver.find_element(by, path).text.strip()
    except:
        return None

# 提取元素两个文本
def find_two_text(driver, by, path):
    try:
        array = driver.find_element(by, path).text.strip().split(" · ")
        if len(array) > 1:
            return array[0], array[1]
        else:
            return array[0], None
    except:
        return None, None

# 根据领域码爬取
def scrap_by_code(driver, industry_code):
    record_list = []
    try:
        driver.get(f'https://www.linkedin.com/jobs/search/?&f_I={industry_code}&refresh=False&sortBy=DD')
        time.sleep(2)
        number = driver.find_element(By.TAG_NAME, "small").text.split(" ")[0]
        number = int(number.replace(",",""))
        for start in range(0,min(number,500),25):
            try:
                driver.get(f'https://www.linkedin.com/jobs/search/?&f_I={industry_code}&refresh=False&sortBy=DD&start={start}')
                time.sleep(2)
                for count in range(1,26):
                    try:
                        item = driver.find_element(By.XPATH, f'//*[@id="main"]/div/section[1]/div/ul/li[{count}]')
                        ActionChains(driver)\
                            .scroll_to_element(item)\
                            .perform()
                        item.click()
                        time.sleep(2)
                        job_title = find_element_text(driver, By.XPATH, "//*[@class='t-24 t-bold jobs-unified-top-card__job-title']")
                        company_name = find_element_text(driver, By.XPATH, "//*[@class = 'jobs-unified-top-card__subtitle-primary-grouping t-black']/span[1]/a")
                        location = find_element_text(driver, By.XPATH, "//*[@class = 'jobs-unified-top-card__subtitle-primary-grouping t-black']/span[2]")
                        job_type, position = find_two_text(driver, By.XPATH, "//*[@class = 'mt5 mb2']/ul/li[1]/span")
                        emps, field = find_two_text(driver, By.XPATH, "//*[@class = 'mt5 mb2']/ul/li[2]/span")
                        job_desc = find_element_text(driver, By.XPATH, "//article")
                        job_desc_with_html = driver.find_element(By.XPATH, "//article").get_attribute("outerHTML") if job_desc else None
                        try:
                            driver.find_element(By.XPATH, "//button[@class='jobs-unified-top-card__job-insight-text-button']").click()
                            skill_list = WebDriverWait(driver, 2).until(lambda d:d.find_elements(By.XPATH, f'//ul[@class="job-details-skill-match-status-list"]/li/div/div[2]'))
                            skills = ", ".join(skill.text for skill in skill_list)
                            dismiss_btn = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
                            dismiss_btn.click()
                            time.sleep(1)
                        except:
                            skills = None
                        record = {
                            "Job title":job_title,
                            "Company name":company_name,
                            "Location":location,
                            "Job type":job_type,
                            "Position":position,
                            "Num of employees":emps,
                            "Field":field,
                            "Skills":skills,
                            "Job desc":job_desc,
                            "Job desc(HTML)": job_desc_with_html
                        }
                        record_list.append(record)
                    except Exception as item_exception:
                        print(f"Item Exception(code:{industry_code}, count:{start+count})\nException:{item_exception}")
                        if "linkedin.com/jobs" not in driver.current_url:
                            driver.execute_script("window.history.go(-1)")
                            time.sleep(2)
                        continue
            except Exception as page_exception:
                print(f"Page exception:(code:{industry_code}, count:{start+count}, total:{number})\nException:{page_exception}")
                continue

    except Exception as e:
        driver.quit()
        raise e
    finally:
        return record_list

# 爬取程序
def scrap(driver, code, save_path):
    record_list = scrap_by_code(driver, code)
    df = pd.DataFrame(record_list)
    df.to_csv(f"{save_path}\\res_{code}.csv", sep="|")
    print(f"Industry code:{code} completed!")

driver = initialize(driver_path, username, password)
scrap(driver, 99, save_path)
scrap(driver, 103, save_path)
scrap(driver, 104, save_path)
scrap(driver, 110, save_path)