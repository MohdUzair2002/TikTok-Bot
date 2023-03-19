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
from selenium.webdriver.common.action_chains import ActionChains

links=[]

name_channek_l=[]
date_l=[]
description_l=[]
tags_l=[]
commenter_name_l_l=[]
commenter_text_l_l=[]
datet_l_l=[]
main_data=[]
main_data_l=[]
main_data_1=[]
chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())

chrome_options.add_argument("--disable-blink-features=AutomationControlled")

chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)

driver.get("https://www.tiktok.com/@islamicspeechesofficial")
i=0
while(i<1):
    link= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'tiktok-yz6ijl-DivWrapper e1cg0wnj1')]//a")))
    link=driver.find_elements(By.XPATH,"//div[contains(@class,'tiktok-yz6ijl-DivWrapper e1cg0wnj1')]//a")[i].get_attribute('href')
    print(link)
    links.append(link)
    i+=1


i=0
while(i<1):
    driver.get(links[i])
    # captcha_closer=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'captcha_verify_bar--close sc-chPdSV dSiAYZ')]")))
    # captcha_closer=driver.find_element(By.XPATH,"//div[contains(@class,'captcha_verify_bar--close sc-chPdSV dSiAYZ')]").click()
    # driver.execute_script("arguments[0].click();", captcha_closer)


    
    data=[]
    commenter_name_l=[]
    commenter_text_l=[]
    datet_l=[]
    # //div[contains(@class,'captcha_verify_bar--close sc-chPdSV dSiAYZ')]
    name_channel=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(@class,'tiktok-1r8gltq-SpanUniqueId e17fzhrb1')]")))
    name_channel=driver.find_element(By.XPATH,"//span[contains(@class,'tiktok-1r8gltq-SpanUniqueId e17fzhrb1')]").text
    name_channek_l.append(name_channel)
    print(name_channel)
    date=driver.find_elements(By.XPATH,"//span[contains(@class,'tiktok-lh6ok5-SpanOtherInfos e17fzhrb2')]//span")[-1].text
    date_l.append(date)
    print(date)
    description=driver.find_elements(By.XPATH,"//span[contains(@class,'tiktok-j2a19r-SpanText efbd9f0')]")[0].text
    description_l.append(description)
    print(description)

    no_of_tags=driver.find_elements(By.XPATH,"//strong[contains(@class,'tiktok-f9vo34-StrongText ejg0rhn1')]")
    j=0
    while(j<len(no_of_tags)):
          tags=driver.find_elements(By.XPATH,"//strong[contains(@class,'tiktok-f9vo34-StrongText ejg0rhn1')]")[j].text
          tags_l.append(tags)
          print(tags)
          j+=1
    f=0
    while(f<5):
        
        commenter_name=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(@class,'tiktok-mfqbp1-SpanUserNameText e1g2efjf3')]")))
        commenter_name=driver.find_elements(By.XPATH,"//span[contains(@class,'tiktok-mfqbp1-SpanUserNameText e1g2efjf3')]")[f]
       
        commenter_name_l.append(commenter_name.text)
        print(commenter_name.text)
        
       
        comment_text=driver.find_elements(By.XPATH,"//p[contains(@class,'tiktok-q9aj5z-PCommentText')]")[f]
        a=''.join(c.encode("utf-8").decode() if ord(c) >= 65536 else c for c in comment_text.text)
        commenter_text_l.append(a)
        # commenter_text_l.append(())
        
        print(comment_text.text)


        date=driver.find_elements(By.XPATH,"//p[contains(@class,'tiktok-1wmf4bu-PCommentSubContent e1g2efjf8')]//span[contains(@data-e2e,'comment-time-1')]")[f]
        datet_l.append(date.text)
        print(date.text)
        print(commenter_text_l)
        f+=1
    
    data.append(name_channek_l)
    data.append(date_l)
    data.append(description_l)
    data.append(tags_l)
    commenter_name_l_l.append(commenter_name_l)
    commenter_text_l_l.insert(i,(commenter_text_l))
    print(i)
    print(commenter_text_l_l)
    datet_l_l.append(datet_l)
    name_channek_l=[]
    date_l=[]
    description_l=[]
    tags_l=[]
    commenter_name_l=[]
    commenter_text_l=[]
    datet_l=[]
    main_data_1.append(commenter_name_l_l)
    main_data_1.append(commenter_text_l_l)
    main_data_1.append(datet_l_l)
    main_data.append(data)
    main_data_l.append(main_data)
    main_data=[]
    i+=1

# time.sleep(200)
header = ['Channel Name','Date','Description','Tags']
with open('data.csv', 'w', encoding='Utf-8',newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        for post in main_data_l:
           writer.writerows(post)
           for comment in main_data_1:
                for comment_index in range (len(comment[0])):
                    writer.writerow([comment[0][comment_index],comment[1][comment_index], comment[2][comment_index]])

        print(main_data_1)
     
        
# a=[[[a,b,c],[]]]
    
a=[[1,2],[1,3]]

  

    
