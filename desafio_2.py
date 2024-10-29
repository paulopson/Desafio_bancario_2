#\n quebra de linha



menu = """

   =============== MENU ==================   
    [1] Depositar
    
    [2] Sacar

    [3] Extrato

    [4] Novo Usuario

    [5] Nova conta
      
    [0] Sair
      
    =====================================
    Selecione ação desejada: """



def depositar(saldo, valor, extrato, /): #passando por posição
    if valor > 0: #verificando se o valor e maior que zero
        saldo += valor #adicionando o deposito no saldo
        extrato += f"\nDeposito: R${valor: .2f}" #colocando o valor depositado no extrato
        print("\n Deposito realizado com sucesso")
    else:
        print("\n E.R.R.O VALOR INVALIDO")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numeros_saque, limite_saque):
    saldo_insuficiente = valor > saldo #pra ver se tem saldo para sacar

    saque_excedido = valor > limite #excedeu o limite de saque

    saque_diario = numeros_saque >= limite_saque #limite de saque diario

    if saldo_insuficiente:
        print("!!! ERRO !!! Saldo insuficiente, confira o saldo da conta")
        
    elif saque_excedido:
        print("!!! ERRO !!! O valor do saque ultrapassa o limite. Tente novamente")
        
    elif saque_diario:
        print("!!! ERRO !!! Limite de saques diarios excedidos, volte amamhã")


    elif valor > 0:
        saldo -= valor #tirando o valor sacado do saldo
        extrato += f"\nSaque: R${valor: .2f}\n" #colocando o valor sacado no extrato
        numeros_saque += 1 #adcionando mais um no numero de saque, para ele começar a contar
        print("\n Saque realizado com sucesso")
    else:
        ("!!! ERRO !!! Valor de saque invalido")
        
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("Não existem movimentações." if not extrato else extrato) #Verificando se existe movimentaçao no extrato
    print(f"\nSaldo: R$ {saldo: .2f}") # mostrando o saldo em conta


def novo_user(usuarios):
    cpf = input("Informe seu cpf: ")
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
        print("E.R.R.O Ja existe usuario com esse Cpf")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe a data do seu nascimento (dd-mm-aa): ")
    endereco = input("Informe seu endereço completo: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) #Adicionando ele como dicionario

    print("Usuario criado com sucesso")


def filtrar_user(cpf, usuarios):
    usuarios_filtrado = [usuario for usuario  in usuarios if usuario ["cpf"] == cpf] #fazendo um compreção de lista para ver se a lista usuario tem algum usuario com o mesmo cpf digitado
    return usuarios_filtrado[0] if usuarios_filtrado else None


def criar_conta(agencia, numero, usuarios):
    cpf = input("Informe seu cpf: ")
    usuario = filtrar_user(cpf, usuarios)

    if usuario:
        print("Conta criada")
        return {"agencia": agencia, "numero_conta": numero, "usuario": usuario}
    
    print("Usuario nao encontrado E.R.R.O")
    




saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
limite_saque = 3
AGENCIA = "0001"
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "1":
        valor= float(input("Quanto deseja depositar: ")) 

        saldo, extrato = depositar(saldo, valor, extrato)      

    
    elif opcao == "2":
        valor= float(input("Valor do saque: "))
        
        saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numeros_saque = numeros_saques, limite_saque = limite_saque, ) 


    elif opcao == "3":
        exibir_extrato(saldo, extrato = extrato)

    
    elif opcao == "4":
       novo_user(usuarios)

    
    elif opcao == "5":
        numero = len(contas) + 1
        conta = criar_conta(AGENCIA, numero, usuarios)

        if conta:
            contas.append(conta)


    elif opcao == "0":
        print(       " Obrigado por usar nossos serviços !         ")
        break
    
   
    else:
        print("--------------------[ E R R O ]------------------")
        
    
        