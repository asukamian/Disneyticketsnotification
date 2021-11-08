from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time


try :
    def wait():
        driver.implicitly_wait(3)
        WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.ID, 'searchResult')))
    driver = webdriver.Chrome(executable_path="#chromedriverの絶対パス")

    url = "https://reserve.tokyodisneyresort.jp/ticket/search/"
    driver.get(url)
    time.sleep(1)
    

    research1 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[1]/div[1]/section[1]/section[3]/div[2]/div/div/ul/div/div/li[1]/div/table/tbody/tr[4]/td[6]/a")

    research1.click()
    time.sleep(1)

    research2 = driver.find_element_by_id("searchEticket")

    research2.click()
    wait()


    research3 = driver.find_elements_by_xpath("/html/body/div[2]/div/div/div[1]/div[1]/div[1]/section[2]/section[2]/div/ul/li[1]/div/p[3]")
    def sellcheck():
        if len(research3) > 0 :
            return "販売してません"
        else:
            return "緊急販売中"



    x = sellcheck()


    def main():
        if x == "緊急販売中":
            send_line_notify(x)

    def send_line_notify(notification_message):
        """
        LINEに通知する
        """
        line_notify_token = '#トークン'
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'message: {notification_message}'}
        requests.post(line_notify_api, headers = headers, data = data)

    if __name__ == "__main__":
        main()

        time.sleep(2)
finally :

    driver.close()

    driver.quit()
