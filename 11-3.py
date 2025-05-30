outFp = None
outStr = ""

fName = input("파일명을 입력하세요: ")
outFp = open(fName, "w", encoding="utf-8")  # 쓰기 모드로 열기

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")  # 줄바꿈은 \n
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 씀 ---")