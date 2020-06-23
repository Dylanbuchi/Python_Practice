import csv

filename = "files/FL_insurance_sample.csv"

file = open(filename)

csv_file = csv.reader(file)

# get 3 first objects in a line
for line in csv_file:
    policyID, statecode, country = line[0:3]

    if not line[0].isdigit():
        continue

    print(
        f"Policy ID: {policyID}\nState code: {statecode}\nCountry: {country}\n")
    break

file.close()


# write to a csv file
people = [["Bob", "20"], ["John", "45"], ["Doug", "69"]]

filename = "files/people.csv"
with open(filename, "w") as people_csv:
    writer = csv.writer(people_csv)
    writer.writerows(people)


# read it
with open(filename) as file:
    for line in file:
        print(line.strip())
