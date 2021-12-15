inputfile = '/home/vladimir/Myproject/Piton/user_passwords.txt'
outputfile = '/home/vladimir/Myproject/Piton/my_passwords.txt'

password_tolookfor = "123"
myfile = open(inputfile, mode='r', encoding='ascii')
# print(myfile.read())                                      # a-append add
myfile2 = open(outputfile, mode='a', encoding='ascii')      # w-perazapis

for num, line in enumerate(myfile, 1):
    if password_tolookfor in line:
        print("Line N:" + str(num) + " : " + line.strip())
        myfile2.write("Found password" + line)
myfile.close()
myfile2.close()
