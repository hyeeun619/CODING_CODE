# 정적 메서드 static method

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def minus(a, b):
        return a - b
    
print(MathUtils.add(30, 40))
print(MathUtils.minus(30, 10))
    
# (정적메서드 사용하지 않고 ) 일반함수로 정의한 경우
# -> 클래스 외부에서 함수가 독립적으로 존재.
# 함수들이 어떤 맥락에서 사용되는지 직관적으로 알기 어려울 수 있음

def add(x, y):
    return x + y

def minus(x, y):
    return x - y
    
print(add(30, 40))
print(minus(30, 10))

# Static Method
# - @staticmethod 데코레이터 사용
# - self, cls와 같은 첫번째 매개변수가 필요하지 않음
# - 클래스 변수나 인스턴스 변수에 접근 불가
# - 유틸리티 함수처럼 사용