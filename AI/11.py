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
