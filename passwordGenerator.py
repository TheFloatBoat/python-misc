import random
letters = ("a", "b", "c", "d", "e", "", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
nonLetterSymbols=("`", "¬", "!", "“", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "[", "}", "]", "~", "#", ";", ":", "‘", "@", "<", ",", ">", ".", "?", "/")
z = int(input("Passsword Length: "))
p = ""
for x in range(0, z):
    if random.randint(0,1) == 1:
        if random.randint(0,1) == 1:
            p = p + letters[random.randint(0, len(letters))]
        else:
            p = p + letters[random.randint(0, len(letters))].upper()
    else:
        if random.randint(0,1) == 1:
            p = p + nonLetterSymbols[random.randint(0, len(nonLetterSymbols))]
        else:
            p = p + str(random.randint(0,10))
print(p)
