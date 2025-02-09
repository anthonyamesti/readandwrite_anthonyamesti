import csv

customer_totals = {}

with open("sales.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
   
    for row in reader:
        customer_id = row[0]
        subtotal = float(row[3])
        tax = float(row[4])
        freight = float(row[5])
        total = subtotal + tax + freight

        if customer_id in customer_totals:
            customer_totals[customer_id] += total
        else:
            customer_totals[customer_id] = total

with open("salesreport.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Customer ID", "Total"])
   
    for customer in sorted(customer_totals.keys(), key=int):
        writer.writerow([customer, f"{customer_totals[customer]:.2f}"])
