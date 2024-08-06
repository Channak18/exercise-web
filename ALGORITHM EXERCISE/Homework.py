# Exercise 1
# text = input("inter text")
# index = 0
# while index < len(text):
#     print(text[index])
#     index += 1

# Exercise 2
# letter = input()
# new_string = ""
# index = 0
# while index < len(letter):
#     if letter[index] == "a":
#         new_string += "X"
#     elif letter[index] == "b":
#         new_string += "Y"
#     else:
#         new_string += letter[index]
#     index += 1
# print(letter, "=>", new_string)

# ex3

# myString = "We Are students"
# print (myString [0:1])
# print (myString [0:0])
# print (myString [:0])
# print (myString [-2:5])
# print (myString [-10: -5 ])
# print (myString [0:2:1])

# ex5

# text = input("Enter the text : ")
# charector_A = 0
# charector_B = 0
# index = 0
# while index < len(text):
#     if text[index] == "A":
#         charector_A += 1
#     else:
#         if text[index] == "B":
#             charector_B += 1
#     index += 1
# print(charector_A)
# print(charector_B)

# ex4

# mystring = " welcomeToPNC"
# print (mystring [10::]) 
# print (mystring [4:8:1]) 
# print (mystring [8:9:1]) 
# print (mystring [1:8:1]) 
# print (mystring [::-2])

# ex6
# text = input("Enter ur text:")
# lettera = 0
# letterb = 0
# letterc = 0
# for i in range(len(text)):
#     if text[i] == 'a' or text[i] == 'A':
#         lettera += 1
#     elif text[i] == 'b' or text[i] == 'B':
#         letterb += 1
#     elif text[i] == 'c' or text[i] == 'C':
#         letterc += 1
# print(lettera, "A or a")
# print(letterb, "B or b")
# print(letterc, "C or c")


# ex2
# letter = input("inter your text: ")
# new_string = ""
# index = 0
# while index < len(letter):
#     if letter[index].lower() == "a":
#         new_string += "X"
#     elif letter[index].lower() == "b":
#         new_string += "Y"
#     else:
#         new_string += letter[index]
#     index += 1
# print(letter, "=>", new_string)

# EX7
# text = input("Enter text:")
# reversed_text = text[::-1]
# print(reversed_text)

# text = "hey"
# lastIndex = len(text) - 1
# for i in range (len(text)):
#     print(text[lastIndex - i])

text = input("inter the text: ")
for i in range(text.upper()):
    print(text)