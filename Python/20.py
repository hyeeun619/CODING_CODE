# 람다식

def add(x, y): # 일반 함수
    return x + y

print(add(3, 4))

add2 = lambda x, y: x + y # 람다식
print(add2(4, 5))

# 매개변수가 1개인 람다식
square = lambda x: x**2
print(square(5))
print((lambda x: x**2)(5)) # 13, 14 동일

# 매개변수가 2개인 람다식
mul = lambda x, y: x * y
print(mul(3, 7))
print((lambda x, y: x *y)(3, 7))

# 람다 함수를 매개변수로 전달

# call(): 함수를 인수로 받아서 그 함수를 10번 호출하는 함수
def call(func):
    for _ in range(10):
        func() # 전달받은 함수를 호출

# hello() : 일반 함수로, "안녕" 문자 출력
def hello():
    print("안녕")

# 람다식으로 정의된 함수 hello2
hello2 = lambda: print("하이")

call(hello) # call 함수에 hello 함수를 전달해서 10번 실행
call(hello2) # call 함수에 hello2 람다식을 전달해서 10번 실행

# 고차함수(map, filter 등)와 함께 쓰이는 람다식
# 참고. 고차함수?
# : 함수를 인수로 받을 수 있고, 함수를 변환 할 수 있다.

# map, filter 와 함께 쓰는 람다식
def square(x):
    return x**3

numbers = [2, 4, 6, 8, 10]

print((map(square, numbers))) # 일반함수
print(list(map(lambda x: x**3, numbers))) # 람다식

# 2. 람다식 with filter()
def even_number(x):
    return x % 2 == 0


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(even_number, numbers2)))  # 일반함수
print(list(filter(lambda x: x % 2 == 0, numbers2)))  # 람다식

# map, filter 두 개를 람다식과 함께 사용
# 3-1. 짝수만 남겨서 -> filter
# 3-2. 그 제곱을 계산 -> map

even_squared_nums = list(map(lambda x : x**2 ,filter(lambda x : x % 2 == 0, numbers2)))
print(even_squared_nums)

def test():
    print("하이")
result = test() # 하이
print(result) # None