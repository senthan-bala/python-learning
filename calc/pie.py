import pygal

datafile = open("games/files/input-data.txt", "r")
file_text = datafile.read()
lines = file_text.splitlines()

pie = pygal.Pie()
bar = pygal.Bar()
for line in lines:
    fruit, price = line.split(",")
    pie.add(fruit, int(price))
    bar.add(fruit, int(price))

pie.render_to_file("games/files/chart.svg")
bar.render_to_file("games/files/chart.svg")
