import numpy as np

'''
# 1차원
print([1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
a1 = np.array([1, 2, 3, 4, 5])
print(a1) # [1 2 3 4 5]

# 2차원
a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(a2)

# 3차원
a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a3)

print(a2.shape) # 배열 모양 2행 3열 , 튜플형태
print(a2. ndim) # 차원
print(a2.dtype) # 원소의 자료형
print(a2.itemsize) # 원소의 크기(바이트)
print(a2.size) # 원소의 개수


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 1]) # 2
print(arr[1, 2]) # 6

row = [0, 2]
col = [2, 2]
print(arr[row, col]) # [3 ,9]

arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 20]) # [30 40 50], 20 이상만 가져옴
print(arr[arr % 20 == 0]) # [20 40], 20으로 나눴을때 0이 나오는 값만 가져옴
arr[arr > 20] = 0
print(arr) # [10 20  0  0  0]
lists = [2, 3, 4]
print(arr[lists]) # [0 0 0], 36번 라인에서 인덱스 2, 3, 4번이 000으로 바꿔져서 000 출력


# 배열생성
zero = np.zeros( (3, 3))
print(zero)
ones = np.ones((5, 5))
print(ones)
ranges = np.arange(1, 20)
print(ranges) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
ranges1 = np.arange(1, 20, 3)
print(ranges1) # [ 1  4  7 10 13 16 19]
linespaces = np.linspace(0, 2, 10) 
print(linespaces)
# [0. 0.22222222 0.44444444 0.66666667 0.88888889 1.11111111 1.33333333 1.55555556 1.77777778 2.]


# 1차원 배열을 3x3 배열로 변환
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped = np.reshape(array, (3, 3))
print(reshaped)
resized = np.resize(array, (4, 4))
print(resized)


# 연산
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a + b) # [ 6  8 10 12]
print(a * b) # [ 5 12 21 32]

c = np.array([1, 4, 9, 16, 25, 36]) # [1. 2. 3. 4. 5. 6.]
print(np.sqrt(c)) # 제곱근, [1. 2. 3. 4. 5. 6.]
print(np.exp(c)) # 지수함수
# [2.71828183e+00 5.45981500e+01 8.10308393e+03 8.88611052e+067.20048993e+10 4.31123155e+15]
print(np.log(c)) # 자연연로그함수
# [0.         1.38629436 2.19722458 2.77258872 3.21887582 3.58351894]

angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print(angles)
print(np.sin(angles))
print(np.cos(angles))

# 합치기
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 수평합치기
print(np.hstack((a, b))) # [1 2 3 4 5 6]

# 수직합치기
print(np.vstack((a, b)))

# 열 기준 합치기
print(np.column_stack((a, b)))

# 분활하기
a = np.array([[1, 2, 3], [4, 5, 6]])
# 수평분할
h = np.hsplit(a, 3)
print(h)
# 수직분할
v = np.vsplit(a, 2)
print(v)
'''

