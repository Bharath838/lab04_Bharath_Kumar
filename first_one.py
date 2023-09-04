class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.id} {self.name} {self.age} {self.salary}"

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

print("Choose the sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")
choice = int(input())

if choice == 1:
    employees.sort(key=lambda x: x.age)
elif choice == 2:
    employees.sort(key=lambda x: x.name)
elif choice == 3:
    employees.sort(key=lambda x: x.salary)

for employee in employees:
    print(employee)
