math=int(input("math:"))
eng=int(input("eng:"))
swa=int(input("swa:"))
total=math+eng+swa
if 0<total<=300:
  average=total/3
  print("total:",total)
  print("average:",average)
  if 70<=average<=100:
    grade= "A"
  elif 60<=average<=69:
    grade= "B"
  elif 50<=average<=59:
    grade= "C"
  elif 40<=average<=49:
    grade="D"
  elif 0<=average<=39:
    grade="fail"
  else:
    grade="invalid"
  print("grade:",grade)
else:
  print("invalid marks")