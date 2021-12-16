import sys
filename = "Lesson_list.txt"
while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding="Latin-1")
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        filename = input("Enter Correct file name! :")
        print(sys.exc_info()[1])
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()
    finally:
        print("Inside Finally")
        print("=============end of=============")
