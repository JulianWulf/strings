# for Schleife break
Family = ["Kotlin","PHP","HTML","CSS","Java","Python"]


for element in Family:
    if element == "PHP":
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

Family = ["Kotlin","PHP","HTML","CSS","Java","Python"]
for element in Family:
    if element == "PHP":
        continue
    print(element)

# While Schleife Continue

v = 9

while v < 20:
    v = v + 1
    if v == 10:
        continue
    print(v)
