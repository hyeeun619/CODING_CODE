# 실습 Supermarket 클래스

class Supermarket:
    total_cutomer = 0
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
        Supermarket.total_cutomer += customer

    def print_location(self):
        print(f"위치: {self.location}")

    def change_cetegory(self, new_product):
        self.product = new_product

    def show_list(self):
        print(f"상품: {self.product}")
    
    def enter_customer(self):
        # self.customer += 1
        Supermarket.total_cutomer += 1

    def show_info(self):
        # print(f"위치 {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}")
        print(f"위치 {self.location}, 이름: {self.name}, 상품: {self.product}, 총 고객수: {self.total_cutomer}")

s1 = Supermarket("마포구 도화동", "마켓온", "음료", 10)
# 새로운 고객이 방문 -> 고객 수 1 증가
s1.enter_customer() 
# 슈퍼마켓 관련 정보 출력
s1.print_location()
s1.show_list()
s1.show_info()

# 상품 카테고리 변경
# print("** 상품 카테고리를 변경합니다. **")
# s1.change_cetegory("빵") # 상품 카테고리를 "빵"으로 변경
# s1.show_list() # 변경된 상품 목록 출력

print("------------")
s2 = Supermarket("마포구 염리동", "염리마켓", "아이스크림", 20)
s2.enter_customer() 
s2.print_location()
s2.show_list()
s2.show_info()
