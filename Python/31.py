# 클래스 메서드

# i) 대체 생성자(Alternative Constructor) 패턴
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name, age)  # Person(name, age)


p1 = Person("김철수", 20)  # 기본 생성자로 객체 생성
p2 = Person.from_birth_year("홍길동", 1990)  # 생년도를 이용해 대체생성자로부터 객체 생성

print(f"{p1.name}: {p1.age}")
print(f"{p2.name}: {p2.age}")

# ii) 유틸리티 함수 구현
# 유틸리티 함수? 여러 곳에서 재사용할 수 있는 특정한 기능을 하는 독립적인 함수
# ex. 마일 단위를 킬로미터 단위로 변환
class Converter:
    conversion_rate = 1.60934 # 클래스 변수

    @classmethod
    def miles_to_km(cls, mile):
        # cls.conversion_rate -> Converter.conversion_rate
        return mile * cls.conversion_rate
    
my_mile = 7
print(Converter.miles_to_km(my_mile))
# 객체 생성없이 바로 클래스.메서드명() 으로 사용 가능

# iii) 클래스 변수 수정
# ex. 모든 인스턴스가 공유하는 값을 관리해야 할 때
class Counter:
    count = 0 # 클래스 변수

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
print(Counter.get_count())
Counter.increment()
print(Counter.get_count())

# iv) 자식 클래스의 정보 유지
class Animal:
    species = "동물"

    @classmethod
    def get_species(cls):
        # cls : 메서드를 호출한 실제 클래스
        # -> 상속 관계에서 자식 클래스의 값을 올바르게 찾아서 보여줌
        return cls.species # Animal.species
    
class Dog(Animal):
    species = "진돗개"

print(Animal.get_species()) # 동물
print(Dog.get_species()) # 진돗개

# 인스턴스(객체)마다 수행해야하는 작업이 동일한 경우
# 단위변환, 문자열 대소문자 변환, 리스트에서 중복값 제거, 날짜 계산, 문자열이 숫자기호로만 이루어져 있는지 검사

# Class Method 정리
# - @classmethod 데코레이터 사용
# - 첫번째 매개변수 cls(클래스) 받음
# - (인스턴스를 생성하지 않고) 클래스 자체를 통해 호출 가능 
# - 클래스 속성에 접근하거나 수정할 때 사용 가능 (iii 예시)
# - 상속시 cls는 하위클래스 참조 (가르킴, 바라봄) (iv 예시)

# vs. Insatnce Method 정리
"""
class Exclass:
    def instance_method(self):
        return "인스턴스 메서드임"
"""
# - 일반적인 메서드로, 첫번째 매개변수로 self(자기자신, 호출된 인스턴스(객체))
# - 인스턴스를 생성한 후에, 인스턴스를 통해 호출하고 인스턴스 속성에 접근 가능
# - 객체의 상태를 변경하거나 접근할 때 사용