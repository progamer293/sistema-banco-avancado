import CPF,listadecontas as loc
cpf=""
login = False

class contabancariaOBJ():

    def __init__(self):
        self.saldo = 0
        self.nome = None
        self.email = None
        self.celular = None
        self.chavepix = None
        self.cpf = None

    def dados(self, nome, email, celular, chavepix,cpf):
        self.nome = nome
        self.email = email
        self.celular = celular
        self.chavepix = chavepix
        self.cpf = cpf

    def depositar(self,valor): 
        if valor > 0 :
            self.saldo += valor
        else:
            print("nao foi possivel fazer o deposito")

    def transferir(self,valortransferencia):
        if valortransferencia > self.saldo:
            print("transferencia recusada")
        elif valortransferencia <=0:
            print("transferencia recusada")
        else:
            self.saldo -= valortransferencia

    def versaldo(self):
        print(self.saldo)

def menuFUN():
    #efetua o login
    
    def loginFUN():
        global cpf,login
        def loginvalidFUN(login):
            if login:
                return False
        if loginvalidFUN(login):
            return None
        # servira para verificar se ha a necessidade de fazer login
    
        # cpfv = cpf valido
        nome = input("insira seu nome").title().strip()
        idade = int(input("insira sua idade"))
        cpf = input("insira seu cpf")
        senha = int(input("escolha uma senha para usar (nao a esqueça)"))


        # validar o cpf      
        CPFv = CPF.validarFUN(cpf)
        celular = ""
        email = ""
        while True:

            email = input("insira um email(confirme sem enviar nenhum caractere para alterar para telefone)")

            if email == "":
                celular = input("insira um numero de celular(confirme sem enviar nenhum caractere para alterar para email)")

            if celular != "" :
                celular = int(celular)
            if email != "" or celular != "":
                break
        conta = contabancariaOBJ()
        conta.dados(nome=nome,cpf=cpf,email=email,celular=celular,chavepix=input("insira uma chave pix"))
        loc.locUPDFUN(cpf=cpf, conta=conta) 
        

    def mainmenuFUN():
        ContaAtual = loc.listadecontas[cpf]
        match int(input("escolha entre|1 transferir|2 ver saldo|3 fazer deposito|4 verificar informaçoes|5 alterar informações|6 sair da conta")):
            case 1:
                ContaAtual.transferir(int(input("insira o valor da transferencia se o valor for maior do que o que tiver na conta, a operaçao nao sera realizada")))

            case 2:
                print(ContaAtual.saldo)
                
            case 3:
                ContaAtual.depositar(valor = int(input("insira o valorconta que deseja depositar")))

            case 4:
                print(f"saldo da conta: {ContaAtual.saldo}")
                print(f"nome de usoario: {ContaAtual.nome}")
                if ContaAtual.email != "":
                    print(f"email veinculado a conta: {ContaAtual.email}")
                if ContaAtual.celular != "":
                    print(f"numero veinculado a conta: {ContaAtual.celular}")
                print(f"chaves pix atuais: {ContaAtual.chavepix}")
                print(f"cpf cadastrado: {ContaAtual.cpf}")
            case 5:
                print("1 nome | 2 email| 3 celular| 4 chave pix")
                escolhas = input("qual informação gostaria de mudar, separe-as con virgula, exp: 1,3,4,2")
                escolhas = escolhas.split(",")
                if "1" in escolhas:
                    ContaAtual.nome = input("insira o novo nome")
                    
                if "2" in escolhas:
                    if ContaAtual.email != '':
                        ContaAtual.email = input("insira o novo email")

                    else: ContaAtual.email = input("insira o email para veincular a esta conta")

                if "3" in escolhas:
                    if ContaAtual != '':
                        ContaAtual.celular = input("insira o novo numero")

                    else: ContaAtual.celular = input("insira o numero para veincular a esta conta")

                if "4" in escolhas:
                    ContaAtual.chavepix = input("insira a nova chave pix")
            case 6:
                global login 
                ContaAtual = None

    while True:
        loginFUN()
        mainmenuFUN()

menuFUN()
