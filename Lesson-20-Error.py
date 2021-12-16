
filename = "Lesson_list.txt"
while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding="Latin-1")
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        filename = input("Enter Correct file name! :")
    else:
        print("Inside ELSE")
        print(myfile.read())
    finally:
        print("Inside Finally")
        print("=============end of=============")
