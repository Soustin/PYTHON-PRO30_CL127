from tempfile import tempdir
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/SOUSTIN/Downloads/chromedriver_win32")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name", "distance", "mass", "radius"]
    star_data = []
    for i in range(0, 98):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        star_table = soup.find('table')
        temp_list = []
        table_rows = star_table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)
        
        Star_names = []
        Distance = []
        Mass = []
        Radius = []
        Lum = []

        for i in range(1, len(temp_list)):
            Star_names.append(temp_list[i][1])
            Distance.append(temp_list[i][3])
            Mass.append(temp_list[i][5])
            Radius.append(temp_list[i][6])
            Lum.append(temp_list[i][7])
