"""
1 - O método de classe utiliza o parâmetro referente à classe.
2 - O método de classe pode acessar ou modificar o estado da classe
3 - Usamos o decorator @classmethod para criar um método de classe
"""
import re


class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_text(cls, string):
        pattern = r"Meu video game é (?P<name>\w+) e o preço é (?P<price>\d+) reais"
        match = re.fullmatch(pattern, string)

        if match is None:
            raise ValueError("O texto não está no formato esperado.")

        name = match.group("name")
        price = int(match.group("price"))
        return cls(name, price)


wii_u = Console.from_text("Meu video game é WiiU e o preço é 1000 reais")
xbox_one = Console.from_text("Meu video game é XboxOne e o preço é 1500 reais")
print(wii_u.__dict__)
print(xbox_one.__dict__)
