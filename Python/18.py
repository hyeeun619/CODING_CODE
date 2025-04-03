# 내장 함수

# abs(정수) : 절댓값 구하는 내장함수
print(abs(-77))
print(abs(0))
print(abs(10))

# 만약에, abs() 내장함수가 없었다면?
def my_abs(n):
    if n < 0: # 음수라면, 양수로 변환
        return -n
    else: # 0 혹은 양수이니 그대로 반환환
        return n

print(my_abs(-77))
print(my_abs(0))
print(my_abs(10))

# pow(x, y): x^y 구하는 내장함수
print(pow(10, 2))
print(pow(2, 10))
print(pow(3, 4))

# 만약에, pow() 내장함수가 없었다면?
def my_pow(x, y): # x: 말, y: 지수
    num = 1 # 초기값

    for _ in range(0, y): # y번 곱하는 행위를 반복
        num *= x

    return num

print(my_pow(10, 2))
print(my_pow(2, 10))
print(my_pow(3, 4))


# amp()

#  각 요소마다 적용하고 싶은 함수
def square(x):
    return x**3

numbers = [2, 4, 6, 8, 10]

print((map(square, numbers))) # <map object at 0x000001667E6A9900>
print(list(map(square, numbers))) # [8, 64, 216, 512, 1000]

# filter()
def even_numbers(x):
    return x % 2 == 0

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter(even_numbers, numbers2)) # <filter object at 0x000002361FF19CC0>
print(list(filter(even_numbers, numbers2))) # [2, 4, 6, 8, 10]


# 실습 (함수만들기)
n = int(input("숫자를 입력하세요."))
def numbers3(x):
    return x % n == 0

numbers4 = [i for i in range(1,31)]
print(numbers4)

numbers5 = (list(filter(numbers3, numbers4)))
print(list(filter(numbers3,numbers4)))
print(f"{n}의 배수의 개수: {len(numbers5)}")

# 실습 (함수만들기, 다른방법)
def count(num):
    lists = [i for i in range(1, 31) if i % num == 0]
    counts = len(lists)

    return (lists, counts)

n = 3 # 배수
my_lists, my_counts = count(n)
print(f"{n}의 배수 목록 : {my_lists}")
print(f"{n}의 개수: {my_counts}")

# print(count(n)) # ([3, 6, 9, 12, 15, 18, 21, 24, 27, 30], 10)

# 실습 (함수만들기, 다른방법)
def count(num):
    # 중첩함수 - 해당 함수 안에서만 호출 가능능
    def check(x): # num의 배수인지를 검사하는 함수수
        return x % num == 0
    lists = list(filter(check, range(1, 31)))


    return (lists, len(lists))

n = 6
my_lists, my_counts = count(n)
print(f"{n}의 배수 목록 : {my_lists}")
print(f"{n}의 개수: {my_counts}")


# 선택 실습 max(),min() 내장 함수 직접 구현해보기
# 버전 1: 매개변수가 2개만 들어온다고 가정
# 버전 2: 매개변수가 n개가 들어올 수 있음을 가정

