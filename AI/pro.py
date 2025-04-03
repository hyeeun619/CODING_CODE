import cv2
from pyModbusTCP.client import ModbusClient

# PLC와 연결 설정 (예시: IP와 포트 설정)
client = ModbusClient(host="192.168.1.100", port=502, auto_open=True)

# OpenCV로 이미지 읽기
image = cv2.imread('jennie.jpeg')

# 이미지 처리 (예: 그레이스케일 변환)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 예시: 이미지를 분석하여 특정 조건을 만족하는지 확인
# (예를 들어, 이미지의 평균 밝기가 일정 기준 이상이면 PLC에 신호를 보낸다고 가정)
average_brightness = gray_image.mean()

# 특정 밝기 조건을 만족하면 PLC에 신호를 보냄
if average_brightness > 100:  # 이 기준은 예시입니다
    print("조건을 만족하여 PLC에 신호를 보냅니다.")
    
    # PLC에서 Coil 상태 읽기
    coil_status = client.read_coils(0, 1)  # Coil 주소 0에서 1개 읽기
    print("현재 Coil 상태:", coil_status)

    # PLC에 데이터 쓰기 (예: Coil 상태 변경)
    client.write_coils(0, [True])  # Coil 주소 0에 True 값 쓰기
    print("Coil 상태를 True로 변경")

else:
    print("조건을 만족하지 않아 PLC에 신호를 보내지 않습니다.")

# 이미지 결과 보기
cv2.imshow('Processed Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
