# 정보 은닉

class Person:
    def __init__(self):
        # 멤버변수 (_name, _age) 언더스코어?
        # -> protected 접근제어로 간주
        # -> 외부에서 직접 접근하지 않고, 해당/서브 클래스에서 사용
        # "직접 접근" 대신 -> getter/setter 를 이용해서 값을 읽거나/수정하도록 함 -> 데이터 보호
        self._namename = ""
        self._age = 0

    def setname(self, name):
        self._name = name

    def getname(self):
        return self._name
    
    def setage(self, age):
        self._age = age

    def getage(self):
        return self._age
    
p1 = Person()
p1.setname("흥부")
p1.setage(35)
print("이름: ", p1.getname())
print("나이: ", p1.getage())

p2 = Person()
p2.setname("놀부")
p2.setage(38)
print("이름: ", p2.getname())
print("나이: ", p2.getage())

# 실습 1
class Supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        return f"위치: {self.location}"

    def change_category(self,new_prodaut):
        self.product = new_prodaut
        return self.product

    def show_list(self):
        return f"상품 {self.product}"

    def enter_customer(self, customer):
        self.customer += 1
        return self.customer

    def show_info(self):
        return f"위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}"

super = Supermarket("마포","마켓온","음료",11)

print(super.print_location())
print(super.change_category("과자"))
print(super.show_list())
print(super.enter_customer(super.customer))
print(super.show_info())

# 실습 2
# class health():
#     def __init__(self,name, hp):
#         self.name = name
#         self.hp = hp
#         self.hour = 0
#         self.al = 0
#     def a1(self, hour):
#         self._hour = hour