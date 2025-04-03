# 바이너리 파일

# with open("owl.png","rb") as file:
    # # data = file.read()
    # # print(f"{len(data)} 바이트")
    # header = file.read(10) # 파일확장자를 찾는 방법법
    # print(f"{header}")

# def files(file_path):
#     with open(file_path, "rb") as file:
#         header = file.read(4) # 4바이트가 확장자의 매직넘버버
#         # print(header)
#         if header == b"\x89PNG": # png는 첫 4바이트가 89 50 4e 47
#             return "png"
#         elif header == b"\xff\xd8\xff\xe0": # jpg는 2바이트이기 때문에 뒤에 2바이트를 삭제
#             return "jpg"
#         else:
#             return "unknown"

# print(files("Cat03.jpg"))

# 바이너리파일 쓰기
# with open("owl.png", "rb") as file:
#     data = file.read()

# with open("owl_copy.png", "wb") as file:
#     file.write(data)