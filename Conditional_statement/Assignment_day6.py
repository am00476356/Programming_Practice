# WAP to check if the marks given falls under the following categories and print the result based on marks

# marks_obtained = int(input("Enter the marks: "))
#
# if marks_obtained >= 75:
#     print("Congratulations you have passed with Distinction")
# elif marks_obtained >= 60:
#     print("Congratulations you have passed with First Class")
# elif marks_obtained >= 35:
#     print("Congratulations you have passed with Second Class")
# else:
#     print("Better luck next time, You Failed")


#  WAP to count the number of special characters in a string

# input_string = input("Enter the string :")
# count = 0
# #print(ord('~'))
# capital_letters = list(range(65,65+26))
# small_letters = list(range(97,97+26))
# check_string = capital_letters + small_letters
# #print(check_string)
#
# # for item in input_string:
# #     if 64 < ord(item) < 65+33 or 96 < ord(item) < 97+33:
# #         count += 0
# #     else:
# #         count += 1
#
# for item in input_string:
#     if ord(item) not in check_string:
#         count += 1
#
#
# print(f"The number of special characters in the string {input_string} are {count}")

# WAP to count the number of capital letters and small letters in a string.
input_string = input("Enter the string :")
count_small = 0
count_capital = 0
#print(ord('~'))
capital_letters = list(range(65,65+26))
small_letters = list(range(97,97+26))
check_string = capital_letters + small_letters
#print(check_string)

# for item in input_string:
#     if 64 < ord(item) < 65+33 or 96 < ord(item) < 97+33:
#         count += 0
#     else:
#         count += 1

for item in input_string:
    if ord(item) in capital_letters:
        count_capital += 1
    elif ord(item) in small_letters:
        count_small += 1


print(f"The number of small cases in the string {input_string} are {count_small}")
print(f"The number of capital cases in the string {input_string} are {count_capital}")



