# 재귀함수

def sos(i):
    print(f"{i}번째 도움 요청")

    if i == 1:
        return""
    else:
        return sos(i -1)
    
sos(10)


# ex. 팩토리얼

def fectorial(n):
    print("n >>", n)
    if n == 1:
        return 1
    else:
        return n * fectorial(n - 1)
    
print(fectorial(3))
print(fectorial(5))
print(fectorial(7))

# 실습 2 피보나치 수열 만들기

def fi(i):
    return fi(i - 1) + fi(i - 2) if (i > 2) else + 1

print(fi(11))

# 실습 2 피보나치 수열 만들기
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibo(n - 1) + fibo(n - 2)

print(fibo(6))
