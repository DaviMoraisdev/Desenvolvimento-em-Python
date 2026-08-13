import re


def from_text(string):
    pattern = r"Meu video game é (?P<name>\w+) e o preço é (?P<price>\d+) reais"
    match = re.fullmatch(pattern, string)

    if match is None:
        raise ValueError("O texto não está no formato esperado.")

    return match.group("name"), int(match.group("price"))


print(from_text("Meu video game é WiiU e o preço é 1000 reais"))
