<<<<<<< HEAD
# import cv2
# from ultralytics import YOLO

# model = YOLO("yolov8n.pt")  # YOLO모델 v8, n:nano버전

# image = cv2.imread("test.jpg")

# # 객체탐지
# results = model.predict(source=image, save=False, save_txt=False, conf=0.5)
# # source : 이미지
# # save : 결과 이미지를 저장할것인가?
# # save_txt : 탐지된 결과(좌표, 클래스)를 저장할것인가?
# # conf: 신뢰도 임계값.  0.5: 50%이상
# # 반환값은 탐지 결과의 리스트형태. results[0]이 이미지에 대한 결과

# # 결과 시각화
# frame = results[0].plot()
# # plot(): 탐지된 객체를 시각화한 이미지를 반환

# cv2.imshow("YOLO", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # --------------------------------- 웹캠

# import cv2
# from ultralytics import YOLO

# model = YOLO("yolov8n.pt")
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # 객체탐지
#     results = model.predict(source=image, save=False, save_txt=False, conf=0.5)

#     # 결과 시각화
#     frame = results[0].plot()

#     cv2.imshow("YOLO", frame)

#     # 종료
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


# ----------------------------- OCR
import cv2
import pytesseract

# Tesseract경로
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

# image = cv2.imread("receipt.png")

# # 흑백변환
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # tesseract를 이용해서 이미지에서 텍스트를 추출
# text = pytesseract.image_to_string(gray, lang="kor+eng")

# print("추출된 텍스트 : ", text)

# ------------------ 자동차 번호 인식
image = cv2.imread("car.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 블러
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 이진화
thresh = cv2.adaptiveThreshold(
    blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)
# adaptiveThreshold : 조명에 대응 쉬운 메서드
# blockSize: 각픽셀의 임계값을 계산할때 참조할 이웃영역의 크기. 반드시 홀수
# C: 계산된 임계값에서 차감할 상수
text = pytesseract.image_to_string(thresh, lang="kor", config="--psm 6")
print("car", text)

cv2.imshow("car", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
=======
# 튜플, Tuple
t1 = (1,) # 요소가 1개인 튜플은 반드시 쉼표 사용!
print(t1)

not_tuple = (1)
print(not_tuple) # 정수

t2 = (1, 2, 3, 4, 5, 3, 3, 3) # 괄호를 사용해 튜플 선언
print(t2)

t3 = 1, 2, 3 # 괄호 없이 쉼표만 사용 튜플 선언 가능능
print(t3)

t4 = ("a", "b", "c", ("안녕", "감자"))
print(t4) 

print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])
print(t4[:2])

print("a" in t4)
print("d" in t4)

# t4[0] = "x"
>>>>>>> 9e5d526 (python 연습)
