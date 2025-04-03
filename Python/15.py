# 함수

# 1. 매개변수x, 리턴값x
# 함수 정의
def say_hello():
    print("Hello, World")

say_hello() # 함수 호출

# 2. 매개변수o, 리턴값x
#2-2. 매개변수 1개
def  print_gretting(name): # 함수 정의
    print(f"Hello, {name}")

print_gretting("Allie") # 함수 호출
print_gretting("Martin")

#2-2. 매개변수 2개
def gugudan(dan, end): # 함수 정의 
    print(f"{dan}단")

    for i in range(1, end): # 1~end-1
        print(f"{dan} x {i} = {dan * i}")

gugudan(7, 15) # 함수 호출
gugudan(4, 20)

# 3. 매개변수x, 리턴값o
def mul_numbers(): # 함수 정의
    print("곱셈을 시작합니다.")
    return 10*5

result = mul_numbers() # 함수 호출
print(result)
print(mul_numbers())

# 매개변수o, 리턴값o
def add_numbers(x,y):
    print("덧셈을 시작합니다.")
    return x + y

result2 = add_numbers(40, 50)
print(result2)
print(add_numbers(40, 50))
print(add_numbers(10, 30))

# 다양한 타입을 return 하는 함수
# 1. List 타입을 반환하는 함수
# ex. 0부터 제한값(limit) 미만의 짝수를 출력하는 함수
def print_even_numbers(limit):
    return [ i for i in range(limit) if i % 2 == 0]

print(print_even_numbers(10))

# 2. Dictionary 타입을 반환하는 함수
def print_user_info(name, grade):
    return{"user_name": name, "user_grade":grade}

print(print_user_info("Allie",2))
print(print_user_info("Bob",4))


# 3. set 타입을 반환하는 함수수
# 문자열을 set 타입으로 변환 => 고유한 문자들만 남긴다.
# print(set("Hello"))
def print_unique_char(word):
    return set(word)

print(print_unique_char("Hi, My name is Sean"))

# 4. Tuple 타입을 반환하는 함수
# ex. 두 숫자의 합과 곱을 동시 반환 => (합, 곱)
def calculate_sum_and_product(a,b):
    return(a + b, a * b)

print(calculate_sum_and_product(3, 5))
print(calculate_sum_and_product(7, 8))

# Collection (컬렉션)
# 혼합 컬렉션
# ex. 딕셔너리 안에 리스트가 있는 예시
# def split_numbers():
#     even_nums = [ n for n in split_numbers if n % 2 == 0] # 리스트
#     odd_nums = [ n for n in split_numbers if n % 2 != 0] # 리스트

#     # 반환값 (딕셔너리)
#     return {"odd": odd_nums, "even": even_nums}

# print(split_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# {"odd": [1, 3, 5, 7, 9], "even": 짝수 리스트}

# 매개변수로 리스트를 받는 함수
# ex. 각 요소를 2배로 만드는 함수
def double(nums):
    return [i * 2 for i in nums]

print(double([1, 2, 3, 4]))

# ex. 각 요소를 문자열로 변환하는 함수
def to_string(nums):
    return[str(i) for i in nums]

print(to_string([8, 16, 24]))


# 실습 1
def numbers_a(x, y):
    if x == y:
        return f"결과(곱):{x * y}"
    else:
        return f"결과(합):{x + y}"
x = int(input("x 입력:"))
y = int(input("y 입력:"))
print(numbers_a(x, y))

# 실습 2
def print_a(x):
    if x >= 20000:
        return f"배송비 포함:{x}"
    else:
        return f"배송비 포함x:{x + 2500}"
x = int(input("상품 가격을 입력하세요. :"))
print(print_a(x))


