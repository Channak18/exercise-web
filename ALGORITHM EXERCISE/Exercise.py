# output = ""
# for i in range(4):
#     name = input()
#     nbOfCha = 0
#     for cha in name:
#         nbOfCha+=1
#     output += str(nbOfCha) + "-"
# print(output[:-1])

# Ex2
# word = input()
# for cha in word:
#     print("Y",end="")

# result = ""
# for i in range(4):
#     text = input("Enter your text")
#     chars = len(text)
#     if i == 3:
#         result += str(chars)
#     else:
#         result += str(chars) + "-"
# print(result)

# text = input()
# result = ""
# for char in text:
#     result += str(char) + ""
#     print("Y")

# text = input("Enter your text")
# if len(text) <= 3:
#     print("It's small")
# elif len(text) >= 4 and len(text) <= 6 or len(text) >=8 and len(text) <= 10:
#     print("It's medium!")
# elif len(text) == 7:
#     print("It's Average")
# elif len(text) >= 7:
#     print("It's large")

# text = input()
# counter = 0
# for i in range(len(text)):
#     if text[i] != 1:
#         counter += 1
# print(counter)
# result = ""
# for i in range(3):
#     text = input()
#     counterA = 0
#     for j in range(len(text)):
#         if text[j] == "A" or text[j] == "a":
#             counterA += 1
#         if i == 2:
#             result += str(counterA)
#         else:
#             result += str(counterA) + "|"
#     print(result)


# text = input("input text")
# countB = 0
# for i in range(len(text)):
#     if text[i] == "b" or text[i] =="B":
#         countB += 1
# print("B"+ str(countB))




# text = "Hello world wod world"
# isFound = False
# index = 0
# result = ""
# while index<len(text):
#     if text[index] == "w":
#         isFound = True
#     else:
#         if text[index] == "d":
#             isFound = False
#             result+=text[index]
#             if result == "world":
#                 print("yes")
#                 print(result)
#             # result = ""
            
#     if isFound:
#         result+=text[index]
#     index += 1
#     # print(result)

# text = "Hello world world world"
# isFound = False
# result = ""
# for index in range(len(text)):
#     if text[index] == "w":
#         isFound = True
#     else:
#         if text[index] == "d":
#             isFound = False
#             result += text[index]
#             if result == "world":
#                 print(result)
#     if isFound:
#         result += text[index]


# text = "world worl worl word world wd"
# isFound = False
# isFoundWorld = False
# firstIndexOfW = None
# index = 0
# result = ""
# while not isFoundWorld:
#     if text[index] == "w":
#         isFound = True
#         firstIndexOfW = index
#     else:
#         if text[index] == "d" or text[index] == " ":
#             isFound = False
#             result+=text[index]
#             if result == "world":
#                 print(result)
#                 print("this is the first index of world :",firstIndexOfW)
#                 isFoundWorld = True
#             result = ""
#     if isFound:
#         result+=text[index]
#     index += 1

