class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        if hourly_rate < 0 or hours_worked < 0:
            raise ValueError("❌ Wages and hours must be non-negative.")
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        base_hours = min(self.hours_worked, 160)
        overtime_hours = max(0, self.hours_worked - 160)
        base_salary = base_hours * self.hourly_rate
        overtime_pay = overtime_hours * self.hourly_rate * 1.5
        return base_salary, overtime_pay

# --- Demo ---
employees = []
n = int(input("Enter number of employees: "))
if n <= 0:
    print("❌ Must have at least one employee.")
else:
    for _ in range(n):
        name = input("Name: ")
        rate = float(input("Hourly wage: "))
        hours = float(input("Hours worked: "))
        employees.append(Employee(name, rate, hours))

    print("\n💵 Payroll Report:")
    for emp in employees:
        base, overtime = emp.calculate_salary()
        print(f"{emp.name}: Hours={emp.hours_worked}, Base={base:.2f}, Overtime={overtime:.2f}, Total={base+overtime:.2f}")
