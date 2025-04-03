import cv2
import matplotlib.pyplot as plt
import numpy as np

# HSV
image = cv2.imread("test_image.jpg")

# # BGR -> HSV 변환
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # cv2.imshow("hsv", hsv_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # 색상범위 설정(빨간색)
# # lower = np.array([0, 120, 70])
# # upper = np.array([10, 255, 255])

# # 색상범위 설정(파란색)
# # lower = np.array([90, 100, 100])
# # upper = np.array([120, 255, 255])

# # 색상범위 설정(초록색)
# lower = np.array([50, 100, 100])
# upper = np.array([70, 255, 255])

# # 마스크 생성
# mask = cv2.inRange(hsv_image, lower, upper)

# # 원본이미지에 마스크 적용
# result = cv2.bitwise_and(image, image, mask=mask)

# plt.figure(figsize=(12, 4))

# # 원본 
# plt.subplot(1, 3, 1)
# plt.title("original")
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis("off")

# # 마스크
# plt.subplot(1, 3, 2)
# plt.title("mask")
# plt.imshow(mask, cmap="gray")
# plt.axis("off")

# # 결과
# plt.subplot(1, 3, 3)
# plt.title("result")
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.axis("off")

# plt.show()

# erode, dilate
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# lower = np.array([100, 150, 0])
# upper = np.array([140, 255, 255])

# # 마스크 생성
# mask = cv2.inRange(hsv, lower, upper)

# # 커널
# kernel = np.ones((5, 5), np.uint8)

# # 침식연산: 작은 노이즈 제거 등, 객체의 경계를 줄임
# mask_eroded = cv2.erode(mask, kernel, iterations=1) # None : 3*3 기본커널

# # 팽창연산 : 객체의 경계를 확장하거나 침식 후 복원
# mask_dilated = cv2.dilate(mask, kernel, iterations=1)

# fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# axes[0, 0].set_title("orginal")
# axes[0, 0].axis("off")

# axes[0, 1].imshow(mask, cmap="gray")
# axes[0, 1].set_title("mask")
# axes[0, 1].axis("off")

# axes[1, 0].imshow(mask_eroded, cmap="gray")
# axes[1, 0].set_title("erode")
# axes[1, 0].axis("off")

# axes[1, 1].imshow(mask_dilated, cmap="gray")
# axes[1, 1].set_title("dilate")
# axes[1, 1].axis("off")

# plt.tight_layout()
# plt.show()

# 스킨 검출
image = cv2.imread("jennie.jpeg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 피부색 범위
# H : 0~20, S : 48~255, V: 80~255
lower = np.array([0, 48, 80])
upper = np.array([20, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

# 노이즈 제거
kernel = np.ones((5, 5), np.uint8)

# 침식연산
mask_eroded = cv2.erode(mask, kernel, iterations=1)

# 팽창연산
mask_dilated = cv2.dilate(mask, kernel, iterations=1)

# 컨투어 윤곽선
# 우리가 원하는 영역 => 마스크 된 부분 
contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 원본 이미지에 윤곽선을 그리기
image_copy = image.copy()
cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title("orginal")
axes[0, 0].axis("off")

axes[0, 1].imshow(mask, cmap="gray")
axes[0, 1].set_title("mask")
axes[0, 1].axis("off")

axes[1, 0].imshow(cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB))
axes[1, 0].set_title("erode")
axes[1, 0].axis("off")

plt.tight_layout()
plt.show()