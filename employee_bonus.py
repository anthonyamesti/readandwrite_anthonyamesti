import csv  

with open("employee_data.csv", mode="r", newline="") as file:
    reader = csv.reader(file)  

    header = next(reader)  
    print("Employee Details:\n")  

    for row in reader:
        employee_id = row[0]  
        name = row[1]  
        age = row[2]  
        salary = float(row[3])  
        hours_worked = row[4]  
        productivity = row[5]  
        team = row[6]  
        bonus_percentage = float(row[7])  

        bonus_amount = salary * bonus_percentage

        print(f"Name: {name}")
        print(f"Salary:  $  {salary:,.2f}")
        print(f"Bonus:   $   {bonus_amount:,.2f}")
        Pay = salary+bonus_amount
        print(f"Pay:     $  {Pay:,.2f}")
        print("-" * 40)  
