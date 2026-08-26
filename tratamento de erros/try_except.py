try:
    numeros = [1, 2, 3]
    print(numeros[10])
except IndexError as error:
    print(f"Esse index não existe {error}")
except ValueError:
    print("Valor não permitido")
else:
    print("PASSOU")
finally:
    print("Sempre executa")

"""except Exception:
      print("Erro desconhecido")"""



def converter_int(valor):
    try:
        return int(valor)
    except ValueError:
        print(f"'{valor}' não é número")
        return None
    except TypeError:
        print(f"Tipo {type(valor)} não pode ser convertido")
        return None

print(converter_int("123"))    # 123
print(converter_int("abc"))    # Não é número
print(converter_int(None))     # Tipo não pode ser convertido