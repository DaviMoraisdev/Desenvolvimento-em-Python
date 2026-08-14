class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price

    def __str__(self):
        return f"{self._brand}{self._model_name}"

    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para{phone_num}")

class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price)

        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera

Samsung = Phone('Samsung', 'S23', '2300')
print(Samsung)
Samsung.make_a_call(12345678989)
print(f"Valor do {Samsung._brand}{Samsung._model_name} é {Samsung._price}")
print(vars(Samsung))

Iphone = Smartphone("Iphone", "17", 10000, "32GB", "1TB", "50MP")
print(Iphone)
Iphone.make_a_call(11654985156)
print(f"Valor do {Iphone._brand} {Iphone._model_name} é {Iphone._price}")