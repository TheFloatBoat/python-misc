import math
import time
import sys

def numFromFile():
  with open('factors.txt', 'r') as file:
    content = file.read()
  content = content.replace('[', '').replace(']', '').replace(' ', '')
  elements = content.split(',')
  result_list = [int(element) for element in elements]
  return result_list

def getNumToFac():
  a=input("What number do we factorise?")
  if a == "OP":
    findPrimes()
  elif a == "quit":
    print("oof")
    sys.exit()
  elif a == 0:
    print("You cannot factorise 0")
  try:
    int(a)
  except:
    print("that's wrong, somehow.")
    a = getNumToFac()
  return int(a)

def factorise(num, updates):
  numToFac = num
  factors = [1]
  numsChecked = 0
  x = 0
  for x in primes:
    while x <= math.sqrt(numToFac) and numToFac % x == 0:
      factors.append(x)
      numToFac /= x
      if updates.lower() == "yes":
        print(f"Factors found so far:{factors}")
  if numToFac != 1:
    print("Precalculated primes have been exceded. Switching to unoptimised mode.")
    numsChecked = x-1
    factors = unopFactoriser(numsChecked, numToFac, factors)
  factors = doubleCheck(num, factors)
  return factors
 
def unopFactoriser(startCheck, target, factors):
  numToCheck = target
  for x in range(startCheck, int(math.floor(math.sqrt(target))+1)):
    while numToCheck % x == 0:
      factors.append(x)
      print(factors)
      numToCheck /= x
    if numToCheck == 1:
      break
  return factors


def doubleCheck(target, factors):
  multOfFactors = 1
  for x in range(0, len(factors)):
    multOfFactors *= factors[x]
  if multOfFactors < target:
    factors.append(int(target/multOfFactors))
  elif multOfFactors > target:
    factors.append(int(multOfFactors/target))
  return factors

def findPrimes():
  primesList = numFromFile()
  currentNum = primesList[len(primesList)-1]+1
  found = 0
  while True:
    isPrime = True
    for x in range(2, math.floor(math.sqrt(currentNum+1))+1):
      if currentNum % x == 0:
        isPrime = False
        break
    if isPrime:
      primesList.append(currentNum)
    currentNum += 1
    found +=1
    if found == 100000:
      with open('factors.txt', 'w') as file:
        file.write("[")
        for prime in primesList:
          file.write(", " + str(prime))
        file.write("]")
      quit = input("It has been 100000 numbers. Do you want to stop?")
      if quit.lower() == "yes":
        break
      else:
        print("I'm assuming no")
        found = 0
  
primes = numFromFile()
while True:
  toFactorise = getNumToFac()
  updates = input("Do you want updates on progress? type yes if you want and anything else if you dont:")
  factors = factorise(toFactorise, updates)
  print(f"The factors of your number are {factors}")
