import math
import time
file_path = "primes.txt"
# Step 1: Read the contents of the file
file_path = "primes.txt"
with open(file_path, "r") as file:
    data = file.read()

# Step 2: Split the string by commas and filter out any empty strings
numbers_str = data.split(",")
numbers_str = [num for num in numbers_str if num]

# Step 3: Convert elements to integers and store them in a Python list
primes_list = [int(number) for number in numbers_str]
def progress_bar(x, pvt):
    progress = x - 1
    total = math.floor(math.sqrt(pvt)) - 1
    percentage = math.floor((progress / total) * 100)

    # Define the length of the progress bar
    bar_length = 40
    num_hashes = int(bar_length * progress / total)
    num_spaces = bar_length - num_hashes

    # Create the progress bar
    bar = "#" * num_hashes + " " * num_spaces

    # Print the progress bar and percentage
    print(f"We're currently testing {progress}/{total}. {percentage}% of the way there! [{bar}]", end='\r')

def getnum():
  pvt = input("what's the number you want? ")
  if pvt == "op":
    findPrimes()
  try:
    pvt = int(pvt)
  except ValueError:
    print("um make it a whole number please")
    getnum()
  return pvt
    

def factorise():
  sum = 1
  pvt = getnum()
  pvto = pvt
  #primef is where primes are stored
  primef = [1]
  #runs until highest factor possible
  x=2
  while True:
    progress_bar(x,pvt)
    #code to see if it is a factor
    while pvt % x == 0:
      primef.append(x)
      pvt = pvt/x
    #x gets bigger than the max possible number
    if x >= (math.floor(math.sqrt(pvt))) or x >= (math.floor(math.sqrt(pvto))):
      #double check
      for y in range(0, len(primef)):
        sum = sum * primef[y]
      if not(sum == pvto):
        primef.append(int(pvto/sum))
      print(f"The search is over! Prime factors are {primef}")
      break

while True:
  factorise()
