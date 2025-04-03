# 클래스 변수와 인스턴스 변수

# 클래스 변수 : "클래스에 속한" 변수 -> 모든 인스턴스(객체)가 공유하는 변수
#   ㄴ 클래스 내부, 메서드 바깥
# 인스턴스 변수 : "각각의 인스턴스에 속한" 변수 -> 각 인스턴스(객체)가 독립적으로 관리하는 변수
#   ㄴ 클래스 내부, 메서드 내부 (주로 __init__메서드 안에)

class Dog:
    kind = "진돗개" # 클래스 변수

    # 생성자자
    def __init__(self, name):
        self.name = name # 인스턴스 변수

# 클래스(설계도)로부터 인스턴스(객체)를 생성
dog1 = Dog("백구")
dog2 = Dog("초코")

# 인스턴스 변수 접근
print(dog1.name)
print(dog2.name)

# 클래스 변수 접근
# i) 인스턴스 변수를 통해 접근
# print(dog1.kind)
# print(dog2.kind)
# ii) 클래스명을 통해 접근
print(Dog.kind)

# 클래스 변수 값 변경시 어떻게 될까?
# -> 클래스 변수 값 변경시, 모든 인스턴스에 영향
Dog.kind = "말티즈"
print(dog1.kind)
print(dog2.kind)
print(Dog.kind)

###
class Example:
    shared = "공유 변수" # 클래스 변수

    def __init__(self, name):
        self.name = name # 인스턴스 변수

e1 = Example("A")
e2 = Example("B")

print(e1.name) # A
print(e2.name) # B

# 클래스 변수 변경
Example.shared = "변경된 공유 변수"

# 인스턴스 변수 변경
e1.name = "C"

print(e1.shared)
print(e2.shared) # 클래스 변수는 모든 인스턴스에 영향
print(e1.name) # 인스턴스 변수는 특정 인스턴스에만 영향
print(e2.name)

#####
print()
print()

# 사번 자동 발급
# i) 클래스 변수 사용 버전
# class Employee:
#     serial_num = 1000 # 클래스 변수

#     def __init__(self, name):
#         Employee.serial_num += 1 # 클래스 변수 값을 1 증가
#         self.id = Employee.serial_num # 사번 저장
#         self.name = name # 이름 저장

#     def __str__(self):
#         return f"사번: {self.id}, 이름: {self.name}"
    
#  ii) 인스턴스 변수 사용 버전
class Employee:
    serial_num = 1000 # 클래스 변수

    def __init__(self, name):
        self.serial_num = 1000 # 인스턴스 변수
        self.serial_num += 1 # 인스턴스가 생성되면 사번 1 증가

        self.id = self.serial_num # 사번 저장
        self.name = name # 이름 저장

    def __str__(self):
        return f"사번: {self.id}, 이름: {self.name}"
    
# -> 사번이 직원마다 "독립적으로 증가하는 이슈"

em1 = Employee("김사랑")
em2 = Employee("홍길동")
# print(em1)
# print(em2)
employee = [
    em1,
    em2,
    Employee("이몽룡"),
    Employee("심청이"),
    Employee("변사또"),
    Employee("전우치"),
]


for em in employee:
    print(em)

