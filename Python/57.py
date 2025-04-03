import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 한글설정
path = "Pretendard-Medium.ttf"
font = font_manager.FontProperties(fname=path).get_name()
plt.rc("font", family=font)


# file_name = "연령별인구현황_월간.csv"
# data = pd.read_csv(file_name, encoding="EUC-KR")

# # print(data.head())
# region_name = input("검색하고 싶은 지역명을 입력하세요: ")

# # 우리가 원하는 나이 컬럼 리스트
# age_columns = [col for col in data.columns if "세" in col]
# # print(age_columns)

# # 숫자로 변환
# for col in age_columns:
#     data[col] = data[col].str.replace(",", "").astype(int)

# # 필터링
# # contains() : 문자열 데이터 필터링, 특정 패턴을 찾을때
# # 옵션값
# # na : 결측값을 포함할지 결정, 기본값 True
# # case : 영문의 대소문자를 구분, 기본값 True
# region_data = data[data["행정구역"].str.contains(region_name, na=False)]

# if region_data.empty:
#     print(f"{region_name}의 지역은 존재하지 않습니다")

# # 데이터 추출
# # 2024년12월_계_0~9세 ["2024년12월", 0~9세]
# age_groups = [col.split("_계_")[1] for col in age_columns]
# # 결과값
# result = region_data[age_columns].iloc[0].values
# # print(result)


# # 그래프그리기
# plt.figure(figsize=(10, 8))
# plt.plot(age_groups, result, marker="o", label=region_name)
# plt.title(f"{region_name}의 연령별 인구수", fontsize=16, pad=10)
# plt.xlabel("연령대")
# plt.ylabel("인구수")
# plt.grid(True, linestyle="--", alpha=0.6)
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()


# 종합실습
file_name = "남여_연령별인구현황_월간.csv"
data = pd.read_csv(file_name, encoding="EUC-KR")

# print(data.info())

region_name = input("검색하고 싶은 지역명을 입력하세요 : ")
# 지역검색
region_data = data[data["행정구역"].str.contains(region_name, na=False)]
if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다")
    exit()

male_columns = [col for col in region_data.columns if "세" in col and "남" in col]
female_columns = [col for col in region_data.columns if "세" in col and "여" in col]
# print(male_columns)

# for col in male_columns:
#     region_data[col] = region_data[col].astype(str).str.replace(",", "").astype(int)
male_result = (
    region_data[male_columns].iloc[0].astype(str).str.replace(",", "").astype(int)
)
female_result = (
    region_data[female_columns].iloc[0].apply(lambda x: int(str(x).replace(",", "")))
)
# iloc : Serise에 백터화 연산을 적용하여 효율적이고 간결한 코드 작성이 가능
# apply() : 사용자함수 정의


age_groups = [col.split("_남_")[1] for col in male_columns]
# print(age_groups)

# 그래프 그리기
plt.figure(figsize=(10, 8))
plt.plot(
    age_groups,
    male_result,
    marker="o",
    label="남성",
    color="blue",
)
plt.plot(
    age_groups,
    female_result,
    marker="o",
    label="여성",
    color="red",
)

plt.title(f"{region_name}의 연령별 인구수", fontsize=16, pad=10, fontproperties=font)
plt.xlabel("연령대", fontproperties=font)
plt.ylabel("인구수", fontproperties=font)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45, fontproperties=font)
plt.legend()
plt.show()
