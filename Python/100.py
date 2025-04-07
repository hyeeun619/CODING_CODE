kor = int(input("국어 점수를 입력하세요 :"))
math = int(input("수학 점수를 입력하세요 :"))
eng = int(input("영어 점수를 입력하세요 :"))

total = kor + math + eng
avg = total / 3

print(f"총점 : {total}")
print(f"평균 : {avg:.2f}")

result = {True : "합격", False: "불합격"}[avg >= 60]
print(f"합격? : {result} ")