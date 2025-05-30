inFp = None
inList, inStr = [], ""

inFp = open("C:/Users/ds271/OneDrive/바탕 화면/파이썬 프로그래밍/self_study/텍스트 파일 입출력.txt", "r", encoding="utf-8")

LineNumber = 1

inList = inFp.readlines()
for inStr in inList:
  print("%d: %s" % (LineNumber, inStr), end = "")
  LineNumber += 1

inFp.close()