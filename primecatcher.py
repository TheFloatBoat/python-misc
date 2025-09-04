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

def getNum():
  a=input("What number do we factorise?")
  if a == "OP":
    findPrimes()
  if a == "quit":
    print("oof")
    sys.exit()
  try:
    int(a)
  except:
    print("that's wrong, somehow.")
    a = getNum()
  if int(a) == 0:
    print("You can't use 0")
    a=int(getNum())
  return int(a)
  
def factorise(num, updates):
  numForCalc = num
  factors = [1]
  switch = False
  atSwitch = 0
  for x in range(0,len(primes)+1):
    try:
      primes[x]
    except IndexError:
      print("Precalculated primes have been exceded. Switching to unoptimised mode.")
      print(f"BTW this is what we have left to factorise:{numForCalc}")
      switch = True
      atSwitch = x-1
      break
    if primes[x] > math.sqrt(numForCalc) or numForCalc == 1:
      break
    while numForCalc % primes[x] == 0:
      factors.append(primes[x])
      numForCalc /= primes[x]
      if updates.lower() == "yes":
        print(f"Factors found so far:{factors}")
  if switch == True:
    factors = unopFactoriser(atSwitch, numForCalc, factors)
  factors = doubleCheck(num, factors)
  return factors

def unopFactoriser(startCheck, target, factors):
  numToCheck = target
  for x in range(primes[startCheck], int(math.floor(math.sqrt(target))+1)):
    if numToCheck % x == 0:
      factors.append(x)
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
          file.write(str(prime) + ", ")
        file.write("]")
      quit = input("It has been 100000 numbers. Do you want to stop?")
      if quit.lower() == "yes":
        break
      else:
        print("I'm assuming no")
        found = 0
primes = numFromFile()


while True:
  toFactorise = getNum()
  updates = input("Do you want updates on progress? type yes if you want and anything else if you dont:")
  factors = factorise(toFactorise, updates)
  print(f"The factors of your number are {factors}")
