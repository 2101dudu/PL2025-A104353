import ply.lex as lex
import sys
import json


# ------ HELPER FUNCTIONS ----------
def format_saldo(saldo):
    euros = int(saldo)
    cents = round((saldo - euros) * 100)
    return f"{euros}e{cents}c"


def format_troco(saldo):
    cents_total = int(round(saldo * 100))
    coins = [
        (200, "2e"),
        (100, "1e"),
        (50, "50c"),
        (20, "20c"),
        (10, "10c"),
        (5, "5c"),
        (2, "2c"),
        (1, "1c")
    ]
    breakdown_list = []
    for value, label in coins:
        count = cents_total // value
        if count:
            breakdown_list.append(f"{count}x {label}")
            cents_total -= count * value
    if not breakdown_list:
        return "0"
    if len(breakdown_list) == 1:
        return breakdown_list[0]
    else:
        return ", ".join(breakdown_list[:-1]) + " e " + breakdown_list[-1]

# ------ HELPER FUNCTIONS ----------


file_path = "stock.json"

saldo = 0
stock = {}
with open(file_path, "r") as file:
    data = json.load(file)
    for product in data["stock"]:
        stock[product["cod"]] = product

print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
print("maq: Bom dia. Estou disponível para atender o seu pedido.")


tokens = [
    "LISTAR",
    "SELECIONAR",
    "MOEDA",
    "SAIR",
]


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_LISTAR(t):
    r'LISTAR'
    return t


def t_SELECIONAR(t):
    r'SELECIONAR\s+[A-Za-z]\d+'
    return t


def t_MOEDA(t):
    r'MOEDA(\s*(2e|1e|50c|20c|10c|5c|2c|1c),*)*\s*(2e|1e|50c|20c|10c|5c|2c|1c)\s*$'
    return t


def t_SAIR(t):
    r'SAIR'
    return t


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

for line in sys.stdin:
    lexer.input(line)

    for token in lexer:
        if token.type == "LISTAR":
            print("maq:")
            print("cod    |  nome      |  quantidade  |  preço")
            print("---------------------------------")
            for product in stock.values():
                print(f"        {product['cod']}        |        {product['nome']: <30}         |      {
                      product['quant']: <2}       |      {product['preco']: <2}")
        elif token.type == "SELECIONAR":
            cod = token.value.split()[1]
            product = stock.get(cod)
            if product is None:
                print("maq: Produto inexistente")
                continue

            if saldo < product["preco"]:
                print("maq: Saldo insufuciente")
                print("maq: Saldo =", format_saldo(saldo))
                print("maq: Produto =", format_saldo(product["preco"]))
                continue

            if product["quant"] == 0:
                print("maq: Produto sem stock")
                continue

            product["quant"] -= 1
            saldo -= product["preco"]
            print("maq: Produto comprado")
            print("maq: Saldo restante =", format_saldo(saldo))

        elif token.type == "MOEDA":
            moedas_str = " ".join(token.value.split()[1:])
            moedas = moedas_str.split(",")
            for moeda in moedas:
                moeda = moeda.strip()
                if moeda:
                    if moeda.endswith('e'):
                        saldo += int(moeda[:-1])
                    elif moeda.endswith('c'):
                        saldo += int(moeda[:-1])/100

            print("maq: Saldo =", format_saldo(saldo))

        elif token.type == "SAIR":
            with open(file_path, "w") as file:
                json.dump({"stock": list(stock.values())}, file, indent=4)

            print("maq: Troco =", format_troco(saldo))
            exit(0)
