import matplotlib.pyplot as plt

# Data
companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','ATOS','Amdocs']
recruitments = [120,150,170,90,110,130,80,95]

# a) Bar Chart
plt.bar(companies, recruitments)
plt.title("Company Recruitment")
plt.xlabel("Companies")
plt.ylabel("Number of Students")
plt.xticks(rotation=30)
plt.show()

# b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        explode=[0.1,0,0,0,0,0,0,0], shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruitments, labels=companies)
centre_circle = plt.Circle((0,0),0.5,color='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# e) Comparison (IBM vs Amdocs)
plt.bar(['IBM','Amdocs'], [90,95])
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("Students")
plt.show()