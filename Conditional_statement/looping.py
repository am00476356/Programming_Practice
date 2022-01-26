# n = 1
# while n <= 10:
#     print(n)
#     n += 1

# n = -1
# while n >= -10:
#     print(n)
#     n -= 1

# n = -10
# while n <= -1:
#     print(n)
#     n += 1

# n= 1
# while n <= 50:
#     if n % 2 == 0:
#         print(n)
#     n += 1
#
# n = 2
# while n <= 50:
#     print(n)
#     n += 2
#
# m = 3
# while m <= 50:
#     print(m)
#     m += 2

# name = "Hello"
# i = len(name)
# a = 0
# while a < i:
#     print(name[a])
#     a += 1


"""Traversing through a list"""

# list_ = [1, 2, 3, 4]
# l = len(list_)
# i = 0
# while i < l:
#     print(list_[i])
#     i += 1

''' traversing through a tuple'''
#
# tup = (1, 2, 4, 5)
# length = len(tup)
# i = 0
# while i < length:
#     print(tup[i])
#     i += 1

''' traversing through a tuple'''

# tup = (1, 2, 4, 5)
# length = len(tup)
# i = 0
# while i < length:
#     print(tup[i])
#     i += 1


#######################################################################
''' FOR LOOP '''
# 1 to 10

# for num in range(1, 11):
#     print(num)
#

# 10 to 1
# for num in range(10, 0, -1):
#     print(num)
#

#-1 to -10
# for num in range(-1,-11,-1):
#     print(num)

# -10 to -1
# for num in range(-10, 0):
#     print(num)


# even numbers
# for num in range(1, 11):
#     if num % 2 == 0:
#         print(num)
#
#
# for num in range(2, 11, 2):
#     print(num)

# """traversing through the string"""
# name = "Python"
# for num in range(len(name)):
#     print(name[num])
#
# string_ = "what is your name?"
# for char in string_:
#     print(char)

'''Traversing through the list'''
# list_ = [1, 2, 3, 4, 5]
# for num in range(len(list_)):
#     print(list_[num])

''''traversing through tuple'''
# tup_ = (1, 5, 3, 4)
# for num in range(len(tup_)):
#     print(tup_[num])

# '''traversing through sets'''
# set_ = {1,'a', 'aaaaa'}
# for num in set_:
#     print(num)

'''traversing through dictionaries'''

# d = {"one": 1, "two": 2, 'three': 3}

# for key in d:
#     print(key, d[key], sep="-->")
#


# print index and element at the index
# name = "Shaktiman"
# for ele in range(len(name)):
#     print(ele, name[ele], sep="--> ")
#
# #enumerator version
#
# # for item in enumerate(name):
# #     print(item)
# #     print(item[0], item[1])
#
#
# for index, item in enumerate(name):
#     print(index, "---->", item)


#WAP to traverse through a string in reversed order.

# name = "Shaktiman"
# for item in range(len(name)-1, -1, -1):
#     print(name[item], end= " ")
#
# print()
# for char in name[::-1]:
#     print(char, end= " ")
# print()
#
# for item in reversed(name):
#     print(item)



'''WAP to count the number of characters present in the given string without using len function.'''

name = "shaktiman12345"
# count = 0
# for _ in name:  # throw away variable because the variable is not used in further actions
#     count += 1
#
# print(count)

# for item in range(0,len(name),2):
#     print(name[item])
#
# for element in name[::2]:
#     print(element)

for item in name:
    if item.isdigit():
        print(item, end=" ")


count = 0
for item in name:
    if "0" <= item <= "9":
        print(item, end=" ")
        count += 1

print()
print(count)




