# for 문

# range 함수
for i in range(5): # range(0,5):
    print(i, end = "")
print()

for i in range(2, 7):
    print(i, end = "")
print()

for i in range(11, 20, 2):
    print(i, end = "")
print()

for i in range(10, 0, -3):
    print(i, end = "")
print()

# 리스트와 for 문
fruits = ["사과", "바나나", "포도", "체리"]
for fruit in fruits:
    print(fruit, end ="|")
print()

# 합계 구하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for num in numbers:
    total += num
    print("현재 total >>", total)
print(f"합계는 {total}입니다.")
print()


# 조건문과 함께 사용
for num in numbers:
    if num % 2 == 0:
        print(num, end = "")
print()

# 딕셔너리와 for 문
my_dic = {
    "name" : "홍길동",
    "address" : "서울시 은평구",
    "gender" : "남자",
    "hobby" : ["런닝", "헬스", "낚시"],
}

# key 값만 순회 
for i in my_dic:
    print(i, end = " ")
print()

print(my_dic.keys())
# 명시적으로 key 값만 순회
for i in my_dic.keys():
    print(i, end = " ")
print()

# values 값만 순회회
print(my_dic.values())
for i in my_dic.values():
    print(i, end = " ")
print()

# key, values 함께 순회
for key, value in my_dic.items():
    print(f"{key}:{value}")