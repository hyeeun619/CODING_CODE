#  실습
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]

# 도시별 평균기온 계산 = 기온 총합 / 기온 개수
def avg_temperatures():
    city = input("도시 이름을 입력하세요: ")

    total = 0 # 기온 총합
    count = 0 # 기온 개수

    for data in weather_data:
        if data[1] == city:
            total += data[2]
            count += 1 
    
    return city, total / count

# 도시별 최고/최소 기온 찾기
def avg_maxmin_temperatures():
    city = input("도시 이름을 입력하세요: ")

    temperatures = [data[2] for data in weather_data if data[1] == city]

    if not temperatures:
        return city, None, None
    else:
        return city, max(temperatures), min(temperatures)

# 도시별 강수량 분석
def total_rain_day():
    city = input("도시 이름을 입력하세요: ")

    temp = filter(lambda x: x[1] == city, weather_data) # 도시 추출

    # [0.0], [1.2], [0.0]
    rain = list(map(lambda x: x[3] ,temp)) # 강수량 추출
    # [1.2]
    total_rain = sum(rain) # 총 강수량
    # len([1.2]) -> 1
    rain_day = len(list(filter(lambda x: x>0, rain))) # 비가 온 날
    return city, total_rain, rain_day

# 데이터 추가
def add_weather():
    data = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시 이름을 입력하세요: ")
    temperatures = float(input("평균 기온을 입력하세요: "))
    rain = float(input("강수량을 입력하세요 (mm): "))

    weather_data.append([data, city, temperatures, rain])

    return city

# 전체 데이터 출력
def all_data():
    print("\n현재 저장된 날씨 데이터: ")

    for data in weather_data:
        print(f"날짜: {data[0]}, 도시: {data[1]}, 평균기온: {data[2]}도, 강수량{data[3]}mm")

# 프로그램 실행 함수
def main_program():
    while True:
        print("[날씨 데이터 분석 프로그램]")
        print("1. 평균 기온 계산")
        print("2. 최고/최저 기온 찾기")
        print("3. 강수량 분석")
        print("4. 날씨 데이터 추가")
        print("5. 전체 데이터 출력")
        print("6. 종료")
        choice = input("원하는 기능의 번호를 입력하세요: ")

        if choice == "1":
            city, avg_resuit = avg_temperatures()
            if avg_resuit is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 평균 기온: {avg_resuit: .2f}도")
        elif choice == "2":
            city, max_value, min_value = avg_maxmin_temperatures()
            if max_value is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 최고기온: {max_value}도, 최저기온: {min_value}도")
        elif choice == "3":
            city, total_rain, rain_day = total_rain_day()
            print(f"{city}의 총 강수량: {total_rain}mm")
            print(f"{city}의 비가 온 날: {rain_day}일")
        elif choice == "4":
            city = add_weather()
            print(f"{city}의 날씨 데이터가 추가되었습니다.")
        elif choice == "5":
            all_data()
        elif choice == "6":
            print("프로그램을 종료합니다.")
            break
        else:
            print("1~6까지의 번호를 입력하세요.")

main_program()

'''
# 람다식 이용해서 푸는법
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]
# 도시별 평균기온 계산 = 기온 총합 / 기온 개수
def avg_temperatures():
    city = input("도시 이름을 입력하세요: ")

    total = 0 # 기온 총합
    count = 0 # 기온 개수

    temp = filter(lambda x: x[1] == city, weather_data) # 도시추출
    temperatures = list(map(lambda x: x[2], temp)) # 기온 추출
    if not temperatures:
        return city, None
    else:
        return city,sum(temperatures) / len(temperatures)
# 도시별 최고/최소 기온 찾기
def avg_maxmin_temperatures():
    city = input("도시 이름을 입력하세요: ")

    temp = filter(lambda x: x[1] == city, weather_data) # 도시 추출
    temperatures = list(map(lambda x: x[2], temp)) # 기온 추출
    
    if not temperatures:
        return city, None, None
    else:
        return city, max(temperatures), min(temperatures)
# 도시별 강수량 분석
def total_rain_day():
    city = input("도시 이름을 입력하세요: ")

    temp = filter(lambda x: x[1] == city, weather_data) # 도시 추출
    rain = list(map(lambda x: x[3] ,temp)) # 강수량 추출
    total_rain = sum(rain) # 총 강수량
    rain_day = len(list(filter(lambda x: x>0, rain))) # 비가 온 날

    return city, total_rain, rain_day
# 데이터 추가
# 전체 데이터 출력
'''
