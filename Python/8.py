<<<<<<< HEAD
import cv2
import numpy as np
import matplotlib.pyplot as plt

############################################################
# 실습 1 

# # 이미지 읽기
# image = cv2.imread("ehgud.jpeg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이스케일로 변환

# # 가우시안 블러 적용 (노이즈 제거)
# blur = cv2.GaussianBlur(gray, (5, 5), 0)

# # 허프 변환을 이용하여 원 검출
# circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist=30,
#                            param1=50, param2=50, minRadius=1, maxRadius=50)

# # 원이 검출되었다면, 원을 이미지에 그리기
# if circles is not None:
#     circles = np.round(circles[0, :]).astype("int")  # 원의 좌표와 반지름을 정수로 변환
#     height, width = image.shape[:2]

#     for (x, y, r) in circles:
#         if x - r > 0 and x + r < width and y - r > 0 and y + r < height:
#             cv2.circle(image, (x, y), r, (0, 255, 0), 4)  # 원의 중심에 초록색 원 그리기

# # 결과 출력
# cv2.imshow('Detected Circles', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

############################################################
# 실습 2 

# # Haar cascade xml 파일 로드
# cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

# # 사람 이미지
# image = cv2.imread("black.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이스케일로 변환

# faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# # 감지된 얼굴 축소 후 확대 -> 블러 적용
# for (x, y, w, h) in faces:
#     face = image[y:y+h, x:x+w]
#     resized = cv2.resize(face, (w // 2, h // 2))  # 얼굴 영역 축소
#     enlarged = cv2.resize(resized, (w, h))  # 원래 크기로 확대
#     blur = cv2.GaussianBlur(enlarged, (5, 5), 0) # 블러 처리
#     image[y:y+h, x:x+w] = blur

# # 결과 이미지 출력
# cv2.imshow("face", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


############################################################
# # 실습 3

# import cv2

# image = cv2.imread("w.jpg")
# title = "mouse event"
# drawing = False  # 직선
# ix, iy = -1, -1 
# is_circle = False # 원원

# def onMouse(event, x, y, flags, param):
#     global ix, iy, drawing, image, is_circle

#     if event == cv2.EVENT_LBUTTONDOWN:  # 마우스를 클릭했을 때
#         if is_circle:  # 원 그리기 모드일 때
#             cv2.circle(image, (x, y), 100, (0, 0, 0), -1)
#             cv2.imshow(title, image)
#         else:  # 직선 그리기 모드일 때
#             drawing = True
#             ix, iy = x, y

#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             temp_image = image.copy()
#             cv2.line(temp_image, (ix, iy), (x, y), (0, 255, 0), 2)  # 직선 그리기
#             cv2.imshow(title, temp_image)

#     elif event == cv2.EVENT_LBUTTONUP:
#         if not is_circle:
#             drawing = False
#             cv2.line(image, (ix, iy), (x, y), (0, 255, 0), 2)
#             cv2.imshow(title, image)

# # 원 그리기와 직선 그리기 모드를 전환하는 함수
# def toggle_mode():
#     global is_circle
#     is_circle = not is_circle  # 원 그리기 모드와 직선 그리기 모드를 전환

# cv2.imshow(title, image)
# cv2.setMouseCallback(title, onMouse)

# while True:
#     cv2.imshow(title, image)

#     key = cv2.waitKey(1) & 0xFF
#     if key == 27:  # ESC를 눌러 종료
#         break
#     elif key == ord('m'):  # 'm' 키를 눌러 원 그리기와 직선 그리기 모드를 전환
#         toggle_mode()

# cv2.destroyAllWindows()


############################################################
# 실습 4

# import cv2
# import numpy as np

# # 돋보기 효과 함수
# def magnifying_glass(image, center, size=100, scale=2):
#     x, y = center
#     height, width = image.shape[:2]

#     x1, y1 = max(0, x - size), max(0, y - size)
#     x2, y2 = min(width, x + size), min(height, y + size)
    
#     magnified_region = image[y1:y2, x1:x2]
#     magnified_image = cv2.resize(magnified_region, (magnified_region.shape[1] * scale, magnified_region.shape[0] * scale))
    
#     magnified_h, magnified_w = magnified_image.shape[:2]
#     overlay_x = x - magnified_w // (2 * scale)
#     overlay_y = y - magnified_h // (2 * scale)
    
#     overlay_x = max(0, overlay_x)
#     overlay_y = max(0, overlay_y)
#     if overlay_x + magnified_w > width:
#         overlay_x = width - magnified_w
#     if overlay_y + magnified_h > height:
#         overlay_y = height - magnified_h

#     result = image.copy()
#     result[overlay_y:overlay_y+magnified_h, overlay_x:overlay_x+magnified_w] = magnified_image
    
#     return result

# # 마우스 이벤트 처리 함수
# def mouse_callback(event, x, y, flags, param):
#     global mouse_position, image_copy
#     if event == cv2.EVENT_MOUSEMOVE:
#         mouse_position = (x, y)
#         image_copy = magnifying_glass(image, mouse_position)

# image = cv2.imread('black.jpg')
# image_copy = image.copy()
# mouse_position = (0, 0)

# cv2.namedWindow('Magnifying Glass')
# cv2.setMouseCallback('Magnifying Glass', mouse_callback)

# while True:
#     cv2.imshow('Magnifying Glass', image_copy)
    
#     # 'q' 키를 누르면 종료
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()


############################################################
# 실습 5

# 이미지 읽기
image = cv2.imread("jennie.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이스케일로 변환

# 엠보싱 효과
mask1 = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
out1 = cv2.filter2D(gray, -1, mask1)

# 스케치 효과
mask2 = 255 - gray
blur = cv2.GaussianBlur(mask2, (5, 5), 0)
sketch = 255 - blur
sketch_color = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
sketch_image = cv2.divide(image, sketch_color, scale=256.0)

# 카툰 효과
cartoon = cv2.stylization(image, sigma_s=100, sigma_r=0.9)

# Matplotlib을 이용한 이미지 출력 (RGB로 변환)
plt.figure(figsize=(10, 10))

# 원본 이미지
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

# 엠보싱 효과
plt.subplot(2, 2, 2)
plt.imshow(out1, cmap='gray')
plt.title("Embossed Effect")
plt.axis('off')

# 스케치 효과
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(sketch_image, cv2.COLOR_BGR2RGB))
plt.title("Sketch Effect")
plt.axis('off')

# 카툰 효과
plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB))
plt.title("Cartoon Effect")
plt.axis('off')

# 전체 이미지 출력
plt.tight_layout()
plt.show()
=======
# 딕셔너리 (dictionary)

# 생성
# dict1 = {}
dict1 = dict()
print(dict1)

# 딕셔너리 생성
dict1 = {"name" : "홍길동", "age" : 20, "city" : "Seoul", "hobby" : ["런닝", "등산", "헬스"]}
print(dict1)

dict2 = dict(name = "홍길동", age = "21")
print(dict2)

# 값 접근하기
print(dict1["name"])
print(dict1["hobby"])
print(dict1["hobby"][2])

# 값 수정
dict1["age"] = 30
print(dict1)

# 요소 추가
dict1["birthday"] = ["19900101"]
print(dict1)

# 키 삭제
del dict1["birthday"]
print(dict1)

# 딕셔너리 메서드
fruits = {"apple" : "사과", "banana" : "바나나"}
print(fruits.get("apple"))
print(fruits.get("peach"))
# -> 존재하지 않는 키로 get 하는 경우 'None' 반환
print(fruits.get("peach", "복숭아"))
# -> 존재하지 않는 키로 검색시 기본값 설정
print(fruits)
# -> 기본값을 설정할 뿐, 딕셔너리 요소 추가 x

# 여러 요소 추가
fruits.update({"grapes" : "포도", "melon" : "멜론"})
print(fruits)
# print(fruits.key())
print(fruits.values())
print(fruits.items())

# 요소 모두 지우기
fruits.clear()
print(fruits)

# 실습
# 1번
student = {}
# 2번
student = {"Alice" : 85, "Bob" : 90, "Charlie" : 95}
print(student)

# 3번
student["David"] = 80
print(student)

# 4번
student["Alice"] = 88
print(student)

# 5번
del student["Bob"]
print(student)

>>>>>>> 9e5d526 (python 연습)
