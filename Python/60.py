# 로또 실습 풀이
from tkinter import *
from bs4 import BeautifulSoup
import requests


def lotto():
    # 입력필드에 넣은 "로또 번호 회차" 값 가져오기
    lotto_num = entry.get()
    print(lotto_num)

    url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={lotto_num}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    print(soup)


root = Tk()  # tkinter 루트 윈도우 생성
root.title("로또 당첨 번호 조회하기")
root.geometry("400x300")

# GUI 컴포넌트 배치
Label(root, text="당첨 회차 입력").pack(pady=10)  # 레이블
entry = Entry(root, width=20)  # 입력필드
entry.pack(pady=10)
Button(root, text="당첨 번호 조회", command=lotto).pack(
    pady=10
)  # 버튼 (클릭시 lotto 함수 실행)

text = Text(root, width=60, height=30)
text.pack(pady=10)

root.mainloop()  # GUI 이벤트 루프 시작 (프로그램 실행)