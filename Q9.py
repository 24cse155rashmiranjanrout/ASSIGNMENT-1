class Product:
    def input(self):
        self.product_no = int(input("Enter product number: "))
        self.product_name = input("Enter product name: ")
        self.cost = float(input("Enter cost: "))
        self.quantity = int(input("Enter quantity: "))
    def calculate(self):
        self.total_amount = self.cost * self.quantity
    def display(self):
        print("Product no:", self.product_no)
        print("Product name:", self.product_name)
        print("Cost:", self.cost)
        print("Quantity:", self.quantity)
        print("Total amount:", self.total_amount)
products = []
for i in range(5):
    print("\nEnter product", i + 1)
    p = Product()
    p.input()
    p.calculate()
    products.append(p)
highest = products[0]

for p in products:
    if p.total_amount > highest.total_amount:
        highest = p
print("\nProduct with highest total amount")
highest.display()
        
