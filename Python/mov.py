from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹 드라이버 초기화
driver = webdriver.Chrome()

# 사이트 열기
driver.get("https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_RSN")
time.sleep(2)

# 년도와 지역 선택
driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]').click()
driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]/option[3]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]').click()
driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]/option[1]').click()

# 메뉴 선택
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
time.sleep(1)

# 1번 체크박스 클릭 후 결과 출력
checkbox_1 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[1]/input')
if not checkbox_1.is_selected():
    checkbox_1.click()  # 체크박스 1번 클릭
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num1 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-중앙선침범 : {num1.text}건")

# 체크박스 열기
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 2번 체크박스 클릭
checkbox_2 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[2]/input')
checkbox_2.click()  # 2번 체크박스 클릭
time.sleep(1)

# 1번 체크박스 해제 후 2번 체크박스 클릭 후 결과 출력
checkbox_1.click()  # 1번 체크박스 해제
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num2 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-신호위반 : {num2.text}건")

# 체크박스 열기
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 3번 체크박스 클릭 후 결과 출력
checkbox_3 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[3]/input')
checkbox_3.click()  # 3번 체크박스 클릭
time.sleep(1)

# 2번 체크박스 해제 후 3번 체크박스 클릭 후 결과 출력
checkbox_2.click()  # 2번 체크박스 해제
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num3 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-안전거리미확보 : {num3.text}건")

# 체크박스 열기
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 4번 체크박스 클릭 후 결과 출력
checkbox_4 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[4]/input')
checkbox_4.click()  # 4번 체크박스 클릭
time.sleep(1)

# 3번 체크박스 해제 후 4번 체크박스 클릭 후 결과 출력
checkbox_3.click()  # 3번 체크박스 해제
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num4 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-안전운전불이행 : {num4.text}건")

# 체크박스 열기
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 5번 체크박스 클릭 후 결과 출력
checkbox_5 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[5]/input')
checkbox_5.click()  # 5번 체크박스 클릭
time.sleep(1)

# 4번 체크박스 해제 후 5번 체크박스 클릭 후 결과 출력
checkbox_4.click()  # 4번 체크박스 해제
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num5 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-교차로운행방법위반 : {num5.text}건")

# 체크박스 열기
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 6번 체크박스 클릭 후 결과 출력
checkbox_6 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[6]/input')
checkbox_6.click()  # 6번 체크박스 클릭
time.sleep(1)

# 5번 체크박스 해제 후 6번 체크박스 클릭 후 결과 출력
checkbox_5.click()  # 5번 체크박스 해제
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num6 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-보행자보호의무위반 : {num6.text}건")

# 체크박스 열기
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 7번 체크박스 클릭 후 결과 출력
checkbox_7 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[7]/input')
checkbox_7.click()  # 7번 체크박스 클릭
time.sleep(1)

# 6번 체크박스 해제 후 7번 체크박스 클릭 후 결과 출력
checkbox_6.click()  # 6번 체크박스 해제
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num7 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-기타 : {num7.text}건")

# 체크박스 열기
driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
time.sleep(1)

# 8번 체크박스 클릭 후 결과 출력
checkbox_8 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[8]/input')
checkbox_8.click()  # 8번 체크박스 클릭
time.sleep(1)

# 7번 체크박스 해제 후 8번 체크박스 클릭 후 결과 출력
checkbox_7.click()  # 7번 체크박스 해제
time.sleep(1)

# 페이지 누르기
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

# 검색 버튼 클릭 (WebDriverWait 사용)
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, search_button_xpath))
)
search_button.click()

# 페이지 로딩 기다리기
time.sleep(10)

# 총 발생건수
num8 = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
print(f"사망사고-과속(~2020) : {num8.text}건")

# 드라이버 종료
driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # 웹 드라이버 초기화
# driver = webdriver.Chrome()

# # 사이트 열기
# driver.get("https://taas.koroad.or.kr/gis/mcm/mcl/initMap.do?menuId=GIS_GMP_STS_RSN")
# time.sleep(2)

# # 년도와 지역 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]').click()
# driver.find_element(By.XPATH, '//*[@id="ptsRafYearStart"]/option[3]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]').click()
# driver.find_element(By.XPATH, '//*[@id="ptsRafSigungu"]/option[1]').click()

# # 메뉴 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
# time.sleep(1)

# # 체크박스 번호 1부터 8까지 반복
# for i in range(1, 9):
#     # 체크박스 클릭
#     checkbox_xpath = f'//*[@id="ptsRafCh1ViolatinLaw"]/li[{i}]/input'
#     checkbox = driver.find_element(By.XPATH, checkbox_xpath)
    
#     # 이전에 클릭한 체크박스를 해제 (현재 선택한 체크박스를 제외한 다른 체크박스는 해제)
#     for j in range(1, 9):
#         if j != i:  # 현재 체크박스를 제외한 나머지 체크박스는 해제
#             checkbox_to_uncheck = driver.find_element(By.XPATH, f'//*[@id="ptsRafCh1ViolatinLaw"]/li[{j}]/input')
#             if checkbox_to_uncheck.is_selected():
#                 checkbox_to_uncheck.click()
#     time.sleep(1)

#     # 현재 체크박스 클릭
#     if not checkbox.is_selected():
#         checkbox.click()  # 체크박스 클릭
#     time.sleep(1)
    
#     # 페이지 누르기
#     driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

#     # 검색 버튼 클릭 (WebDriverWait 사용)
#     search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
#     search_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, search_button_xpath))
#     )
#     search_button.click()

#     # 페이지 로딩 기다리기
#     time.sleep(10)

#     # 총 발생건수 출력
#     num = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
#     print(f"사망사고 : {num.text}건")
    
#     # 체크박스 열기
#     driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
#     time.sleep(1)


# # 사고 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[1]/input').click()
# time.sleep(1)

# # 메뉴 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
# time.sleep(1)

# # 체크박스 번호 1부터 8까지 반복
# for i in range(1, 9):
#     # 체크박스 클릭
#     checkbox_xpath = f'//*[@id="ptsRafCh1ViolatinLaw"]/li[{i}]/input'
#     checkbox = driver.find_element(By.XPATH, checkbox_xpath)
    
#     # 이전에 클릭한 체크박스를 해제 (현재 선택한 체크박스를 제외한 다른 체크박스는 해제)
#     for j in range(1, 9):
#         if j != i:  # 현재 체크박스를 제외한 나머지 체크박스는 해제
#             checkbox_to_uncheck = driver.find_element(By.XPATH, f'//*[@id="ptsRafCh1ViolatinLaw"]/li[{j}]/input')
#             if checkbox_to_uncheck.is_selected():
#                 checkbox_to_uncheck.click()
#     time.sleep(1)

#     # 현재 체크박스 클릭
#     if not checkbox.is_selected():
#         checkbox.click()  # 체크박스 클릭
#     time.sleep(1)
    
#     # 페이지 누르기
#     driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

#     # 검색 버튼 클릭 (WebDriverWait 사용)
#     search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
#     search_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, search_button_xpath))
#     )
#     search_button.click()

#     # 페이지 로딩 기다리기
#     time.sleep(10)

#     # 총 발생건수 출력
#     num = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
#     print(f"사망사고 : {num.text}건")
    
#     # 체크박스 열기
#     driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
#     time.sleep(1)

# # 사고 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[2]/input').click()
# time.sleep(1)

# # 메뉴 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
# time.sleep(1)

# # 체크박스 번호 1부터 8까지 반복
# for i in range(1, 9):
#     # 체크박스 클릭
#     checkbox_xpath = f'//*[@id="ptsRafCh1ViolatinLaw"]/li[{i}]/input'
#     checkbox = driver.find_element(By.XPATH, checkbox_xpath)
    
#     # 이전에 클릭한 체크박스를 해제 (현재 선택한 체크박스를 제외한 다른 체크박스는 해제)
#     for j in range(1, 9):
#         if j != i:  # 현재 체크박스를 제외한 나머지 체크박스는 해제
#             checkbox_to_uncheck = driver.find_element(By.XPATH, f'//*[@id="ptsRafCh1ViolatinLaw"]/li[{j}]/input')
#             if checkbox_to_uncheck.is_selected():
#                 checkbox_to_uncheck.click()
#     time.sleep(1)

#     # 현재 체크박스 클릭
#     if not checkbox.is_selected():
#         checkbox.click()  # 체크박스 클릭
#     time.sleep(1)
    
#     # 페이지 누르기
#     driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

#     # 검색 버튼 클릭 (WebDriverWait 사용)
#     search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
#     search_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, search_button_xpath))
#     )
#     search_button.click()

#     # 페이지 로딩 기다리기
#     time.sleep(10)

#     # 총 발생건수 출력
#     num = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
#     print(f"사망사고 : {num.text}건")
    
#     # 체크박스 열기
#     driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
#     time.sleep(1)

# # 사고 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[4]/input').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="ptsRafCh1AccidentContent"]/li[3]/input').click()
# time.sleep(1)

# # 메뉴 선택
# driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
# time.sleep(1)

# # 체크박스 번호 1부터 8까지 반복
# for i in range(1, 9):
#     # 체크박스 클릭
#     checkbox_xpath = f'//*[@id="ptsRafCh1ViolatinLaw"]/li[{i}]/input'
#     checkbox = driver.find_element(By.XPATH, checkbox_xpath)
    
#     # 이전에 클릭한 체크박스를 해제 (현재 선택한 체크박스를 제외한 다른 체크박스는 해제)
#     for j in range(1, 9):
#         if j != i:  # 현재 체크박스를 제외한 나머지 체크박스는 해제
#             checkbox_to_uncheck = driver.find_element(By.XPATH, f'//*[@id="ptsRafCh1ViolatinLaw"]/li[{j}]/input')
#             if checkbox_to_uncheck.is_selected():
#                 checkbox_to_uncheck.click()
#     time.sleep(1)

#     # 현재 체크박스 클릭
#     if not checkbox.is_selected():
#         checkbox.click()  # 체크박스 클릭
#     time.sleep(1)
    
#     # 페이지 누르기
#     driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()

#     # 검색 버튼 클릭 (WebDriverWait 사용)
#     search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
#     search_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, search_button_xpath))
#     )
#     search_button.click()

#     # 페이지 로딩 기다리기
#     time.sleep(10)

#     # 총 발생건수 출력
#     num = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
#     print(f"사망사고 : {num.text}건")
    
#     # 체크박스 열기
#     driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
#     time.sleep(1)

# # 드라이버 종료
# driver.quit()