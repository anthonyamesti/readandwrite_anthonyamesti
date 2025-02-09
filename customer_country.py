import csv

with open("customers.csv", mode="r", newline="") as input_file:
    reader = csv.reader(input_file) 

    header = next(reader)
    name_index = header.index("FirstName") 
    name_index = header.index("LastName") 

    country_index = header.index("Country")  

    with open("customer_country.csv", mode="w", newline="") as output_file:
        writer = csv.writer(output_file) 

        writer.writerow(["Full Name", "Country"])  

        count=0
        for row in reader:
            writer.writerow([row[1] + ' ' + row[2], row[4]])
            count += 1  # Increase customer count for each row

print(f"Total number of customers: {count}")
print("Finished creating customer_countries.csv!")
