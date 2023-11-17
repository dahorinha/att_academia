import mysql.connector

academia = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "302302",
    database = "academia_vinicius"
)
while True:
    menu_pri = int(input("Digite 1 para inserir, 2 para atualizar, 3 para deletar, 4 para visualizar, ou 0 para sair: "))
    if menu_pri == 0:
        break

    elif menu_pri == 1:
        menu_adc = int(input("Menu: \n1 - Para incluir alunos\n2 - Para incluir modalidade\n3 - Para incluir personal\n4 - Para incluir funcionários\n"))

        if menu_adc == 1:
            campos = ['Nome', 'Telefone', 'endereço']
            valores = [input(f"Digite o {campo}: ") for campo in campos]
            inserir_registro('aluno', campos, valores)

        elif menu_adc == 2:
            campos = ['nome_mod', 'professor', 'turno']
            valores = [input(f"Digite a {campo}: ") for campo in campos]
            inserir_registro('modalidade', campos, valores)

        elif menu_adc == 3:
            campos = ['nome', 'telefone', 'endereço']
            valores = [input(f"Digite o {campo}: ") for campo in campos]
            inserir_registro('personal', campos, valores)

        elif menu_adc == 4:
            campos = ['nome', 'cpf', 'departamento', 'cpf_sup', 'salario']
            valores = [input(f"Digite o {campo}: ") for campo in campos]
            inserir_registro('funcionario', campos, valores)
    elif menu_pri == 2:
        tabela = input("Você quer atualizar qual tabela: aluno, modalidade, personal ou funcionario?  ")
        campo = input("Digite o campo que você deseja atualizar: ")
        valor = input("Digite o novo valor para atualizar: ")
        condicoes = input("Digite as condições (ex: id = 1): ")
        atualizar_registro(tabela, campo, valor, condicoes)

    elif menu_pri == 3:
        tabela = input( "Você deseja deletar informações de qual tabela? \n1 - Para alunos\n2 - Para modalidade\n3 - Para personal\n4 - Para funcionários\n")
        condicoes = input("Digite as condições para deletar (ex: id = 1): ")
        deletar_registro(['aluno', 'modalidade', 'personal', 'funcionario'][int(tabela) - 1], condicoes)

    elif menu_pri == 4:
        menu_ver = int(input("Menu: \n1 - Para visualizar alunos\n2 - Para visualizar modalidade\n3 - Para visualizar personal\n4 - Para visualizar funcionários\n"))
        if menu_ver in range(1, 5):
            visualizar_registros(['aluno', 'modalidade', 'personal', 'funcionario'][menu_ver - 1])

    else:
        print("Opção inválida. Tente novamente.")
