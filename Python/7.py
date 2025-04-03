<<<<<<< HEAD
# import cv2
# import numpy as np

# # 이미지 로드
# image = cv2.imread("fu.jpeg")

# # 이미지 색상 변환 (BGR -> HSV)
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # 초록색 범위 설정
# green_lower = np.array([35, 50, 50])
# green_upper = np.array([85, 255, 255])

# # 초록색 영역 마스크 생성
# green_mask = cv2.inRange(hsv_image, green_lower, green_upper)

# # 마스크에 가우시안 블러 적용
# green_mask = cv2.GaussianBlur(green_mask, (5, 5), 0)

# # 마스크에 모폴로지 연산 (열림) 적용
# green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

# # 외곽선 검출
# contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > 100]

# # 결과 출력
# print(f"검출된 초록색 물체 개수: {len(filtered_contours)}")

# # 사각형 그리기
# output_image = image.copy()
# for contour in filtered_contours:
#     x, y, w, h = cv2.boundingRect(contour)
#     cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # 이미지 출력
# cv2.imshow("Original Image", image)
# cv2.imshow("Green Color Mask", green_mask)
# cv2.imshow("Detected Contours", output_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

image = cv2.imread("green.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([50, 100, 100])
upper = np.array([70, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

# result = cv2.bitwise_and(image, image, mask=mask)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count = 0
for contour in contours:
    # contourArea : 위에서 검출한 윤곽선의 면적을 계산하는 함수. 반환값은 면적을 float형식
    area = cv2.contourArea(contour)
    if area > 100:  # 작은 노이즈 제거
        count += 1
        x, y, w, h = cv2.boundingRect(
            contour
        )  # 객체를 감싸는 가장 작은 축에 정렬된 사각형
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

print(f"검출된 초록색은 : {count}개")
cv2.imshow("green", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
=======
# 셋 (set)

s1 = {1, 2, 3, 4} # 중복 허용 x
print(s1)

s1.add(5) # 원소 추가
print(s1)

# update() : 다른 set, list, tuple의 요소들을 현재 집합에 추가하는 기능
s1.update([6, 7, 8, 9, 10]) 
print(s1)

s1.remove(3)
print(s1)
# s1.remove(100) # KeyError: 100 존재하는 요소만 삭제 가능

s1.discard(9) # 요소 삭제제
s1.discard(100) # 존재하지 않는 요소 삭제해도 오류 발생 x
print(s1)

s1.clear()
print(s1)

# set 연산
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 합집합
s3 = s1.union(s2)
print(s3)

s3 = s1 | s2
print(s3)

# 교집합
# s3 = s1.intersection(s2)
s3 = s1 & s2
print(s3)

# 차집합
# s3 = s1.difference(s2)
# s3 = s1 - s2

# s3 = s2.difference(s1)
s3 = s2 - s1
print(s3)

# in 키워드
print(1 in s1)
print(100 in s1)

# len()
print(len(s1))
>>>>>>> 9e5d526 (python 연습)
