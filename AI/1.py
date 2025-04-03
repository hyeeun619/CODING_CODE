<<<<<<< HEAD
import cv2
import numpy as np

########################################################################

# # 기본창 띄우기 
# image = cv2.imread("Cat03.jpg")
# gray_image = cv2.imread("Cat03.jpg",cv2.IMREAD_GRAYSCALE) #cv2.IMREAD_COLOR : 기본값(생략가능)

# cv2.imshow("Color Image", image)
# cv2.imshow("Gray Image", gray_image)

# # cv2.waitKey(0) # 0 = 창을 무한대기, 5000 = 5초 대기
# key = cv2.waitKey(0)
# if key == ord("q"): # ord() : 문자의 아스키코드값 획득 
#     print(chr(key)) # chr() : 아스키코드값을 문자로 변경

# cv2.destroyAllWindows() #모든창 종료
########################################################################

# # 도형그리기
# width = 500
# height = 500
# canvas = np.zeros((height, width, 3), dtype=np.uint8)

# # 직선그리기 (그릴캔버스, 시작점, 끝점, 색상, 두께)
# cv2.line(canvas, (50, 50), (450, 50), (0, 255, 0), 3)

# # 사각형 그리기 (캔버스, 왼쪽상단, 오른쪽하단, 색상, 두께)
# cv2.rectangle(canvas, (50, 100), (200, 250), (255, 0, 0), 2)

# # 원 그리기 (캔버스, 중심좌표, 반지름, 색상, 두께)
# cv2.circle(canvas, (300, 200), 50, (0, 0, 255), -1) # -1 : 내부 채우기 

# # 다각형 그리기
# pts = np.array( [[250, 300], [350, 300], [150, 400]]) # 3행 2열 
# # reshape : 배열의 형태를 변경
# pts = pts.reshape((-1, 1, 2)) # -1 : 자동맞춤(3, 1, 2)
# # -1로 쓰는 이유 : 점 개수의 상관없이 자동으로 크기를 조절
# cv2.polylines(canvas, [pts], isClosed=True, color=(255, 255, 0), thickness=2) # thickness : 두께, isClosed : 도형 선 ? 닫기

# # 텍스트 추가
# cv2.putText(canvas, "Hello OpenCV", (120, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
# # FONT_HERSHEY_SIMPLEX : 기본값, 산세리프 폰트, san-serif 
# # FONT_HERSHEY_PLAIN : 작은크기의 산세리프 폰트 
# # FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체


# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

########################################################################

# 이미지 색상, 사이즈 변경
# image = cv2.imread("Cat03.jpg")

# gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # resized = cv2.resize(image, (400, 300)) #고정값으로 변경
# scale = 0.5 # 50%
# resized = cv2.resize(image, None, fx=scale, fy=scale)

# # # cv2.imwrite("CatResize.jpg", resized) # 이미지 저장

# # cv2.imshow("Gray", gray)
# # cv2.imshow("HSV", hsv)
# # cv2.imshow("Resize", resized)

# roi = image[50:200, 100:300]

# cv2.imshow("Roi", roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows(0)

########################################################################

# # x값, y값 찾기, 영역설정
# start, end = None, None


# def mouse_click(e, x, y, flag, param):
#     global start, end
#     if e == cv2.EVENT_LBUTTONDOWN:  # 클릭을 누른상태
#         print(f"마우스 누른상태 : x={x}, y={y}")
#         start = (x, y)
#     elif e == cv2.EVENT_LBUTTONUP:  # 클릭을 뗀 상태
#         print(f"마우스 뗀 상태 : x={x}, y={y}")
#         end = (x, y)
#         # 영역표시
#         roi = image[start[1] : end[1], start[0] : end[0]]
#         cv2.imshow("select", roi)


# image = cv2.imread("Cat03.jpg")
# cv2.imshow("image", image)

# # 마우스 콜백함수
# cv2.setMouseCallback("image", mouse_click)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
########################################################################

# 회전, 이동
# image = cv2.imread("Cat03.jpg")

# # 중심좌표
# (h, w) = image.shape[:2]
# center = (w//2, h//2)
# print(center)

# 회전
# matrix = cv2.getRotationMatrix2D(center, 180.0, 1.0) # 이미지 회전, 이동을 위해 사용하는 메서드 
# rotated = cv2.warpAffine(image, matrix, (w, h))

# # 이동
# matrix = np.float32([[1, 0, 100], [0, 1, 50]])
# move = cv2.warpAffine(image, matrix, (w, h))


# # cv2.imshow("rotate", rotated)
# cv2.imshow("move", move)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


########################################################################
# 실습1. 이미지처리
# 1번 이미지를 읽어서 크기 출력
img = cv2.imread("Cat03.jpg", cv2.IMREAD_COLOR)
h, w, c = img.shape
print("img.shape", img.shape)

# 2번 이미지를 흑백으로 변환 후 화면 표시
img = cv2.imread("Cat03.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Cat03_gray,jpg", img_gray)

# 3번 이미지를 50% 크기로 축소 후 새로운 창 표시
image = cv2.imread("Cat03.jpg")
scale = 0.5
resized_image = cv2.resize(image, None, fx=scale, fy=scale)
cv2.imshow("Cat03_50%.jpg", resized_image)

# 4번 이미지를 90도 회전하여 저장
image = cv2.imread("Cat03.jpg")
(h, w) = image.shape[:2]
center = (w // 2, h // 2) #중심좌표

# 90도 회전
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated_image = cv2.warpAffine(image, matrix, (w, h))

cv2.imwrite("Cat03_90.jpg", rotated_image)
cv2.imshow("Cat03.jpg", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
=======
# 한 줄 주석 (ctrl+/)
# Python 파일 실행 단축기: ctrl + F5

'''
여기는
여러줄
주석입니다
'''

"""
쌍따움표 세개도
여러줄
주석입니다
"""

print("Hello World")
print("Hello", "World")
print("Hello", "World", sep="") # seperate, 구분자자
print("010", "1234", "4321", sep="-") # 공백에 - 표시 
print("Hello", "Python", 1, 2, sep="_") # 자료형 달라도 됨
print() # print 함수 안에 아무것도 안넣으면 줄바꿈 처리 됨됨
print("1111")
print("안녕하세요, ", end="") # end 옵션 : 문장 끝에 넣고 싶은 것
print("코딩온입니다.")
print("안녕하세요 ", end=", ") # 결과 동일일
print("코딩온입니다.")

ive = "I AM"
print(ive)
ive = "장원영"
print(ive)
print(f"제가 좋아하는 가수는 {ive}입니다.") # f 문자열 포매팅
print("제가 좋아하는 가수는 ", ive, "입니다.", sep="") # 위와 결과 동일

print(type(77)) # int : 숫자형 > 정수 타입 / integer
print(type(7.2)) # float : 숫자형 > 실수 타입
print(type('i\'ve')) # <class 'str'> 출력
print(type("i\"ve")) # <class 'str'> 출력

print('i\'ve') # i've
print("i\'ve") # i've

print("i\"ve") # i"ve
print('i\"ve') # i"ve

a = 77
print(type(a))
a = 7.2
print(type(a))
a = 'ive'
print(type(a)) # str: 문자열

print("111\n111") # \n: 줄바꿈꿈
print("111\t111") # \t: 탭 (8칸)

print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\__|")

num = 10 # 10진수
b_num = 0b1010 # 2진수
h_num = 0xA # 16진수
print(num)
print(b_num)
print(h_num)

print(bin(10)) # 10진수를 2진수로 표현
print(hex(10)) # 10진수를 16진수로 표현
print(type(bin(10))) # 문자열
print(type(hex(10))) # 문자열

print(ord("0")) # ord(): 주어진 문자를 해당하는 유니코드 정수값으로 변환
print(ord("A"))
print(chr(48)) # chr(): 주어진 유니코드 정수값을 문자로 변환
print(chr(65))
>>>>>>> 9e5d526 (python 연습)
