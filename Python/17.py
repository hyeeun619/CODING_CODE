# 매개변수

# 기본 매개변수
# 주의. 기본값이 있는 매개변수는 맨 뒤에 와야 함
def pr_str(txt="안녕하세요", count=1):
    # print(txt, count)
    for _ in range(count):
        print(txt)

    # 반복문에서 "_" : 반복변수를 사용하지 않을 때 사용하는 관례적인 이름

pr_str()
pr_str("하이", 3)
pr_str("안녕", 7)
pr_str("빠이")

# 함수 호출 키워드
def intro(name, age, city):
    print(f"이름은 {name}이고 나이는 {age}이고, 사는곳은 {city}입니다.")

intro("Allie", 23, "seoul")
intro(city = "seoul", name = "Allie", age = 23)
intro("Allie", city = "seoul", age = 23) # 위치 매개변수가 가장 먼저 와야 함

# 가변 매개변수
def calc_avg(*args):
    print(args)  # tuple

    total = 0
    for i in args:
        total += i
    avg = total / len(args)

    return avg


print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8))
print(calc_avg(10, 20, 30))

# 다른 예시
def text_def(a, b, *args):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")

text_def("Hi", 100, 9, 7, 5, 3, 1)

# 가변 키워드 매개변수
def print_info(**kwargs):
    # print(kwargs) # dictionary
    for key, value in kwargs.items():
        print(f"{key}의 값은 {value} 입니다.")

print_info(name = "홍길동", city = "서울", gender = "남자")
print_info(name = "성춘향", city = "부산", age = 30)