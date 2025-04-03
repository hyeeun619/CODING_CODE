import cv2

image = cv2.imread("Cat03.jpg")
gray_image = cv2.imread("Cat03.jpg",cv2.IMREAD_GRAYSCALE) #cv2.IMREAD_COLOR : 기본값(생략가능)

cv2.imshow("Color Image", image)
cv2.imshow("Gray Image", gray_image)

# cv2.waitKey(0) # 0 = 창을 무한대기, 5000 = 5초 대기
key = cv2.waitKey(0)
if key == ord("q"): # ord() : 문자의 아스키코드값 획득 
    print(chr(key)) # chr() : 아스키코드값을 문자로 변경
