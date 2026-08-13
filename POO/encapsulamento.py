class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")

Davi = Employee("Davi", 4000)
Zé = Employee("Zé", 5000)
Davi.show()
Zé.show()
Davi.__salary = 44000
Davi.show()
