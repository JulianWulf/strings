# for Schleife break
Family = ["Julian","Andreas","Valentin","Anton","Mama","Papa"]


for element in Family:
    if element == "Valentin":
        break
    print(element)


# While Schleife break
v = 9

while v < 20:
    print(v)
    v = v + 1
    if v == 20:
        break



# for Schleife Continue

Family = ["Julian","Andreas","Valentin","Anton","Mama","Papa"]
for element in Family:
    if element == "Valentin":
        continue
    print(element)

# While Schleife Continue

v = 9

while v < 20:
    v = v + 1
    if v == 10:
        continue
    print(v)
