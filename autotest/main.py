from selenium import webdriver
from  time import sleep
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.android.chrome')
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get('https://www.cathaybk.com.tw/cathaybk')
driver.implicitly_wait(10)
driver.save_screenshot('home.png')
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/a/img[2]').click()#點擊個人金融
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[1]').click()#點擊產品介紹
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]').click()#點擊信用卡
driver.implicitly_wait(10)
driver.save_screenshot('credit_card_item.png')
credit_card_item = driver.find_elements(By.XPATH,"//div[contains(@class,'is-L2open')]//a[contains(@class,'cubre-a-menuLink')]")
print("信用卡項目: "+str(len(credit_card_item)))
sleep(7)
driver.find_element_by_xpath('//*[@id="lnk_Link"]').click()#點擊信用卡介紹
sleep(7)
driver.find_element_by_xpath('/html/body/div[1]/main/article/section[6]/div/div[2]').click()#點擊停卡
stop_card_list = driver.find_elements(By.XPATH,"//section[contains(@data-anchor-block,'blockname06')]//span[contains(@class,'swiper-pagination-bullet')]")
print("停卡數量: "+str(len(stop_card_list)))

stop_card = "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]" #XPath
for i in range(1, len(stop_card_list)+1):
    driver.find_element_by_xpath("/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]" + "/span[%d]"%(i)).click()
    sleep(10)
    driver.save_screenshot('stop_card_{}'.format(i) + ".png")
    sleep(10)



