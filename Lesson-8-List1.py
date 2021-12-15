

cities = ['New york', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']
print(cities)
print(len(cities))
print(cities[0])
print(cities[-1])
print(cities[2].upper())

cities[2] = 'Tula'
print(cities)

cities.append('kursk')
cities.append('Yalta')
print(cities)
cities.insert(2, 'Feodosia')
print(cities)

del cities[-1]
print(cities)
cities.remove("Tula")
print(cities)
print(cities[3])
deleted_city = cities.pop()
print("Detelted city is: " + deleted_city)
print(cities)

cities.reverse()
print(cities)

