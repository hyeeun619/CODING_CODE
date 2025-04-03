import math, random

print(math.pi) # 파이값 출력
print(math.sqrt(25)) # 제곱근
print(math.factorial(4)) # 팩토리얼

print(math.ceil(3.14)) # 올림
print(math.floor(3.14)) # 내림
print(round(3.14)) #반올림
print(round(3.74)) 
# 참고. round() 함수는 math 모듈에 속한 함수가 아닌 파이썬 내장 함수

 # a,b 모두 포함하여 임의의의 정수 리턴
rand_int = random.randint(1, 10) 
print(f"randint: {rand_int}") 

# a, b 모두 포함하여 임의의 실수 리턴
rand_float = random.uniform(1.5, 6.5)
print(f"uniform: {rand_float}") 

# 0 <= x < 1 사이의 임의의 실수 리턴 (1 미포함)
rand_between = random.random() 
print(f"random: {rand_between}")

# a <= x < b 사이의 점수 리턴 (b 미포함)
rand_range = random.randrange(10, 1000)
print(f"randrange: {rand_range}")

# 리스트에서 무작위로 하나 선택
nums = [1, 2, 3, 4, 5, 6, 7]
rand_choice = random.choice(nums)
print(f"choice: {rand_choice}")

# sample(population, k)
# - population: 모집단 (리스트, 튜플, 문자열, range())
# - k: 선택할 요소 개수
# : population에서 k만큼 무작위 추출 (k 값은 population보다 클 수 없음)
fruits = ["사과", "오렌지", "바나나", "포도", "귤"]
rand_sample = random.sample(fruits, 2)
print(f"sample: {rand_sample}")

# 실습 - 로또 방법 1
import random

nums = random.sample(range(1, 46), 6)
nums.sort()
print(nums)

# 실습 방법 2
# 1. 빈 set 만들기
lotto_nums = set()

# 2. 6개의 숫자 뽑기
while len(lotto_nums) < 6:
    # 난수를 set에 추가
    lotto_nums.add(random.randint(1, 45))

# 3. 오름차순 정렬
sorted_lotto_nums = sorted(lotto_nums)
print(sorted_lotto_nums)