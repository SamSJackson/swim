import csv 

links_file = "links/freestyle-advanced-workouts.txt"
distances_file = "links/distances.txt"

with open(links_file, 'r') as f:
    links = f.readlines()
    links = dict([(line.strip().rsplit("/")[-1], line.strip()) for line in links])

with open(distances_file, 'r') as f:
    distance_lines = f.readlines()
    distances = dict([line.split() for line in distance_lines])

output = []
for (name, link) in links.items():
    distance = distances.get(name)

    if name.startswith("dr1"):
        name = "ocean-sunfish"
        distance = 4600

    tup = (name, distance, link)
    output.append(tup)


# TODO: Add another column detailing the intensity/style of workout (vo2, threshold, etc.)
with open("db.csv", 'w+') as f:
    fieldnames = ["workout_name", "distance", "url"]
    writer = csv.writer(f, delimiter=',')

    writer.writerow(fieldnames)
    for tup in output:
        writer.writerow(tup)
