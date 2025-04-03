# 전역변수
quantitiy = 10

def get_price(price):
    # price : 매개변수
    return price * quantitiy

print(f"{quantitiy}개의 가격은 {get_price(50000)}입니다.")

# 지역변수
def  oneUp():
    x = 0
    x += 1
    return x

print(oneUp())
# print(x) # NameError: name 'x' is not defined
print(quantitiy)

# 변수의 유효 범위
amount = 10

def price_sum(price):
    amount = 7
    print("# ", amount) # 7
    return price * amount # 14000 = 2000 * 7

result = price_sum(2000)
print(result)
print("## ", amount)  # 10

# global 키워드
x = 0
print(x)

def oneUp():
    global x # 함수 내에서 전역변수 "변경"이 이루어질 예정 힌트
    x += 1
    return x

print(oneUp())
print(oneUp())
print(oneUp())
print(x)