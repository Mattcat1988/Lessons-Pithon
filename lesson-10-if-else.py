x = 25
if x == 25:
    print("yes you right")
else:
    print("no you are wrong")
age = 19
if age <= 4:
    print("You are baby")
elif 4 < age < 12:
    print("you age kid")
elif 12 <= age < 19:
    print("you age teen")
else:
    print("you old")
all_cars = ['chrusler', 'dacia', 'bmw', 'Kia', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolett']
german_cars = ['bmw', 'vw', 'audi']
if 'lada' in all_cars:
    print("yes Lada is in the list")
else:
    print("not in the list ")
if 'bmw' in all_cars:      # Loop
    print("hello bmw")
else:
    print("bmw no list")
for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is German Car")
    else:
        print(xxxx + " is not german Car")
for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " Is German Car")
