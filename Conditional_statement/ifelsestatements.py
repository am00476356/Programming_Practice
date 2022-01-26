## Number is odd or even

# number = 2
# if number%2 == 0 :
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")



## character is present in the string or not

# name = "This is a special string"
# char = "is"
#
# if char in name :
#     print("it is present")
# else :
#     print("it is not present")



## WAP to check if the character is lowercase or not

# char = input("input a character : ")
#
# if "a"<= char <= "z":
#     print(f"{char} is lowercase")
#
# else:
#     if "A" <= char <= "Z":
#         print(f"{char} is uppercase")
#     else :
#         print(f"{char} is not an alphabet")

########################################################
# """Another way ot use this"""
#
# char = input("input a character : ")
#
#
# if "a" <= char <= "z":
#     print(f"{char} is lowercase")
#
# elif "A" <= char <= "Z" :
#     print(f"{char} is uppercase")
#
# else :
#     print(f"{char} is not an alphabet")



####################################################

a = "fwd direction"
"""One way to do this"""
# if(len(a) > 0):
#     print("the Iterable is not empty")
# else:
#     print("iterable is empty")

#Way 2
# if bool(a):
#     print("The Iterable is not empty")
# else:
#     print("The iterable is empty")


# way 3

# if a:
#     print("the iterable is not empty")
# else:
#     print("the iterable is empty")


#################
# WAP to check if it is default value:

# if a:
#     print("Non default value")
# else:
#     print("Default value")

# WAP to convert the lowercase letter into lower and lowercase to uppercase.
"""My way"""
# s1 = input("Enter the word you want to change: ")
#
# print(s1.swapcase())
#
# if s1.isupper():
#     s2 = s1.lower()
# elif s1.islower():
#     s2 = s1.upper()
# else:
#     s2 = s1
#     print("what have you put!!! Just see below:")
#
# print(s2)

"""Taught as Way1"""
# char = 'n'
# if 'a'<= char <= 'z':
#     upper_char = char.upper()
#     print(upper_char)
# elif 'A' <= char <= 'Z':
#     lower_case = char.lower()
#     print(lower_case)
# else:
#     print("character is not an alphabet")
#
# """WAY 2"""
# char = 'n'
# if char.islower():
#     upper_char = char.upper()
#     print(upper_char)
# elif char.isupper():
#     lower_case = char.lower()
#     print(lower_case)
# else:
#     print("character is not an alphabet")
#
# '''WAY 3'''
#
# char = 'n'
#
# if 'a'<= char <= 'z':
#     print(chr(ord(char)-32))
# elif 'A'<= char <='Z':
#     print(chr(ord(char)+32))
# else:
#     print("character is not an alphabet")


# str = "Hello"
# str_check = "aeiou"
# str_check2 = "AEIOU"
# if str[0] in str_check or str[0] in str_check2:
#     print("Starts with vowel")
# else:
#     print("Doesn't start with vowel")
#
# # string.startswith('aeiouAEIOU') will check the whole string and not only single character.
#
# str = "ORANGE"
# str_check = "aeiou"
# str_check2 = "AEIOU"
# if str[-1] in str_check or str[-1] in str_check2:
#     print("Ends with vowel")
# else:
#     print("Doesn't end with vowel")


# string = "Mom"
# a = string.lower()
# if a == a[::-1]:
#     print(f"{string} is a palindrome")
# else:
#     print(f"{string} is not a palindrome")
#
#
# a = 121
# string_1 = str(a)
# if string_1 == string_1[::-1]:
#     print("palindrome")
# else:
#     print("Not a palindrome")
#

# iterable = [1, 3, 5]
#
# if len(iterable) % 2 == 0:
#     print("Yes")
# else:
#     print("No")

a = 1231234
print(a.as_integer_ratio())

temp_string = str(a)
if int(temp_string[0]) % 2 == 0:
    print("Starts with even")
else:
    print("Starts with odd")
""" one line statement"""
print("number is ")



