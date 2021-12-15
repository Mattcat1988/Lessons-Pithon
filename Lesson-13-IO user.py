# name = input("Please enter you name : ")
# print("Privet " + name)
# num1 = input("Enter X: ")
# num2 = input("Enter Y: ")
# summa = int(num1) + int(num2)
# print(summa)
# message = ""
# while True:
#    message = input("Enter Password ")
#   if message == 'secret':
#       break
#   print(message + " Password Not Correct")
# print("Password was:" + message)
mylist = []
msg = ""
while msg != 'stop'.upper():
    msg = input("enter new item, and stop to finish ")
    mylist.append(msg)
    print(mylist)