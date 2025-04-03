# calculator.py

#  함수
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# 변수
PI = 3.141592

# 클래스
class Calculator:
    def multiply(self, a, b):
        return a * b

# 퀴즈
# calculator 모듈 기능 추가해서 37.py에 사용하는 코드까지 작성

# 1. divide(x, y) 함수
def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없음"
    else:
        return x / y
    
# 2. 자연로그 e 2.718 변수
e = 2.718

# 3. Calculator 클래스에 제곱을 구하는 square(x)메서드
class Calculator:
    def square(self, x):
        return x ** 2
    