import json

def cadastrar_paciente(nome, idade, sexo, peso, altura):
    # Carregar os dados existentes, se houver
    try:
        with open('pacientes.json', 'r') as arquivo:
            pacientes = json.load(arquivo)
    except FileNotFoundError:
        pacientes = []

    # Adicionar o novo paciente à lista
    novo_paciente = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo,
        'peso': peso,
        'altura': altura
    }
    pacientes.append(novo_paciente)

    # Salvar os dados atualizados no arquivo
    with open('pacientes.json', 'w') as arquivo:
        json.dump(pacientes, arquivo, indent=4)

    print("Paciente cadastrado com sucesso!")

def pesquisar_paciente(nome):
    # Carregar os dados existentes
    try:
        with open('pacientes.json', 'r') as arquivo:
            pacientes = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum paciente cadastrado ainda.")
        return

    # Pesquisar pelo paciente
    encontrado = False
    for paciente in pacientes:
        if paciente['nome'] == nome:
            print("Paciente encontrado:")
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"Sexo: {paciente['sexo']}")
            print(f"Peso: {paciente['peso']}")
            print(f"Altura: {paciente['altura']}")
            encontrado = True
            break

    if not encontrado:
        print("Paciente não encontrado.")

# Exemplo de cadastro de pacientes
cadastrar_paciente("Allan Kardec", 30, "Masculino", 75, 1.75)
cadastrar_paciente("Joana D'Arc", 25, "Feminino", 60, 1.65)

# Exemplo de pesquisa de paciente
nome_paciente = input("Digite o nome do paciente que deseja pesquisar: ")
pesquisar_paciente(nome_paciente)

