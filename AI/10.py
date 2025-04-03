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