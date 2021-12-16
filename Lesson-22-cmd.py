import sys   # system move
import os    # commands terminal
x = len(sys.argv)
if x > 1:
    if sys.argv[1] == "/?":
        print("Help Requested")
        print("Usage of whis program is python.exe myfile.py argv1 argv2")
    print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("Arguments NOT PROVIDED")

os.system("ls > test2.txt")
os.mkdir("mydir")
sys.exit(0)
