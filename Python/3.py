<<<<<<< HEAD
import cv2
import matplotlib.pyplot as plt
import numpy as np

# # 웹캠 연결
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read() # ret : True or False
#     if not ret:
#         print("프레임을 읽지 못했습니다.")
#         break

#     cv2.imshow("video", frame)

#     # 1ms동안 키 입력을 기다렸다가 q가 입력되면 종료 
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release() # 비디오 해제
# cv2.destroyAllWindows()


########################################################################

# # 웹캠 저장
# cap = cv2.VideoCapture(0)

# # 코댁 설정
# fourcc = cv2.VideoWriter_fourcc(*'XVID') # .avi파일 생성 / .mp4 : mp4v
# fps = 20.0 # 초당 프레임 수

# # 비디오 저장 객체 생성
# out = cv2.VideoWriter("output.avi", fourcc, fps, (640, 480))

# while cap.isOpened():
#     ret, frame = cap.read() # 프레임 읽기
#     if not ret:
#         break

#     out.write(frame)
#     cv2.imshow("wideo", frame)

#     # 1ms동안 키 입력을 기다렸다가 q가 입력되면 종료
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()

# 실습 손 윤곽선을 감지하고 필터를 추가

# cap = cv2.VideoCapture(0)

# # 코댁 설정
# fourcc = cv2.VideoWriter_fourcc(*'XVID') # .avi파일 생성 / .mp4 : mp4v
# fps = 20.0 # 초당 프레임 수

# # 비디오 저장 객체 생성
# out = cv2.VideoWriter("out.avi", fourcc, fps, (640, 480))
# out2 = cv2.VideoWriter("out2.avi", fourcc, fps, (640, 480))
# out3 = cv2.VideoWriter("out3.avi", fourcc, fps, (640, 480))

# while cap.isOpened():
#     ret, frame = cap.read() # 프레임 읽기
#     if not ret:
#         break

#     out.write(frame)

#     # 그레이스케일 변환
#     output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # 임계값 처리
#     _, binary = cv2.threshold(output, 127, 255, cv2.THRESH_BINARY)

#     # 컨투어 감지
#     contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # 컨투어 그리기
#     frame_img = frame.copy()
#     cv2.drawContours(frame_img, contours, -1, (0, 255, 0), 2)

#     out2.write(frame_img)

#     # 샤프닝필더
#     kernel = np.array([[0, -1, 0], [-1, 7, -1], [0, -1, 0]])

#     # 필터적용
#     sharped = cv2.filter2D(frame, -1, kernel)

#     out3.write(sharped)

#     cv2.imshow("wideo", frame)
#     cv2.imshow("Contours", frame_img)
#     cv2.imshow("sharped", sharped)

#     # 1ms동안 키 입력을 기다렸다가 q가 입력되면 종료
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break


# cap.release()
# out.release()
# out2.release()
# out3.release()
# cv2.destroyAllWindows()


# 실습 다른버전 
plt.ion()  # matplotlib 인터렉티브 모드 활성화(실시간 업데이트)

# 종료 플래그
quit_cap = False


# matplotlib 이벤트 핸들러
def on_key(e):
    global quit_cap
    if e.key == "q":
        quit_cap = True


plt.figure(figsize=(12, 4))
# 키이벤트 연결
plt.gcf().canvas.mpl_connect("key_press_event", on_key)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열수없습니다.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # matplotlib 3개의 영상 실시간 업데이트
    plt.clf()  # 기존의 그래프 초기화

    # 원본
    original = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 예시로 이미지를 제출할때
    cv2.imwrite("orginal.jpg", cv2.cvtColor(original, cv2.COLOR_RGB2BGR))

    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title("original")
    plt.axis("off")

    # 손 윤곽선 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # 이진화처리
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )  # 컨투어탐지
    contour_img = frame.copy()  # 원본을 복사해서 사용
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)  # 컨투어 그리기
    contour_img = cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 3, 2)
    plt.imshow(contour_img)
    plt.title("contour")
    plt.axis("off")

    # 샤프닝 필터 적용
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(contour_img, -1, kernel)

    plt.subplot(1, 3, 3)
    plt.imshow(sharpened)
    plt.title("sharp")
    plt.axis("off")

    # 업데이트 간격을 조절
    plt.pause(0.01)
    plt.show()

    # # 종료
    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break
    if quit_cap:
        print("종료합니다")
        break

cap.release()
cv2.destroyAllWindows()
plt.close("all")  # 모든 matplotlib 닫기
=======
# song = input("너의 최애 노래는?")
# print(song) # 러브 다이브
# print(type(song)) # <class 'str' => "문자열"

# a = input("1 + 1 = ?")
# print(a) # 2
# # "2" 문자열의 타입을 "숫자형(정수형)" 으로 변환 필요
# # => "형 변환환"
# print(a*2) # 22 <= "2" * 2

# 형변환 (type casting, type conversion)
# 1. 정수형으로 변환
print(int("10"), type(int("10"))) # 문자열 "10"을 정수로 변환
print(int(10.9), type(int(10.9))) # 실수 10.9를 정수로 변환 ( 소수점 이하 버림)

# 2. 실수형으로 변환
print(float("11.2"), type(float("11.2"))) # 문자열 "11.2"를 실수로 변환
print(float(10), type(float(10))) # 정수 10을 실수로 변환환

# 3. 형변환 안되는 예시
# print(int("name")) # 숫자 기호가 아닌 문자열을 정수로 변환하려 할 때
# print(int("11.2")) # 실수 문자열을 정수로 변환하려 할 때

b = 2 # 정수형
print(b * 10) # 20
print(str(b) * 10) # 2222222222
print(str(b) + "입니다") # 2입니다
# print(b + "입니다") # type error


# str() 활용 예시
math_score = 80
eng_score = 85
total_scroe = math_score + eng_score
avg_score = total_scroe / 2

print("합계: " + str(total_scroe))
print("평균: " +str(avg_score))
# print("합계: " + total_scroe)
# print("평균: " + avg_score)

# 1번
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")
print("안녕하세요!"+ name + "님 (" + age + "세)")

# 2번
name = input("이름을 입력하세요.")
birth = input("태어난 년도를 입력하세요.")
this = input("올해 년도를 입력하세요.") 
age = int(this) - int(birth) + 1
print("올해는" + this + "년", name + "님의 나이는" + str(age) + "세 입니다.")
>>>>>>> 9e5d526 (python 연습)
