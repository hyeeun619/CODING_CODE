# 다중 상속
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheels:
    def __init__(self, wheel_count):
        self.wheel_sount = wheel_count

class Car(Engine, Wheels): # 다중상속
    def __init__(self, horsepower, wheel_count):
        # 부모클래스의 생성자를 호출해서 hoursepower, wheel_count를 초기화
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, wheel_count)

    def info(self):
        print(f"이 자동차는 {self.horsepower} 마력과 {self.wheel_sount} 개의 바퀴를 가짐")

car = Car(100, 4)

car.info()
print(Car.mro()) # mro(): 클래스 계층구조를 나타냄
# [<class '__main__.Car'>, <class '__main__.Engine'>, <class '__main__.Wheels'>, <class 'object'>]

# 참고. <class 'object'>
# : 모든 클래스는 object 클래스를 상속하므로 object 클래스를 맨 마지막으로 검색색

# MRO (메서드 해석 순서, Method Resolution Order)
# :"다중상속"에서 메서드 호출 순서 결정하는 규칙
# ex. Car 클래스에서 메서드를 찾을 때 어떤 순서로 부모클래스들을 탐색할지 결정

# MRO

class A:
    def speak(self):
        print("A 클래스")

class B(A):
    def speak(self):
        print("B 클래스")

class C(A):
    def speak(self):
        print("C 클래스")

class D(B, C):
    pass # 아무것도 안하는 키워드

d = D()
# A, B, C 클래스 모두 speak() 메서드를 가지고 있는데, 과연 여기서 어떤 클래스의 speak()가 호출?-
# -> MRO 우너칙에 따른 클래스의 메서드가 호출이 됨
d.speak() # B 클래스
print(D.mro()) # D -> B -> C -> A -> object

# 다중상속의 유의점
# 이름이 충돌 문제가 있다