# 리스트 내포
# 파이썬에서 리스트를 간결하게 생성하는 문법
"""
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)

squares2 = [n**2 for n in range(1, 6)]
print(squares2)

# 조건문과 함께 사용
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)

"""

# 실습 1

num = int(input("몇단을 출력할까요?"))
for i in range(1,10):
    print(f"{num}x{i}={num*i}")
    
# 실습 2
num = int(input("어디까지 계산할까요? :")) # 9
total = 0
for i in range(1,num+1,2): # 1 ~ 9
    total += i
    print(f"1부터 {num}까지의 홀수의 합 : {total}")

# 실습 3
student_dic = {
    "student1" : [83, 92, 88],
    "student2" : [90, 79, 86],
    "student3" : [88, 86, 94]
}
kor = 0
eng = 0
math = 0

for i in student_dic.values():
    kor += i[0]
    eng += i[1]
    math += i[2]

print(f"국어: {kor/3: .2f}점, 영어 {eng/3: .2f}점, 수학 {math/3: .2f}점")

# 실습3 다른 방법
