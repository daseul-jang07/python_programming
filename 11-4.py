inFp, outFp = None, None
inStr = ""

# 사용자로부터 파일명 입력받기
inFname = input("소스 파일명을 입력하세요: ")
outFname = input("타깃 파일명을 입력하세요: ")

# 파일 열기
inFp = open(inFname, "r", encoding="utf-8")
outFp = open(outFname, "w", encoding="utf-8")

# 내용 복사
inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

# 파일 닫기
inFp.close()
outFp.close()

# 완료 메시지
print("--- %s 파일이 %s 파일로 복사되었음 ---" % (inFname, outFname))
