class Employee:
    def __init__(self):
        self.empid = 0
        self.name = ""
        self.basic_pay = 0
        self.ta = 0
        self.da = 0
        self.gross_pay = 0
    def calc(self):
        self.gross_pay = self.basic_pay + (10 * self.ta / 100) + (40 * self.da / 100)
    def disp(self):
        print("\nEmployee Details")
        print("Employee ID:", self.empid)
        print("Name:", self.name)
        print("Basic Pay:", self.basic_pay)
        print("TA:", self.ta)
        print("DA:", self.da)
        print("Gross Pay:", self.gross_pay)
emp = Employee()
emp.empid = int(input("Enter Employee ID: "))
emp.name = input("Enter Employee Name: ")
emp.basic_pay = float(input("Enter Basic Pay: "))
emp.ta = float(input("Enter TA: "))
emp.da = float(input("Enter DA: "))
emp.calc()
emp.disp()
