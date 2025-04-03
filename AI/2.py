<<<<<<< HEAD
import cv2
import matplotlib.pyplot as plt
import numpy as np

# image = cv2.imread("test_image.jpg")
# # BGR -> RGB 변경
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# plt.figure(figsize=(10, 10))

# # 원본
# plt.subplot(2, 2, 1)
# plt.imshow(image_rgb)
# plt.title("original")
# plt.axis("off")

# # 블러링
# # 평균블러
# blurred = cv2.blur(image_rgb, (5, 5))
# plt.subplot(2, 2, 2)
# plt.imshow(blurred)
# plt.title("blur")
# plt.axis("off")

# # 가우시안블러
# # gaussian = cv2.GaussianBlur(image_rgb, (5, 5), 0)
# # plt.subplot(2, 2, 3)
# # plt.imshow(gaussian)
# # plt.title("gaussian")
# # plt.axis("off")

# # 미디안 블러
# median = cv2.medianBlur(image_rgb, 5)
# plt.subplot(2, 2, 4)
# plt.imshow(median)
# plt.title("median")
# plt.axis("off")

# # 엣지강조
# # 샤프닝커널
# kernel = np.array([[0, -1, 0], [-1, 7, -1], [0, -1, 0]])

# # 필터적용
# sharped = cv2.filter2D(median, -1, kernel)

# plt.subplot(2, 2, 3)
# plt.imshow(sharped)
# plt.title("kernel")
# plt.axis("off")

# 엣지 추출
image = cv2.imread("test_image.jpg", cv2.IMREAD_GRAYSCALE)

# sobel
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3) # x방향 미분
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3) # y방향 미분
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("original")
plt.axis("off")

# plt.subplot(2, 2, 2)
# plt.imshow(sobel_combined, cmap="gray")
# plt.title("sobel")
# plt.axis("off")

# # laplacian
# laplacian = cv2.Laplacian(image, cv2.CV_64F)
# plt.subplot(2, 2, 3)
# plt.imshow(laplacian, cmap="gray")
# plt.title("laplacian")
# plt.axis("off")

# canny
canny = cv2.Canny(image, 100, 300)
plt.subplot(2, 2, 4)
plt.imshow(canny, cmap="gray")
plt.title("canny")
plt.axis("off")

########################################################################
# 컨투어
image2 = cv2.imread("test_image.jpg") # 원본이미지 추가 
# 이진화처리
_, binary = cv2.threshold(canny, 127, 255, cv2.THRESH_BINARY)

# 컨투어감지
contour, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 컨투어 원본에 그리기
# result_image = image.copy()
cv2.drawContours(image2, contour, -1, (0, 255, 0), 2)

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("contour")
plt.axis("off")

# 컨투어 계산
for i in contour:
    # 면적계산
    print(f"면적 : {cv2.contourArea(i)}")

    # 중심점계산
    M =cv2.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00']) # x중심
        cy = int(M['m01'] / M['m00']) # y중심
        # m00 = 면적, m10 = x좌표에 대한 1차모멘트, m01 = y좌표에 의한 1차모멘트

        # 중심점표시
        cv2.circle(image2, (cx, cy), 5, (0, 0, 0), -1)
    else:
        print("컨투어 면적이 0")
        
    # 둘레 계산
    print(f"둘레 : {cv2.arcLength(i, True)}")

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
=======
print(3+2) # 5
print(3-2) # 1
print(3*2) # 6
print(3/2) # 1.5
print(3//2) # 1
print(3%2) # 1
print(3**2) # 9

print(3.25//2) # 1.0
print(3.25%2) # 1.25

print(1+(2*(3**2))) # 19
# 1+(2*9) -> 1+18 -> 19
print(1+2*-3**2) # -17
# 1+2*-9 -> 1+(-18) -> -17

# 30개의 빵을 4명이 나눠가질 때 몫/나머지 구하기기
print(f"빵의 개수 {30 // 4}")
print(f"남은 빵의 개수: {30 % 4}")

a = 1
print(a) # 1
a += 1 # a = a + 1
print(a) # 2

print("장원영"+"럭키비키")
print("럭키"*10)
>>>>>>> 9e5d526 (python 연습)
