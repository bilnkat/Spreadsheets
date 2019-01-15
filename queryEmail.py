import csv

def emailQuery(csvData, results, email):

    with open(csvData, newline="", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for row in reader:
            tmp = ', '.join(row)
            if email in tmp:
                with open(results, "a", newline="", encoding="utf8") as rcsv:
                    writer = csv.writer(rcsv, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(tmp)