import matplotlib.pyplot as plt
from matplotlib import font_manager

# Matplotlib
# 폰트 경로
path = "Pretendard-Medium.ttf"
font_prop = font_manager.FontProperties(fname=path)
font = font_manager.FontProperties(fname=path).get_name()
plt.rc("font", family=font)

# 기본사용법
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y, color= "red", linestyle = "--", linewidth = 3, label= "sampele graph")

# plt.plot(
# x, y, marker="*", 
# markersize=20, markerfacecolor="red", 
# markeredgecolor="blue", label="marker sample")


# plt.title("맵플롯립", fontproperties=font_prop, pad=10, fontsize=20, color="red",backgroundcolor="green") # 풀어쓰는 방법 
# font = {
#     "size":20,
#     "color": "white",
#     "backgroundcolor": "black",
#     "weight": "bold"
# } # 폰트설정 

# plt.title("맵플롯립 딕셔너리",fontproperties=font_prop, pad=10, fontdict=font) # 딕셔너리 이용방법 
# plt.legend(title="legend", fontsize=13, loc="lower center") # 범례표시
# plt.grid(True, axis="both", linestyle="--", color="blue", alpha=0.1) # 그리드 

# # x, y축 레이블 
# plt.xlabel("x axis", fontdict=font, labelpad=10)
# plt.ylabel("y axis", fontdict=font)

# 축범위 설정
# plt.xlim([1, 10]) 
# plt.ylim([0, 20])
# plt.axis([1, 10, 0, 20]) # 위와 동일 x, y축 동시에 입력하는 방법
# plt.axis("equal") # x, y축 동일하게 설정
# plt.axis("scaled") # x, y축 비율에 따라 스케일 설정
# plt.axis("tight") # 그래프에 모든 영역을 채우도록 설정
# plt.axis("auto") # 자동으로 축설정

# plt.show()

# 그래프 여러개 표시
# 하나의 창에 여러개 그래프 그리기 
# x = [1, 2, 3, 4]
# y1 = [1, 2, 3, 4]
# y2 = [2, 4, 6, 8]
# y3 = [3, 6, 9, 12]
# y4 = [4, 8, 12, 16]
# plt.plot(x, y1, label = "y = x", color = "red")
# plt.plot(x, y2, label = "y = 2x", color = "orange")
# plt.plot(x, y3, label = "y = 3x", color = "green")
# plt.plot(x, y4, label = "y = 4x", color = "blue")

# plt.legend(title = "4graph", loc = "upper center", ncol=4)
# plt.title("graph sample")
# plt.xlabel("x")
# plt.ylabel("y")

# plt.show()

# 하나씩 여러개 그래프 그리기 (방법 1)

# plt.subplot(2, 2, 1)
# plt.plot(x, y1)
# plt.title("x = y")

# plt.subplot(2, 2, 2)
# plt.plot(x, y2)
# plt.title("x = 2y")

# plt.subplot(2, 2, 3)
# plt.plot(x, y3)
# plt.title("x = 3y")

# plt.subplot(2, 2, 4)
# plt.plot(x, y4)
# plt.title("x = 4y")

# plt.suptitle("sample graph")
# plt.tight_layout()
# plt.show()

# 하나씩 여러개 그래프 그리기 (방법 2)
# fig, axes = plt.subplots(2, 2)

# axes[0, 0].plot(x, y1)
# axes[0, 0].set_title("x = y")

# axes[0, 1].plot(x, y2)
# axes[0, 1].set_title("x = 2y")

# axes[1, 0].plot(x, y3)
# axes[1, 0].set_title("x = 3y")

# axes[1, 1].plot(x, y4)
# axes[1, 1].set_title("x = 4y")

# plt.tight_layout()
# plt.show()


# 막대 그래프 그리기
categories = ["A", "B", "C"]
values = [10, 15, 7]

# # plt.bar(categories, values, width=0.5, color=["r", "g", "b"], alpha=0.5, edgecolor="black", linewidth=5) # align = "edge"
# bars = plt.bar(categories, values, color= "orange", label = "Bar Graph")
# plt.xticks(categories, ["2023", "2024", "2025"])

# # 바 그래프별 텍스트 넣기
# for bar in bars:
#     plt.text(bar.get_x() + bar.get_width() / 2, # x좌표(막대의 중심)
#              bar.get_height() + 0.6, # y좌표(막대 위에다가 올리는 것)
#              str  (bar.get_height()), # 높이값 넣는거
#              ha = "center",
#              va = "top",
#              color = "black"
#              ) 

# plt.title("Bar graph")


# plt.show()


# 수평
bars = plt.barh(categories, values, color=["r", "g", "b"])

for bar in bars:
    plt.text(bar.get_width() + 0.5, # x좌표
             bar.get_y() + bar.get_height() / 2, # y좌표의 중심
             str(bar.get_width()),
             ha = "right",
             va = "center",
             color = "black"
             )
    
plt.legend(bars, ["2023", "2024", "2025"], title = "years", ncol=1)

# 기준선
plt.axvline(x = values[0], linestyle = "--")
plt.title("bar graph", pad = 10)
plt.xlabel("catergory")
plt.ylabel("year")

# plt.savefig("bar.jpg", format="jpg")

# plt.show()



