import pandas as pd

# 결측값
data = {
    "Name": ["홍길동", "임꺽정", "성춘향"],
    "Age": [25, None, 20],
    "City": ["서울", "부산", None]
}

df = pd.DataFrame(data)
# print(df)
# print(df.isnull()) # 결측값 여부
# print(df.isnull().sum()) # 결측값 개수의 합
# print(df.info())

# df_drop = df.dropna() # 결측값이 있는 행 모두 제거
# df_drop_column = df.dropna(axis=1)  # 결측값이 있는 열 삭제
# df_fill = df.fillna(0)
# df_fill_prev = df.fillna(method="ffill") # 이전에 있는 값으로 채움
# df_fill_next = df.fillna(method="bfill") # 다음에 있는 값으로 채움
# print(df_fill_next)

# -------------------------------------------------------------------
# 주요 메서드
# isin()
s = pd.Series(["홍길동", "임꺽정", "성춘향","이몽룡"])
result = s.isin(["홍길동", "이몽룡"])

data = {
    "Name":["홍길동", "임꺽정", "성춘향","이몽룡"],
    "Age": [25, 30, 20, 31]
}
df = pd.DataFrame(data)
# result = df.isin(["성춘향", "홍길동", 20]) # True, False 찾기
# result = df[df["Name"].isin(["성춘향", "홍길동", 20])] # True값만 필터링

s = pd.Series([1, 2, None])
result = s.isin([None, 2])
# print(result)

# value_counts()
s = pd.Series(["사과", "바나나", "사과", "오렌지", "바나나", "사과"])

df = pd.DataFrame({
    "과일": ["사과", "바나나", "사과", "오렌지", "바나나", None, "사과"],
    "수량": [1, 2, 3, 4 ,5 , 6, 7]
})
# print(df["과일"].value_counts(normalize=True)) # 빈도를 비율로 나타냄(%)
# print(df["과일"].value_counts(ascending=True)) # 오름차순으로 정렬
# print(df["과일"].value_counts(dropna=False)) 

# agg()
s = pd.Series([1, 2, 3, 4, 5])
result = s.agg(["sum", "mean", "max"])
print(result)

df = pd.DataFrame({"A": [ 1, 2, 3], "B": [10, 11, 12]})
print(df.agg(["sum", "mean"]))
print(df.agg({"A":"sum", "B":"mean"}))

# 연산 (사칙연산, 부등호)
s1 = pd.Series([10, 20, 30])
s2 = pd.Series([5, 15, 25])
print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 / s2)
print(s1 > 15)
# 동계연산
print(s1.sum())
print(s1.mean()) # 평균
print(s1.max())
print(s1.min())
print(s1.std()) # 표준편차
print(s1.var()) # 분산
print(s1.median()) # 중앙값
# 통계지표
print(s1.describe())

# 그룹
# data = {
#     "group": ["A", "A", "B", "B", "C"],
#     "value": [10, 20, 30, 40, 50]
# }
# df = pd.DataFrame(data)
# # result = df.groupby("group")["value"].max()
# result = df.groupby("group")["value"].agg(["sum", "mean", "var"])
# print(result)

data = {"group": ["A", "A", "B", "B", "C"],
    "value1": [10, 20, 30, 40, 50],
    "value2": [5, 15, 25, 35, 45]
}
df = pd.DataFrame(data)
# result = df.groupby("group").agg({"value1": "sum", "value2": ["mean", "max"]})
result = df.groupby("group").filter(lambda x: x["value1"].sum() > 30)
print(result)
