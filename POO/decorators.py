from .decorator import my_decorator, uppercase_decorator, split_string

# 1 - Exemplo
@my_decorator
def my_function():
    print("Dentro da função")

my_function()

# 2 - Exemplo
@uppercase_decorator
def text():
    return "Hello World"

print(text())

# 3 - Exemplo
@split_string
def example():
    return "Aprendendo Python e criando decorators"

print(example())