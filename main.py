class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    def show_info(self):
        print(f"🚗 {self.brand} {self.model} ({self.year})")
        print(f"Narx: {self.price:,} so‘m")
    
    def update_price(self, new_price):
        self.price = new_price
        print(f"Narx yangilandi: {new_price:,} so‘m")

# Test
car = Car("Toyota", "Camry", 2023, 45000000)
car.show_info()
car.update_price(42000000)
