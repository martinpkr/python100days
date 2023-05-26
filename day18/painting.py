import colorgram

colors = colorgram.extract('canvas.png',6)
list_of_tuples = []

for color in colors:

    tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    list_of_tuples.append(tuple)

print(list_of_tuples)