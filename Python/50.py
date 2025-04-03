from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # By사용
from selenium.webdriver.common.keys import Keys  # Key사용
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import os
import requests
import numpy as np

# service = Service()
# driver = webdriver.Chrome(service=service)

# driver.get("https://www.koreabaseball.com/")
# time.sleep(2)

# a = driver.find_element(By.XPATH, '//*[@id="lnb"]/li[2]').click()
# time.sleep(2)

# b =driver.find_element(By.XPATH, '//*[@id="lnbTeamRank"]').click()
# time.sleep(2)

# c = driver.find_elements(By.CSS_SELECTOR, '.tData tr')


# driver.quit()

# # with open("datas/2024kbo.txt", "w", encoding='utf-8') as file:
# #     file.write(c)

# # with open("datas/2024kbo.txt", "r", encoding='utf-8')as file:
# #     data = file.read()
# #     print(data)

# input("")

# 실습 야구데이터
url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

table = soup.select_one("table.tData")
trs = table.select("tr")[1:]

lists = []
for tr in trs:
    td = tr.select("td")
    td = [i.text.strip() for i in td] # td랑 공백 지우기
    lists.append([td[0], td[1], td[3], td[4], td[5], td[6]])

array = np.array(lists)

file_name = "kbo_2024_ranking.txt"
header = "순위\t팀\t승\t패\t무\t승률" #파일 제목

with open(file_name, "w", encoding="utf-8")as file:
    file.write(header + "\n")
    for data in array:
        file.write("\t".join(data) + "\n")

with open(file_name, "r", encoding="utf-8")as file:
    print(file.read())

# join(): 문자열 리스트를 하나의 문자열로 결합할 때
# word = ["홍길동", "성춘향", "이몽룡"]
# print(" ".join(word))


# 데이터 분석 순서
# 1. 수집(파일 불러오기, 웹 스크래핑(크롤링))
# 웹 스크래핑 2가지 방법 : Bea-, sell-
# 2. 전처리 과정
# 파일불러오기 : Nempy(수치), pandas(그 외)
# 3. 시각화