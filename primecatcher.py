import math
def getnum():
  global pvt
  pvt = input("what's the number you want? ")
  try:
    pvt = int(pvt)
  except ValueError:
    print("um make it a number pweese")
    getnum()


print("Welcome! Just several sidenotes:")
print("a) Any numbers returned as floats are of dubious accuracy. Check before usage.")
print("b) All numbers that do not have prime factors returned are prime.")#this is because somehow somewhere in this mess is a bug ughhhhhh
while True:
  sum = 1
  getnum()
  pvto = pvt
  primef = []
  for x in range(2, math.floor(math.sqrt(pvt))):
    if x > math.floor(math.sqrt(pvt)):
      for y in range(0, len(primef)):
        sum = sum * primef[y]
      if not(sum == pvto):
         primef.append(pvto/sum)
      print(f"The search is over! Prime factors are {primef}")
      break

    print(f"We're currently testing {x-1}/{math.floor(math.sqrt(pvt))-1}. {math.floor(((x-1)/(math.sqrt(pvt)-1))*100)}% of the way there!")
    while pvt % x == 0:
      primef.append(x)
      pvt = pvt/x
