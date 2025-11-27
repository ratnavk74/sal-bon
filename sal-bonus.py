import sys

if len(sys.argv) == 2:
    salary = float(sys.argv[1])
    print("User provided salary:")
else:
    salary = 50000   
    print("No input provided — using default salary:")

bonus = salary * 0.10
total_salary = salary + bonus

print("\n----- SALARY BONUS CALCULATION -----")
print("Salary:", salary)
print("Bonus (10%):", bonus)
print("Total Salary:", total_salary)
