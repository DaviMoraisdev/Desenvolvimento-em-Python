class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")

    # Método para buscar dados
    def get_salary(self):
        return self.__salary

    # Método para modificar atributo privado 
    def set_salary(self, salary):
        self.__salary = salary

Davi = Employee("Davi", 4000)
Zé = Employee("Zé", 5000)
Davi.name = "Davi 2"
Davi.show()
Zé.show()
Davi.set_salary(10000)
Davi.show()