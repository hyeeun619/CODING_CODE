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

service = Service()
driver = webdriver.Chrome(service=service)

# # 실습1. github
# driver.get("https://github.com/login")

# driver.find_element(By.ID, "login_field").send_keys("gpdms7353@naver.com")
# driver.find_element(By.ID, "password").send_keys("whdqja0507!")
# driver.find_element(By.NAME, "commit").click()

# name = driver.find_element(
#     By.XPATH,
#     '//*[@id="switch_dashboard_context_left_column-button"]/span[1]/span/span[2]',
# )
# print(f"사용자 이름은 : {name.text}")
# input("")

# 실습2. 쇼핑몰 크롤링
# driver.get("https://www.11st.co.kr/")
# find = driver.find_element(By.CSS_SELECTOR, ".search_text")
# find.send_keys("노트북")
# find.send_keys(Keys.ENTER)
# time.sleep(5)

# items = driver.find_elements(By.CSS_SELECTOR, "#section_commonPrd .c-search-list__item")

# for item in items:
#     name = item.find_element(By.CSS_SELECTOR, ".c-card-item__name > dd").text
#     price = item.find_element(By.CSS_SELECTOR, ".c-card-item__price > span").text
#     price = int(price.replace(",", ""))
#     if price >= 500000:
#         print(f"상품명: {name}, 가격: {price}")

# input("")

# 실습 3. 여행사이트
# driver.get("https://www.agoda.com/ko-kr?ds=qdL8YSV4z5LoWxHS#rooms")
# time.sleep(2)
# departure = driver.find_element(By.ID, "textInput").send_keys("도쿄")
# search = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located(
#         (
#             By.XPATH,
#             '//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/div/div/ul',
#         )
#     )
# )
# search.find_element(By.CSS_SELECTOR, "li:first-child").click()
# # 시작날짜
# click_day = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(
#         (
#             By.XPATH,
#             '//*[@id="DatePicker__AccessibleV2"]/div/div[2]/div[1]/div[3]/div[5]/div[4]/div/div/div',
#         )
#     )
# )
# click_day.click()
# # 종료날짜
# driver.find_element(
#     By.XPATH,
#     '//*[@id="DatePicker__AccessibleV2"]/div/div[2]/div[2]/div[3]/div[1]/div[7]/div/div/div',
# ).click()
# # 인원클릭
# driver.find_element(By.ID, "occupancy-box").click()
# # people = WebDriverWait(driver, 10).until(
# #     EC.element_to_be_clickable((By.ID, "occupancy-box"))
# # )
# # 검색하기 클릭
# search_click = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="Tabs-Container"]/button'))
# )
# search_click.click()

# # 마지막으로 열린 탭으로 전환
# driver.switch_to.window(driver.window_handles[-1])

# # 호텔명
# hotel_name = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".hotel-list-container h3"))
# )
# price = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located(
#         (By.CSS_SELECTOR, ".hotel-list-container .PropertyCardPrice__Value")
#     )
# )
# print(f"호텔명 : {hotel_name[0].text}, 가격 {price[0].text}")
# input("")


# 실습4. 구글 이미지
# driver.get("https://www.google.com/imghp")
# time.sleep(2)

# search = driver.find_element(By.ID, "APjFqb")
# search.send_keys("토끼")
# search.send_keys(Keys.ENTER)
# time.sleep(2)

# # 무한스크롤
# for i in range(3):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     time.sleep(2)

# images = driver.find_elements(By.CSS_SELECTOR, "img.YQ4gaf")
# os.makedirs("images", exist_ok=True) # 폴더 신규 생성, 존재하면 무시

# code = 1
# for image in images:
#     src = image.get_attribute("src")
#     if "FAVICON" not in src and "https" in src:
#         print(src)
#         res = requests.get(src)
#     with open(f"images/img_{code}.png", "wb")as file:
#         file.write(res.content)
#     code += 1

# input("")