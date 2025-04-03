# 예외처리
# try:
#     x = int(input("숫자를 입력하세요"))
#     result = 10 / x

# except ZeroDivisionError as e:
#     print("예외메시지 : ", e)
# except ValueError as e:
#     print("예외메시지 : ", e)
# else:
#     print(f"result는 {result}")
# finally:
#     print("프로그램을 종료합니다.")


# 예외가 없을 시
# x = int(input("숫자를 입력하세요"))
# result = 10 / x


# 하나로 쓰는 방법
# try:
#     x = int(input("숫자를 입력하세요"))
#     result = 10 / x

# except (ZeroDivisionError, ValueError) as e:
#     print("예외메시지 : ", e)
# except ValueError as e:
#     print("예외메시지 : ", e)
# else:
#     print(f"result는 {result}")
# finally:
#     print("예외처리을 종료합니다.")


# raise
def dicide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b

try:
    result = dicide(10, 0)
except ZeroDivisionError as e:
    print("예외발생", e)
else:
    print(result)