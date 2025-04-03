import csv
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

# 1번 체크박스 클릭
checkbox_1 = driver.find_element(By.XPATH, '//*[@id="ptsRafCh1ViolatinLaw"]/li[1]/input')
if not checkbox_1.is_selected():
    checkbox_1.click()  # 체크박스 1번 클릭
time.sleep(1)

# 사고 유형과 법규 위반 리스트 정의
accident_types = ['사망사고', '중상사고', '경상사고', '부상신고']
violations = ['중앙선침범', '신호위반']

# 사고 데이터 수집 함수
def collect_accident_data(accident_type, violation_type):
    # 사고 선택 및 법규 위반 선택
    accident_index = accident_types.index(accident_type) + 1
    driver.find_element(By.XPATH, f'//*[@id="ptsRafCh1AccidentContent"]/li[{accident_index}]/input').click()
    time.sleep(1)
    
    # 사고 유형에 따라 두 번째 항목 선택
    if accident_index < len(accident_types):
        driver.find_element(By.XPATH, f'//*[@id="ptsRafCh1AccidentContent"]/li[{accident_index + 1}]/input').click()
    time.sleep(1)
    
    driver.find_element(By.XPATH, '//*[@id="ptsRaf-LRG_VIOLT_1_CODE"]/a').click()
    time.sleep(1)
    
    # 법규 위반 선택
    if violation_type == '중앙선침범':
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[3]').click()
    elif violation_type == '신호위반':
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/div/p/a[2]').click()
    
    # 검색 버튼 클릭 (WebDriverWait 사용)
    search_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/p'
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, search_button_xpath))
    )
    search_button.click()

    # 페이지 로딩 기다리기
    time.sleep(10)

    # 총 발생건수
    num = driver.find_element(By.XPATH, '//*[@id="regionAccidentFind"]/div[3]/div[1]/span')
    print(f"{accident_type}-{violation_type} : {num.text}건")

    # 사고 데이터를 CSV에 저장
    with open('accident_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([f'{accident_type}-{violation_type}', num.text])

# 사고 유형과 법규 위반 반복문으로 데이터 수집
for accident_type in accident_types:
    for violation in violations:
        collect_accident_data(accident_type, violation)

# 웹 드라이버 종료
driver.quit()
