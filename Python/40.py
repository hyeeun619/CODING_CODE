# 실습 타자연습 게임

import random
import time

words = [
    "mountain",
    "river",
    "forest",
    "ocean",
    "desert",
    "tree",
    "flower",
    "cloud",
    "rain",
    "sunlight",
]


def game():
    print("영어 타자 연습 게임")
    print("게임종료를 원하시면 exit를 입력하세요")

    total_words = 0  # 게임한 단어 갯수
    start_time = time.time()  # 게임시작 시간

    while True:
        word = random.choice(words)
        print(f"단어 : {word}")

        while True:
            user_input = input("입력 : ")

            if user_input == "exit":  # 게임 종료
                end_time = time.time()
                total_time = end_time - start_time
                print("\n게임종료")
                print(f"총입력한 단어는 {total_words}개 입니다.")
                print(f"총걸린시간은 {total_time:.2f}초")
                print(f"단어당 평균시간은 {total_time / total_words:.2f}초")
                return

            if user_input == word:
                print("통과!")
                total_words += 1
                break
            else:
                print("오타! 다시입력하세요")


game()