# Sistema de Portaria

Pequeno projeto em Python para consultar convidados, registrar check-ins e acompanhar a ocupação de um evento. Os dados são persistidos em CSV.

## Estrutura

- `main.py`: inicia a interface da portaria e processa os comandos digitados.
- `portaria.py`: contém as classes `Convidado` e `GerenciadorPortaria`, responsáveis pelas regras de negócio, buscas e persistência.
- `test_portaria.py`: testes automatizados das principais regras do sistema.
- `convidados.txt`: relação inicial de convidados usada para criar a base quando o CSV não existe.
- `lista_eventos.csv`: base persistida com nome, código, status e horário de entrada.

## Como executar

Na raiz do repositório:

```bash
python3 Projeto/main.py
```

Comandos disponíveis:

- Digite um nome ou código para localizar um convidado e confirmar sua entrada.
- `total`: exibe a quantidade de convidados, presenças e ocupação.
- `confirmados`: lista quem já realizou o check-in.
- `pendentes`: lista quem ainda não realizou o check-in.
- `pendente <nome ou código>`: desfaz o check-in de um convidado.
- `sair`: encerra o programa.

## Testes

Com o `pytest` instalado:

```bash
python -m pytest -q Projeto/test_portaria.py
```
