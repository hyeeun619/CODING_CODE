import pandas as pd

# 실습. 공공데이터 활용

file_name = "운동기구.csv"
df = pd.read_csv(file_name, encoding="cp949")
# print(df.head())
# print(df.info())
df.columns = df.columns.str.strip()  # 열 이름 앞뒤 공백 제거

# 공원별 총 운동기구 설치 수
a = df.groupby("구분")["운동기구 수량"].sum()
with open("공원별 총 운동기구 설치 수", "w", encoding='utf-8') as file:
    file.write(a.to_csv(header=True))

# 운동기구 종류별 설치 개수
b = df.groupby("운동기구 기종명")["운동기구 수량"].sum()
with open("운동기구 종류별 설치 개수", "w", encoding='utf-8') as file:
    file.write(b.to_csv(header=True))

# 관리기관별 총 운동기구 설치 수
c = df.groupby("관리기관")["운동기구 수량"].sum()
with open("관리기관별 총 운동기구 설치 수", "w", encoding='utf-8') as file:
    file.write(c.to_csv(header=True))

# 특정 공원 데이터 필터링
df["구분"] = df["구분"].str.strip()  # 모든 공백을 제거
d = df[df["구분"] == "남산공원(회현)"]
with open("특정 공원 데이터 필터링", "w", encoding='utf-8') as file:
        file.write(d.to_csv(header=True))


# 특정 운동기구 종류 데이터 필터링
df["운동기구 기종명"] = df["운동기구 기종명"].str.strip()
e = df[df["운동기구 기종명"] == "스텝사이클"]
with open("특정 운동기구 종류 데이터 필터링", "w", encoding='utf-8') as file:
         file.write(e.to_csv(header=True))

# 운동기구 수량 기준 내림차순 정렬
f = df.sort_values(by='운동기구 수량', ascending=False)
with open("운동기구 수량 기준 내림차순 정렬", "w", encoding='utf-8') as file:
          file.write(f.to_csv(header=True))