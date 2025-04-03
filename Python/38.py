import sys, os

# 명령행 인수 전체 리스트 출력
print(sys.argv)
print(sys.argv[0])
# print(sys.argv[1])

# Python 버전 출력
print(sys.version)

# 프로그램 종료
print("프로그램을 종료합니다.")
# sys.exit(0)
# print("이 문장은 실행되지 않죠!")

print()

# 현재 디렉토리 출력
print("현재 작업 디렉토리", os.getcwd())
file_path = os.chdir(os.getcwd()) # 해당 경로로 이동
dir = os.popen("dir") # 'ls' 명령 조회 / dir
# print(dir.read()) #'ls' 명령어의 출력 결과 가져오기

# 디렉토리 생성
# os.mkdir("temp") # make directory
# print("폴더가 생성되었습니다!")

# 디렉토리 삭제
# os.rmdir("temp") # remove directory
# print("폴더가 삭제되었습니다!")

# 환경변수 출력
# 환경변수: PATH 라는 곳에 경로를 미리 세팅해서 필요에 따라 언제든지 가져다 쓰고자 하는 것
print("PATH 환경변수:", os.environ.get("PATH"))