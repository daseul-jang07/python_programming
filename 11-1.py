inFp = None
inStr = ""

# 파일 열기 (인코딩 문제 없도록 utf-8 사용)
inFp = open("C:/Users/ds271/OneDrive/바탕 화면/파이썬 프로그래밍/self_study/텍스트 파일 입출력.txt", "r", encoding="utf-8")

lineNum = 1  # 줄 번호 초기화

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (lineNum, inStr), end="")  # 줄 번호와 내용 출력
    lineNum += 1

inFp.close()
