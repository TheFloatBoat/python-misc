class caesar:

  def encrypt():
    text = input("Enter the text to encrypt: ")
    #input
    shift = int(input("Enter the shift value: ")) % 25

  #shift value
    result = ''
    #result string
    for i in text:
      char = i
      #YOU CAN GET CHARACTERS USING
      try:
        location = letters.index(char.lower())
        location += shift
        if location >= 26:
          location %= 26
        result += letters[location]
      except ValueError:
        result += char
    print("Encrypted text:", result)

  def decrypt(toDecrypt):
    for x in range(1, 27):
      result = ''
      #result string
      for i in toDecrypt:
        char = i
        #YOU CAN GET CHARACTERS USING
        try:
          location = letters.index(char.lower())
          location += x
          if location >= 26:
            location %= 26
          result += letters[location]
        except ValueError:
          result += char
      print("Encrypted text:", result)


letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

while True:
  torn = input("Chose what method to encrypt\n  a)Caesar Cypher\n  b)Brute force caesar cypher\n  Use:")
  if torn.lower() == "a":
    caesar.encrypt()
  elif torn.lower() == "b":
    caesar.decrypt(input("Brute force what?:"))
  else:
    print("dude READ the words")
