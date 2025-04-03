import matplotlib.pyplot as plt
from matplotlib import font_manager

# 폰트 경로
path = "Pretendard-Medium.ttf"
font_prop = font_manager.FontProperties(fname=path)
font = font_manager.FontProperties(fname=path).get_name()
plt.rc("font", family=font)


# 실습1. 그래프 그리기
# months = ["jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# sales_2019 = [100, 120, 140, 110, 130, 150, 160, 170, 180, 200, 190, 210]
# sales_2020 = [90, 110, 130, 120, 140, 160, 170, 160, 150, 180, 200, 190]

# plt.plot(months, sales_2019, label = "2019", color = "blue")
# plt.plot(months, sales_2020, label = "2020", color = "orange")
# plt.legend(loc = "upper left", ncol=1)
# plt.title("Monthly Sales Comparison (2019-2020)")
# plt.xlabel("Month")
# plt.ylabel("Sales")

# plt.show()


# 실습2. 그래프 그리기
# categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5"]
# data = [20, 35, 15, 27, 45]

# bars = plt.bar(categories, data, color= "lightsteelblue") # 그래프 설정 
# plt.grid(True, axis="both", linestyle="-", color="black", alpha=0.1) # 그리드 설정

# plt.title("Bar Chart", fontsize=10) 
# plt.xlabel("Categories", labelpad=10, fontsize = 8)
# plt.ylabel("Values", labelpad=10, fontsize = 8) 
# plt.ylim([0, 50]) # y축 최대값 설정
# plt.xticks(rotation=45, fontsize = 5) # x축 글꼴 기울기 설정
# plt.yticks(fontsize = 5)

# plt.show()

# 실습3. 그래프 그리기
# labels = ["Apple", "Grapes", "Melon", "Banana"]
# sizes = [34, 18, 16, 32]
# explode = explode=[0.07, 0.1, 0, 0.08]
# colors = ["r", "purple", "g", "y"]

# plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%",explode=explode,
#         wedgeprops={"edgecolor":"black","width": 0.75}, startangle=70, labeldistance=1.4)
# plt.gca().invert_xaxis()

# plt.show()