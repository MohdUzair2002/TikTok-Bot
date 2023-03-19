from selenium import webdriver
import time
import requests
import csv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

links=[]
main_data=[]

commenter_name_l=[]
commenter_text_l=[]
datet_l=[]

chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
# chrome_options.add_argument('--profile-directory=Profile 1')

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)

driver.get("https://www.tiktok.com/@islamicspeechesofficial")
i=0
while(i<5):
    link= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'tiktok-yz6ijl-DivWrapper e1cg0wnj1')]//a")))
    link=driver.find_elements(By.XPATH,"//div[contains(@class,'tiktok-yz6ijl-DivWrapper e1cg0wnj1')]//a")[i].get_attribute('href')
    print(link)
    links.append(link)
    i+=1
i=0
while(i<5):
    data=[]
    driver.get(links[i])
    # try:
    #     captcha_closer=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'captcha_verify_bar--close sc-chPdSV dSiAYZ')]")))
    #     captcha_closer=driver.find_element(By.XPATH,"//div[contains(@class,'captcha_verify_bar--close sc-chPdSV dSiAYZ')]").click()
    # except:
    #     pass
    j=0
    while(j<5):
        
        commenter_name=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(@class,'tiktok-mfqbp1-SpanUserNameText e1g2efjf3')]")))
        commenter_name=driver.find_elements(By.XPATH,"//span[contains(@class,'tiktok-mfqbp1-SpanUserNameText e1g2efjf3')]")[j]
        commenter_name_l.append(commenter_name.text)
        print(commenter_name.text)

        comment_text=driver.find_elements(By.XPATH,"//p[contains(@class,'tiktok-q9aj5z-PCommentText e1g2efjf6')]")[j]
        commenter_text_l.append(comment_text.text)
        print(comment_text.text)


        date=driver.find_elements(By.XPATH,"//p[contains(@class,'tiktok-1wmf4bu-PCommentSubContent e1g2efjf8')]//span[contains(@data-e2e,'comment-time-1')]")[j]
        datet_l.append(date.text)
        print(date.text)

        j+=1
    data.append(commenter_name_l)
    data.append(commenter_text_l)
    data.append(datet_l)
    main_data.append(data)
    commenter_name_l=[]
    commenter_text_l=[]
    datet_l=[]
    i+=1
header = ['Commenter Name','Comment Text','Date']
with open('post_comment_data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(main_data) 