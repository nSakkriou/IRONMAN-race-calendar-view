# coding: utf-8

from selenium import webdriver
import selenium, sys, os, time, json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

RACE_URL = "https://www.ironman.com/races"

def main():

    fullData = []

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    page = driver.get(RACE_URL)

    time.sleep(5)
    try:
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    except:
        pass

    # Scrap cards info
    def race_info():
        raceCards = driver.find_elements(By.CLASS_NAME, "race-card")

        for race in raceCards:
            data = {
                "date" : {
                    "day" : race.find_element(By.CLASS_NAME, "race-day").text,
                    "month" : race.find_element(By.CLASS_NAME, "race-month").text,
                    "year" : race.find_element(By.CLASS_NAME, "race-year").text,
                },

                "title" : race.find_element(By.TAG_NAME, "h3").text,
                "location" : race.find_element(By.CLASS_NAME, "race-location").text
            }

            fullData.append(data)

    # Get all pages
    c = 1
    while(True):
        time.sleep(2)
        race_info()

        print(f"LOG : Page {c} scrapped")
        c += 1

        try:
            element = driver.find_element(By.XPATH, f'//*[@id="pageEl_460466978"]/div/div[2]/div/div[{str(c)}]')
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.execute_script("arguments[0].click();", element)
        except: 
            break 

        time.sleep(2)

    with open('data.json', "w+", encoding="utf8") as f:
        f.write(json.dumps(fullData))



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

