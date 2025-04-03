<<<<<<< HEAD
import cv2
import mediapipe as mp

# MediaPipe 손 추적 모델 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# 웹캠 영상 캡처
cap = cv2.VideoCapture(0)

# 웹캠이 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

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
            # 각 랜드마크 좌표를 따라 선 그리기
            for i in range(1, len(mp_hands.HandLandmark)):
                # 각 랜드마크 연결
                x1, y1 = int(landmarks.landmark[i-1].x * image.shape[1]), int(landmarks.landmark[i-1].y * image.shape[0])
                x2, y2 = int(landmarks.landmark[i].x * image.shape[1]), int(landmarks.landmark[i].y * image.shape[0])
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # 랜드마크 점 그리기
            for landmark in landmarks.landmark:
                x, y = int(landmark.x * image.shape[1]), int(landmark.y * image.shape[0])
                cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

    # 이미지 표시
    cv2.imshow("Hand Tracking", image)

    # 'q' 키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
=======
# 내장함수
number = [10, 20, 30, 40]
print(sum(number))

scores = {"국어" : 83, "영어" : 90, "수학" : 95}
print(scores.values())
total_score = sum(scores.values())
print(total_score)

print(max(number))
print(min(number))

print(max(scores.values()))
print(min(scores.values()))

names = ["Alice", "Bob", "Charlie","Lily"]
scores = [85, 90, 95, 100, 105]
zipped = list(zip(names, scores))
zipped2 = dict(zip(names, scores))
print(zipped)
print(zipped2)
>>>>>>> 9e5d526 (python 연습)
