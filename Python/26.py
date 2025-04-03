# @property 데코레이터를 사용해 getter, setter 정의하기

class Person:
    def __init__(self, name, age):
        # 이중 밑줄(__) : 외부에서 직접 접근 막기 
        # -> 캡슐화 (getter, setter를 통해서만 접근하도록)
        self.__name = name
        self.__age = age

    # getter 메서드
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    #setter 메서드
    @name.setter
    def name(self, value):
        self.__name = value

    @age.setter
    def age(self, value):
        self.__age = value


p1 = Person("홍길동", 20)
# getter 사용
print(p1.name)
print(p1.age)

# setter 사용
p1.name = "홍길동2"
p1.age = 21

# setter로 변경된 값 출력
print(f"변경된 이름: {p1.name}")
print(f"변경된 나이: {p1.age}")