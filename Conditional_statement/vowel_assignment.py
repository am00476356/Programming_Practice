char = input("Enter the character :")
if char in "aieouAEIOU":
    new_dict = {char: ord(char)}
    #d[char] = ord(char)
    #d.update({char: ord(char)}
    #d.setdefault(char, ord(char)}
    print(new_dict)
else:
    print(f"Entered character {char} is not a vowel")

#print(ord(char))
