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
print( ) 

i=1
while i<6:
  print(i)
  i+=1
else:
    print("i is no longer less than 6")
print( ) 
  
fruits=["apple","banana","cherry"]
for b in fruits:
  print(b)
print( )
for x in "banana":
  print (x)
print( )
fruits = ["apple","banana","cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print( )
fruits = ["apple","banana","cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print( )


for x in range (2,6):
  print(x)
print( )

for x in range (6):
  print(x)
print( )

adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
  for y in fruits:
    print(x,y)
print( )
for x in [0,1,2]:
  print(x)
  pass
print( )
for x in [0,1,2]:
  pass
print(x)
print( )  

genre=['pop','rock','jaz']
for i in range(len(genre)):
  print("i like", genre[i])
