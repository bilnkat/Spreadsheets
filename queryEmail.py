import csv

email = ""

with open(r"C:\Users\bgeneral\Desktop\test.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    for row in reader:
        if "777" in row[0]:
            with open(r"C:\Users\bgeneral\Desktop\results.csv", "a", newline="") as rcsv:
                writer = csv.writer(rcsv, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
                writer.writerow(row[0])
            # print(row[0])

