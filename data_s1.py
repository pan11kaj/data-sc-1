import csv;
rows = []
with open("main.csv","r") as file:
    read = csv.reader(file)
    for r in read:
        rows.append(r)
headers = rows[0]
planet_data_rows = rows[1:]
planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
    planet_masses.append(planet_data[4])
    planet_radiuses.append(planet_data[5])
    planet_names.append(planet_data[2])
planet_gravity = []
for index, name in enumerate(planet_names):
    gravity = (float(planet_masses[index])*1.989e+30) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) *6.957e+8
    planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()