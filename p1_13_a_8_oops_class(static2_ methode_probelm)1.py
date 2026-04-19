class Product:
    type_product_name = "Electronic devices"

    def __init__(self, p_name, p_storage, p_model, price):
        self.p_name = p_name
        self.p_storage = p_storage
        self.p_model = p_model
        self.price = price

    @classmethod
    def class_data(cls):
        print(cls.type_product_name)

    @staticmethod
    def product_dis(price, discount):
        return (price * discount) / 100   # ✅ return value

    def actual_price(self, discount):
        discount_amount = Product.product_dis(self.price, discount)
        total_price = self.price - discount_amount
        print("Final price =", total_price)

    def get_data(self):
        print(f"{self.p_name} {self.p_storage}GB {self.p_model} Price: {self.price}")


# object
p1 = Product("Samsung", 256, "Latest Model", 7000)

Product.class_data()
print()

p1.get_data()
print()

# discount calculation
p1.actual_price(10)