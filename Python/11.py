<<<<<<< HEAD
import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

canvas = None
last_x, last_y = None, None

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

# 손가락 끝을 연결하여 그림을 그리는 함수
def draw_on_canvas(image, landmarks, hand):
    global canvas, last_x, last_y
    if canvas is None:
        canvas = np.zeros_like(image)

    # 검지 손가락 끝 좌표
    finger_tip = mp_hands.HandLandmark.INDEX_FINGER_TIP
    x, y = int(landmarks.landmark[finger_tip].x * image.shape[1]), int(landmarks.landmark[finger_tip].y * image.shape[0])

    # 주먹을 쥐었는지 판단
    if hand == 'fist':
        canvas = np.zeros_like(image)

    if hand == 'open' and last_x is not None and last_y is not None:
        # 손가락 끝을 기준으로 선을 그림
        cv2.line(canvas, (last_x, last_y), (x, y), (0, 255, 0), 5)  # 녹색 선

    # 현재 좌표를 마지막 좌표로 저장
    last_x, last_y = x, y

    image_with_canvas = cv2.addWeighted(image, 1, canvas, 0.5, 0)

    cv2.imshow("Canvas Drawing", image_with_canvas)

# 손 상태 확인 함수 (주먹 쥐었는지, 손을 편 상태인지 확인)
def get_hand_state(landmarks):
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    if (abs(thumb_tip.x - index_tip.x) < 0.05 and abs(thumb_tip.y - index_tip.y) < 0.05 and
        abs(middle_tip.x - ring_tip.x) < 0.05 and abs(ring_tip.x - pinky_tip.x) < 0.05):
        return 'fist'
    else:
        return 'open'

# 손 추적 및 그림 그리기
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("이미지 캡처 실패")
        break

    # BGR 이미지를 RGB로 변환
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 손 추적
    results = hands.process(image_rgb)

    # 손이 감지되면 랜드마크 그리기
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)
            hand_state = get_hand_state(landmarks)
            draw_on_canvas(image, landmarks, hand_state)

    # 이미지 표시
    cv2.imshow("Hand Finger Tracking", image)

    # 'q' 키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
=======
# while 문
i = 0
while i > 0:
    print("반복문 연습", i)
    i -= 1
print("종료")

# 합계 구하기
num = 1 # 더하는 숫자
total = 0 # 총합
while num <= 10:
    total += num # total = total + num
    print("현재 total 값 >", total)
    num += 1 # num = num + 1

print(f"1부터 10까지의 합은 {total}입니다.")

# 입력값 받기
user_input = ""
while user_input != "종료":
    user_input = input("원하는 값을 입력하세요. '종료' 입력시 종료됩니다.")
    print(f"입력한 값: {user_input}")

print("프로그램이 종료되었습니다.")

# break 문
# 예시. 숫자를 입력받아서 0이 입력되면 반복문 종료
while True:
    num = int(input("숫자입력 (0 입력시 종료):"))
    
    if num == 0:
        print("프로그램 종료")
        break

    print(f"입력한 숫자는 {num}입니다.")

# continue 문
# 예시. 숫자 입력받고 짝수만 출력하고 홀수는 건너뛰기
while True:
    num = int(input("숫자 입력 (음수 입력시 종료):"))
    
    if num < 0:
        print("프로그램 종료")
        break # 음수 입력시 프로그램 종료료

    if num % 2 != 0:
        continue # 홀수는 건너뛰고, 다시 입력 받기

    print(f"입력한 짝수는 {num}입니다.")


# 실습 1
while True:
    hye = input("양수를 입력하세요. ('종료' 입력시 프로그램 종료):")

    # hye 변수 값이 "종료" 문자열과 값이 같다면
    if hye == "종료":
        print("프로그램을 종료합니다.")
        # 프로그램 종료 (반복문을 빠져나와야 함)
        break

    # hye 변수 값이 "0" 이라면
    if hye == "0":
        # 이번 반복 회차는 건너뛰고, 다음 반복회차로 계속 나아감
        continue

    num = 1
    total = 0
    # num(1)부터 hye(사용자가 입력한 값)까지의 total(총합)
    while num <= int(hye):
        total += num
        num += 1
    print(f"1부터 {hye}까지의 합은 {total}입니다.")

    if hye < "0":
        print("양수만 입력 하세요.")


# 실습1 다른방법
while True:
    positive_input = input("양수를 입력하세여 ('종료' 입력시 프로그램 종료): ")
    
    if positive_input == "종료":
        print("프로그램을 종료 합니다")
        break
    
    try: 
        positive_input = int(positive_input)
        
        if positive_input < 0:
            print("양수만 입력하세여")
            continue
        elif positive_input == 0:
            continue
        else:
            result = 0
            i = 1
            
            while i <= positive_input:
                result = result + i
                i = i + 1
                
            print(f"1부터 {positive_input}의 합은 {result}입니다")

    
    except:
        print("양수만 입력하세여")
        continue


# 실습 1 다른 방법
while True:
    user_input = input("양수를 입력하세요.('종료'입력시 프로그램 종료): ")

    if user_input == "종료":
        print("프로그램을 종료합니다")
        break

    if not user_input.isdigit():  # True -> not False
        print("양수를 입력하세요")
        continue

    number = int(user_input)
    if number == 0:
        continue

    total = 0
    num = 1
    while num <= number:
        total += num
        num += 1
    print(f"1부터 {number}까지의 합은 {total}입니다.")
>>>>>>> 9e5d526 (python 연습)
