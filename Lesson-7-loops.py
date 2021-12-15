#            start  end  step
for x in range(-10,100, 2 ):
    print("Number x = " + str(x))
    if x == 42:
        break

print("--------------------off-----------------")

x = 0
while True:
    print(x)
    x = x + 1
    if x == 100:
        break
