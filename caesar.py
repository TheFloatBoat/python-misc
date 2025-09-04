while True:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  DECRYPTED_TEXT = input("Decrypted Message:")
  ENCRYPTED_TEXT = ""
  for char in DECRYPTED_TEXT:
      if char not in alphabet:
          ENCRYPTED_TEXT += char
      else:
          INDEX = 0
          if (alphabet.index(char)+13) >= 26:
              INDEX = (alphabet.index(char)+13)%26
          else:
              INDEX = alphabet.index(char)+13
          ENCRYPTED_TEXT += alphabet[INDEX]
  print(ENCRYPTED_TEXT)
