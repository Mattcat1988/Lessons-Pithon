#        0       1    2       3         4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
for x in cars:
    print(x.upper())

for x in range(1, 6):
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)
for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is: " + str(max(mynumber_list)))  # показать максимальный номер в list
print("Min number is: " + str(min(mynumber_list)))
print("Summa number is: " + str(sum(mynumber_list)))  # сумма
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
#     начать:сколько добавить
mycars = cars[1:4]  # вырезать
print(mycars)
mycars = cars[:]
print(mycars)
mycars = cars[-3:-1]
print(mycars)

cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
mycars = cars[:]  # копия массива
