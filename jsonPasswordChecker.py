import json

loginData=open("passwords.txt", "r").readlines()
loginData = json.loads(loginData[0])
isDetailsCorrect=False
def loginChecker ():
  username=input("what is your name:")
  password=input("what is your password:")
  try:
    if password==loginData[username]:
      print(f"welcome {username}")
      return True
    else:
      print("You are either not a user or your password is wrong")
  except KeyError:
    print("You are either not a user or your password is wrong")
    return False

while not isDetailsCorrect:
  isDetailsCorrect = loginChecker()
