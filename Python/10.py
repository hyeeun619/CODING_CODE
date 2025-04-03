<<<<<<< HEAD
# import cv2
# import mediapipe as mp
# import numpy as np

# # MediaPipe 손 추적 모델 초기화
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
# mp_drawing = mp.solutions.drawing_utils

# # 그림을 그릴 캔버스 (검은 배경)
# canvas = None
# last_x, last_y = None, None  # 이전 손가락 끝 위치 저장

# # 웹캠 영상 캡처
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("웹캠을 열 수 없습니다.")
#     exit()

# # 손가락 끝을 연결하여 그림을 그리는 함수
# def draw_on_canvas(image, landmarks):
#     global canvas, last_x, last_y
#     if canvas is None:
#         # 처음에는 검은 배경으로 캔버스를 생성
#         canvas = np.zeros_like(image)

#     # 손가락 끝 좌표 추출 (검지 끝을 기준으로 선을 그릴 수 있도록)
#     finger_tip = mp_hands.HandLandmark.INDEX_FINGER_TIP
    
#     # 손가락 끝 좌표
#     x, y = int(landmarks.landmark[finger_tip].x * image.shape[1]), int(landmarks.landmark[finger_tip].y * image.shape[0])

#     # 이전 좌표가 존재하면 선을 그리기 (손가락 끝을 기준으로 선을 그림)
#     if last_x is not None and last_y is not None:
#         cv2.line(canvas, (last_x, last_y), (x, y), (0, 255, 0), 5)  # 녹색 선

#     # 현재 좌표를 마지막 좌표로 저장 (다음 프레임에서 선을 그리기 위해)
#     last_x, last_y = x, y

#     # 캔버스에 그려진 내용을 원본 이미지에 덧씌우기
#     image_with_canvas = cv2.addWeighted(image, 1, canvas, 0.5, 0)

#     # 이미지를 화면에 표시
#     cv2.imshow("Canvas Drawing", image_with_canvas)

# # 손 추적 및 그림 그리기
# while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#         print("이미지 캡처 실패")
#         break

#     # BGR 이미지를 RGB로 변환 (mediapipe는 RGB 이미지 처리)
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # 손 추적
#     results = hands.process(image_rgb)

#     # 손이 감지되면 랜드마크 그리기
#     if results.multi_hand_landmarks:
#         for landmarks in results.multi_hand_landmarks:
#             # 손의 랜드마크를 연결하여 그리기
#             mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)

#             # 손가락 끝에 선을 그려서 그림을 그리기
#             draw_on_canvas(image, landmarks)

#     # 이미지 표시
#     cv2.imshow("Hand Finger Tracking", image)

#     # 'q' 키를 눌러 종료
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # 리소스 해제
# cap.release()
# cv2.destroyAllWindows()
=======
# 조건문

age = 17

# if 문문
# if age < 20: # 17 < 20 -> True
#     print("미성년자 입니다.")

# if age >= 20:
#     print("성인 입니다.")

# print(f"나이는 {age}(세) 입니다.")

# else 문
if age < 20: # 1~19
    print("미성년자 입니다.")
else: # 20~
    print("성인입니다.")

# elif 문 (else if)
age = int(input("나이를 입력하세요."))

if age < 20:
    print("10대 입니다.")
elif age < 30:
    print("20대 입니다.")
elif age < 40:
    print("30대 입니다.")
elif age < 50:
    print("40대 입니다.")
else:
    print("50대 이상입니다.")

# 실습 1

pw = input("비밀번호를 입력하세요.")

if pw == "abc123":
    print("비밀번호가 맞습니다.")

num = int(input("숫자를 입력하세요."))

if num % 2 == 0:
    print("짝수입니다.")

# 실습 2
pw = input("비밀번호를 입력하세요.")

if pw == "abc123":
    print("비밀번호가 맞습니다.")
else :
    print("비밀번호가 틀렸습니다.")

num = int(input("숫자를 입력하세요."))

if num % 2 == 0:
    print("짝수입니다.")
else :
    print("홀수입니다.")

# 실습 3
hye = int(input("점수를 입력하세요."))

if hye >= 90:
    print("학점 : A")
elif hye >= 80:
    print("학점 : B")
elif hye >= 70:
    print("학점 : C")
elif hye >= 60:
    print("학점 : D")
else :
    print("학점 : F")

# 중첩 조건문
# 불리언 (Boolean) : 참과 거짓을 나타내는 데이터 타입
# 참 : True
# 거짓 : False

# 예시. 로그인 여부와 권한에 따른 메세지가 다르게 출력력
is_logged = True
role = "admin"

if is_logged:
    print("로그인 상태입니다.")
    if role == "admin":
        print("관리자 권한을 갖습니다.")
    elif role == "editor":
        print("편집자 권환을 갖습니다.")
    else:
        print("일반 사용자입니다.")
else:
    print("로그인이 필요합니다.")

# 삼항 연산자
age = 33
status = "성인" if age >= 20 else "미성년자"
print(status)

number = 7
result = "짝수" if number % 2 == 0 else "홀수"
print(result)

a, b = 5, 8
max_value = a if a > b else b
print(max_value)

# 중첩 삼항 연산자
score = 81
grade = "A" if score >= 90 else (
    "B" if score >= 80 else "C"
)

# 조건문에서 in 연산자 활용용
users = ["Sean", "Linda", "Allie", "Martin"]

usersname = input("Name >>")

if usersname in users:
    print(f"환영합니다, {usersname}님!")
else:
    print("등록되지 않은 사용자입니다. 회원가입을 진행해주세요.")


# 실습 4
age = int(input("나이를 숫자로 입력해주세요. :"))
payment = input("결제방법을 입력해주세요. (현금 또는 카드) :")

if payment == "카드":
    if age < 8:
        pay = 0
    elif age < 14:
        pay = 450
    elif age < 20:
        pay = 720
    elif age < 75:
        pay = 1200
    else:
        pay = 0
else :
    if age < 8:
        pay = 0
    elif age < 14:
        pay = 450
    elif age < 20:
        pay = 1000
    elif age < 75:
        pay = 1300
    else:
        pay = 0
print(f"{age}세의 {payment}요금은 {pay}원입니다.")

# 실습 4 (다른 풀이)
pay_list = [[0, 450, 720, 1200, 0],
            [0, 450, 1000, 1300, 0]]

years = input("나이를 숫자로 입력해 주세여: ")
years = int(years)

how = input("결재방법을 입력해 주세여 (카드 또는 현금): ")

code = -1 
result = 0

code = 0 if how == "카드" else 1\
         if how == "현금" else -1
        
result = pay_list[code][0] if years < 8 else pay_list[code][1]\
                           if years < 14 else pay_list[code][2]\
                           if years < 20 else pay_list[code][3]\
                           if years < 75 else pay_list[code][4]

if code == 0:
    print(f"{years}세의 카드요금은 {result}입니다")
else:
    if code == 1:
        print(f"{years}세의 현금은 {result}입니다")
    else:
        print("결제방법을 잘못 입력하셨습니다")

# 실습 4 다른 방법
# 실습. 중첩 조건문
age = int(input("나이를 숫자로 입력하세요: "))

if age > 0:
    method = input("결제방법을 입력해주세요(카드 또는 현금): ")
    if method == "카드":
        if age < 8:
            price = "무료"
        elif age < 14:
            price = "450원"
        elif age < 20:
            price = "720원"
        elif age < 75:
            price = "1200원"
        else:
            price = "무료"
    elif method == "현금":
        if age < 8:
            price = "무료"
        elif age < 14:
            price = "450원"
        elif age < 20:
            price = "1000원"
        elif age < 75:
            price = "1300원"
        else:
            price = "무료"
    else:
        price = None
        print("결제방법을 카드나 현금으로 입력하세요")

    if price:
        print(f"{age}세의 {method}요금은 {price}입니다.")
else:
    print("나이는 음수가 될 수 없습니다.")

# 실습 5
fruit_dict = {"apple" : 95, "banana" : 105, "cherry" : 50} 
fruit = input("과일을 영문으로 입력하세요. :")

if fruit in fruit_dict:
    kcal = fruit_dict[fruit]
    print(f"{fruit}의 칼로리는 {kcal}Kcal입니다.")
else:
    print("포함되지 않은 과일입니다.")
>>>>>>> 9e5d526 (python 연습)
