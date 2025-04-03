import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 실습1
# penguins = sns.load_dataset("penguins")

# # 펭귄의 종별 평균 몸무게를 막대그래프로 표시 
# plt.figure(figsize=(8, 6))
# sns.barplot(data=penguins, x='species', y='body_mass_g')
# plt.title("species or body_mass_g")
# plt.show()

# # 부리 길이와 부리 깊이의 관계를 산점도로 시각화 하고 종별로 색상을 다르게 표시
# plt.figure(figsize=(8, 6))
# sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue = "species", palette="deep")
# plt.title("length_mm or depth_mm")
# plt.show()

# # 펭귄의 섬에 따라 몸무게를 분포
# plt.figure(figsize=(8, 6))
# sns.violinplot(data=penguins, x='island', y='body_mass_g', hue='species', split=True, palette='deep')
# plt.title('island')
# plt.show()

# 실습2
# flights = sns.load_dataset("flights")
# # print(flights.info())

# # 연도별 승객수의 평균 -> 꺾은선 그래프
# sns.lineplot(data=flights, x="year", y="passengers")
# plt.show()

# # 연도와 월별 승객수 -> 히트맵
# plt.figure(figsize=(10,6))
# sns.heatmap(flights.pivot(index="month", columns="year", values="passengers"), annot = True, fmt="d", cmap = "crest")
# plt.show()

# # 특정 연도의 월별 승객수 -> 막대 그래프 
# flights_1958 = flights[flights["year"] == 1958]
# sns.barplot(data=flights_1958, x='month', y='passengers')
# plt.show()

# 실습3
# titanic = sns.load_dataset("titanic")
# # print(titanic.info())

# # 탑승클래스와 생존여부 간의 관계(catplot)
# sns.catplot(data=titanic, x="class", y="survived",kind="point")
# plt.show()

# # 나이의 분포를 생존 여부에 따라 시각화(kdeplot)
# sns.kdeplot(data=titanic, x="age", hue="survived", common_norm=False)
# plt.show()