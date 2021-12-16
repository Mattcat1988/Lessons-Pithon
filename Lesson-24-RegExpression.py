import re
input_filename = "/home/vladimir/Myproject/Piton/site.txt"
result_filename = "/home/vladimir/Myproject/Piton/results.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resulfile = open(result_filename, mode='w', encoding='Latin-1')
mytext = inputfile.read()
lookfor = r"[\w.-]+@(?!mail\.com)[A-Za-z-]+\.[\w.]+"


results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resulfile.write(item + "\n")

print("Total: " + str(len(results)))
# https://regex101.com/