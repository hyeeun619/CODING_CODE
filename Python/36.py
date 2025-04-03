from datetime import datetime, timedelta, date
import time

# import 구문은 파일 최상단에 작성하는 것이 좋음

# datetime 모듈
now = datetime.today() # 현재시간 및 시간 가져오기
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(f"{now.year}년 {now.month}월 {now.day}일")

now = datetime.now() # 현재 날짜와 시간 가져오기
print(now)

# 특정 날짜 계산
next_week = now + timedelta(weeks = 1, hours = 1)
before_two_hours = now - timedelta(hours = 2)
print(next_week)
print(before_two_hours)

# 개강일로부터 오늘까지의 지난 일자 계산
open_day = date(year = 2024, month = 12, day = 30) # 24년 12월 30일 날짜 생성

print(date.today()) # today(): 오늘 날짜 출력
print(date.today().weekday()) # weekday(): 요일을 숫자로 반환
# 주의. 0(월)~6(일)

week = ["월", "화", "수", "목", "금", "토", "일"]
print(week[date.today().weekday()])

pass_day = date.today() - open_day
print(pass_day) # 15 days, 0:00:00 -> "[일수] + [시:분:초]" (자세히)
print(pass_day.days) # 15 -> 일수값만 계산해서 정수 결과

# time 모듈

print(time.time()) # 1736842895.9358945
# 타임스탬프 값 출력
# 1970년 1월 1일 00:00:00을 기준으로 했을 때 현재까지의 시간 초 단위
# - 현재 시점에 따라 값이 달라짐

print(time.localtime()) # 로컬시간대 출력 (컴퓨터의 시스템 설정에 따라 다르게 출력)
# ime.struct_time(tm_year=2025, tm_mon=1, tm_mday=14, tm_hour=17, tm_min=24, tm_sec=1, tm_wday=1, tm_yday=14, tm_isdst=0)
# 참고. tm_yday : 연중 날짜 (1~366)
# 참고. tm_isdst : 서머타임 여부 (-1: 정보없음, 0: 비적용, 1: 적용)

print("2초 대기")
time.sleep(2) # 지정된 초단위 시간동안 프로그램 실행을 중지
print("대기 완료")

start_time = time.perf_counter() # 시간 측정
time.sleep(1)
end_time = time.perf_counter() 
print(end_time - start_time) # 1.0004484000382945
# 두 호출시간 차이 = 코드 실행 시간