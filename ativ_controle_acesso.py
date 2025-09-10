# Entrada de dados
cargo = input("Digite o cargo do funcionário: ").strip().lower()
dia = input("Digite o dia da semana: ").strip().lower()

# Lista de dias úteis
dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

# Lógica de acesso
if cargo == "gerente":
    print("Acesso permitido: gerente tem acesso irrestrito.")
elif cargo == "analista":
    if dia in dias_uteis:
        print("Acesso permitido: analistas só entram em dias úteis.")
    else:
        print("Acesso negado: analistas não têm acesso no fim de semana.")
elif cargo == "estagiário":
    if dia in dias_uteis:
        print("Acesso permitido: estagiários só entram em dias úteis.")
    else:
        print("Acesso negado: estagiários não têm acesso no fim de semana.")
else:
    print("Cargo não reconhecido. Acesso negado.")

_