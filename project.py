# Get the user's income as input and convert it to an integer
salary = int(input("Enter your income: "))

# Define a function to calculate the tax based on the income (salary)
def Calculating_tax(salary):
    tax = 0

    if (salary <= 400000): #First tax slab
        tax = 0

    if (salary > 400000): #second tax slab
        if (salary <= 800000):
            tax = tax + (salary - 400000) * 0.05
        else:
            tax = tax + 20000

    if (salary > 800000): #third tax slab
        if (salary <= 1200000):
            tax = tax + (salary - 800000) * 0.1
        else:
            tax = tax + 40000

    if (salary > 1200000): #fourth tax slab
        if (salary <= 1600000):
            tax = tax + (salary - 1200000) * 0.15
        else:
            tax = tax + 60000

    if (salary > 1600000): #fifth tax slab
        if (salary <= 2000000):
            tax = tax + (salary - 1600000) * 0.2
        else:
            tax = tax + 80000

    if (salary > 1600000): #sixth tax slab
        if (salary <= 2000000):
            tax = tax + (salary - 1600000) * 0.25
        else:
            tax = tax + 100000

    if (salary > 2000000): #seventh tax slab
        if (salary <= 2400000):
            tax = tax + (salary - 2000000) * 0.3
        else:
            tax = tax + 120000

    if (salary > 2400000): #eight tax slab
        tax = tax + (salary - 2400000) * 0.35

    # Print the final calculated total tax
    print("Your overall tax is: ", tax)
    
    return tax

# Call the function with the input salary to calculate and print the tax
Calculating_tax(salary)