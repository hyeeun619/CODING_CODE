import pandas as pd

# 리스트 형식으로 생성
# data = [10, 20, 30, 40]
# series = pd.Series(data) #기본 인덱스
# series = pd.Series(data, index = ["a", "b", "c", "d"]) # 커스텀 인덱스
# print(series)

# 딕셔너리 형식으로 생성
# data = {
#     "a": 10,
#     "b": True,
#     "c": 3.14,
#     "d": "python"
# }
# series = pd.Series(data, name="딕셔너리")
# print(series)
# print(series.index)
# print(series.values)
# print(series.shape)

# data = ("민지", "여", False)
# member = pd.Series(data, index = ["이름", "성별", "결혼여부"])
# print(member)
# print(member["이름"])
# print(member[["성별", "결혼여부"]])

# data = [10, 20, 30, 40, 50]
# series = pd.Series(data, index = ["a", "b", "c", "d", "e"])
# print(series["a"]) # 인덱스를 변경했으면 그 인덱스를 사용(권장)
# print(series[series > 20])
# series["c"] = 100
# print(series)
# print("a" in series) # 인덱스 "a"가 존재
# print(series.sum()) # 합계
# print(series.mean()) # 평균
# print(series.max()) # 최대값
# print(series.astype(float)) # 타입을 변경

# pandas vs numpy
# 인덱스: 커스텀이 가능 vs 숫자(0부터)
# 데이터 타입 : 혼합가능 vs 단일

# 실습
# data = ["4 cups", "1 cup", "2 large", "1 can"]
# series = pd.Series(data, index = ["밀가루", "우유", "계란", "참치캔"], name= "Dinner")
# print(series)

# -------------------------------------------------------------------
# 데이터프레임

# index = ["2020", "2021", "2022", "2023", "2024", "2025"]
# yeonhee = pd.Series([140, 150, 160, 170, 180, 190], index=index)
# cheolsu = pd.Series([200, 210, 220, 230, 240, 250], index=index)

# result = pd.DataFrame({"영희": yeonhee, "철수": cheolsu})
# print(result)
# print(result.head()) # 0~5 위에서 5개 출력
# print(result.tail()) # 아래에서 5개 출력
# print(result.shape) # 6행 2열 (6, 2)
# print(result.info()) # 요약정보
# print(result.columns) # 열이름
# print(result.values) # 행값
# print(result.index) 
# print(result.dtypes)
# print(result["철수"])
# print(result[["철수"]])

# data = {
#     "Name": ["홍길동", "임꺽정", "성춘향"],
#     "Age": [25, 30, 27],
#     "City": ["서울", "부산", "인천"]
# }
# df = pd.DataFrame(data, index = ["a", "b", "c"])
# print(df)
# loc(index, cloum)
# print(df.loc["b"])
# print(df.loc["b", "Age"])
# print(df.loc["a":"c", "Name":"Age"])
# print(df.loc[~(df["Age"] >= 30)])
# print(df.loc[:, "Name"])
# print(df.loc["a", :])

# print(df.iloc[1])
# print(df.iloc[1, 1])
# print(df.iloc[0:2, 0:1]) # 끝 값이 포함되지 않음
# print(df.iloc[[0, 2], [1, 2]])
# print(df.iloc[:, 0])
# print(df.iloc[0, :])

# 데이터를 넣고 추가/수정하는 방법
# 행 추가
# new_data = {"Name": "이몽룡", "Age": 31, "City": "포항"}
# result = pd.concat([df, pd.DataFrame([new_data])],ignore_index=True)

# # 인덱스 같이 행 추가
# new_data = pd.DataFrame({"Name": "이몽룡", "Age": 31, "City": "포항"}, index=["d"])
# concat
# result = pd.concat([df, new_data])
# # loc
# result.loc["e"] = ["전우치", 28, "대전"]

# 인덱스 같이 열 추가
# result["직업"] = ["엔지니어", "개발자", "디자이너", "기획자", "데이터분석가"]

# 요소값 수정
# result.at["b", "City"] = "천안"
# result.loc[result["Name"] == "임꺽정", "Age"] = 31

# 컬럼값 변경
# result.rename(columns={"Name": "이름", "Age":"나이", "City": "도시"},inplace=True)

# 데이터 정렬(기본:오름차순)
# result.sort_values(by="나이", inplace=True, ascending=False)
# # ascending=False :내림차순 

# 컬럼 삭제
# result.drop(columns=["도시"], inplace=True)
# print(result)

# 실습. 데이터프레임 만들기
data = {"이름": ["홍길동", "임꺽정", "성춘향"],
"수학": [85, 90, 78],
"영어": [88, 76, 92],
"과학": [95, 89, 84]}
df = pd.DataFrame(data)
print(df)

new_data = {"이름": "이몽룡", "수학": 88, "영어": 85, "과학": 90}
result = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
result["Total"] = result[["수학", "영어", "과학"]].sum(axis=1)
result.at[1, "영어"] = 80
result.rename(columns={"수학": "Math"}, inplace=True)
# result = result.rename(columns={"수학": "Math"})
print(result)