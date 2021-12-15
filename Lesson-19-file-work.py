inputfile = '/home/vladimir/Myproject/Piton/user_names.txt'
myfile = open(inputfile, mode='r', encoding='ascii')
# print(myfile.read())

for num, line in enumerate(myfile, 1):
    if "Davidson" in line:
        print("Line N:" + str(num) + " : " + line.strip())

