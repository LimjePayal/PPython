import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
auto_emp = df[df["Department"] == "Automotive"]
print("\nEmployees in Automotive:\n", auto_emp)

# b) Details by Employee ID
emp_id = int(input("\nEnter Employee ID: "))
emp_details = df[df["Employee ID"] == emp_id]
print("\nEmployee Details:\n", emp_details)

# c) Developers in Infosys
developers = df[df["Designation"] == "Developer"]
print("\nDevelopers in Infosys:\n", developers)